# Copyright 2018/2019 The RLgraph authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from rlgraph import get_backend
from rlgraph.components.loss_functions import LossFunction
from rlgraph.spaces import IntBox
from rlgraph.spaces.space_utils import sanity_check_space
from rlgraph.utils import pytorch_one_hot
from rlgraph.utils.decorators import rlgraph_api, graph_fn
from rlgraph.utils.pytorch_util import pytorch_tile
from rlgraph.utils.util import get_rank

if get_backend() == "tf":
    import tensorflow as tf
elif get_backend() == "pytorch":
    import torch


class DQNLossFunction(LossFunction):
    """
    The classic 2015 DQN Loss Function [1] with options for "double" Q-losses [2], Huber loss [3], and container
    actions [4]:

    L = Expectation-over-uniform-batch(r + gamma x max_a'Qt(s',a') - Qn(s,a))^2
    Where Qn is the "normal" Q-network and Qt is the "target" net (which is a little behind Qn for stability purposes).

    [1] Human-level control through deep reinforcement learning. Mnih, Kavukcuoglu, Silver et al. - 2015
    [2] Deep Reinforcement Learning with Double Q-learning. v. Hasselt, Guez, Silver - 2015
    [3] https://en.wikipedia.org/wiki/Huber_loss
    [4] Action Branching Architectures for Deep Reinforcement Learning. Tavakoli, Pardo, and Kormushev - 2017
    """
    def __init__(self, double_q=False, huber_loss=False, importance_weights=False, n_step=1,
                 shared_container_action_target=True, scope="dqn-loss-function", **kwargs):
        """
        Args:
            double_q (bool): Whether to use the double DQN loss function ([2]).
            huber_loss (bool): Whether to apply a huber loss correction ([3]).
            importance_weights (bool): Where to use importance weights from a prioritized replay.
            n_step (int): n-step adjustment to discounting.

            shared_container_action_target (bool): Whether - only in the case of container actions - the target term
                should be shared (average) over all action components' single loss terms. Default: True.
        """
        self.double_q = double_q
        self.huber_loss = huber_loss
        assert n_step >= 1, "Number of steps for n-step learning must be >= 1, is {}".format(n_step)
        # TODO reward must be preprocessed to work correctly for n-step.
        # For Apex, this is done in the worker - do we want to move this as an in-graph option too?
        self.n_step = n_step
        self.shared_container_action_target = shared_container_action_target

        # Clip value, see: https://en.wikipedia.org/wiki/Huber_loss
        self.huber_delta = kwargs.get("huber_delta", 1.0)
        self.importance_weights = importance_weights

        super(DQNLossFunction, self).__init__(scope=scope, **kwargs)

        self.flat_action_space = None
        self.ranks_to_reduce = 0  # How many ranks do we have to reduce to get down to the final loss per batch item?

    def check_input_spaces(self, input_spaces, action_space=None):
        """
        Do some sanity checking on the incoming Spaces:
        """
        assert action_space is not None
        self.action_space = action_space
        self.flat_action_space = action_space.flatten()
        # Check for IntBox and num_categories.
        sanity_check_space(self.action_space, must_have_categories=True, allowed_sub_types=[IntBox])
        self.ranks_to_reduce = len(self.action_space.get_shape(with_batch_rank=True)) - 1

    @rlgraph_api
    def loss(self, q_values_s, actions, rewards, terminals, qt_values_sp, q_values_sp=None, importance_weights=None):
        loss_per_item = self.loss_per_item(
            q_values_s, actions, rewards, terminals, qt_values_sp, q_values_sp, importance_weights
        )
        total_loss = self.loss_average(loss_per_item)
        return total_loss, loss_per_item

    @rlgraph_api
    def loss_per_item(self, q_values_s, actions, rewards, terminals, qt_values_sp, q_values_sp=None,
                      importance_weights=None):
        # Get the targets per action.
        td_targets = self._graph_fn_get_td_targets(rewards, terminals, qt_values_sp, q_values_sp)
        # Average over container sub-actions.
        if self.shared_container_action_target is True:
            td_targets = self._graph_fn_average_over_container_keys(td_targets)

        # Calculate the loss per item.
        loss_per_item = self._graph_fn_loss_per_item(td_targets, q_values_s, actions, importance_weights)
        # Average over container sub-actions.
        loss_per_item = self._graph_fn_average_over_container_keys(loss_per_item)

        # Apply huber loss.
        loss_per_item = self._graph_fn_apply_huber_loss_if_necessary(loss_per_item)

        return loss_per_item

    @graph_fn(flatten_ops=True, split_ops=True, add_auto_key_as_first_param=True)
    def _graph_fn_get_td_targets(self, key, rewards, terminals, qt_values_sp, q_values_sp=None):
        """
        Args:
            rewards (SingleDataOp): The batch of rewards that we received after having taken a in s (from a memory).
            terminals (SingleDataOp): The batch of terminal signals that we received after having taken a in s
                (from a memory).
            qt_values_sp (SingleDataOp): The batch of Q-values representing the expected accumulated discounted
                returns (estimated by the target net) when in s' and taking different actions a'.
            q_values_sp (Optional[SingleDataOp]): If `self.double_q` is True: The batch of Q-values representing the
                expected accumulated discounted returns (estimated by the (main) policy net) when in s' and taking
                different actions a'.

        Returns:
            SingleDataOp: The target values vector.
        """
        qt_sp_ap_values = None

        # Numpy backend primarily for testing purposes.
        if self.backend == "python" or get_backend() == "python":
            from rlgraph.utils.numpy import one_hot
            if self.double_q:
                a_primes = np.argmax(q_values_sp, axis=-1)
                a_primes_one_hot = one_hot(a_primes, depth=self.flat_action_space[key].num_categories)
                qt_sp_ap_values = np.sum(qt_values_sp * a_primes_one_hot, axis=-1)
            else:
                qt_sp_ap_values = np.max(qt_values_sp, axis=-1)

            for _ in range(qt_sp_ap_values.ndim - 1):
                rewards = np.expand_dims(rewards, axis=1)

            qt_sp_ap_values = np.where(terminals, np.zeros_like(qt_sp_ap_values), qt_sp_ap_values)

        elif get_backend() == "tf":
            # Make sure the target policy's outputs are treated as constant when calculating gradients.
            qt_values_sp = tf.stop_gradient(qt_values_sp)

            if self.double_q:
                # For double-Q, we no longer use the max(a')Qt(s'a') value.
                # Instead, the a' used to get the Qt(s'a') is given by argmax(a') Q(s',a') <- Q=q-net, not target net!
                a_primes = tf.argmax(input=q_values_sp, axis=-1)

                # Now lookup Q(s'a') with the calculated a'.
                one_hot = tf.one_hot(indices=a_primes, depth=self.flat_action_space[key].num_categories)
                qt_sp_ap_values = tf.reduce_sum(input_tensor=(qt_values_sp * one_hot), axis=-1)
            else:
                # Qt(s',a') -> Use the max(a') value (from the target network).
                qt_sp_ap_values = tf.reduce_max(input_tensor=qt_values_sp, axis=-1)

            # Make sure the rewards vector (batch) is broadcast correctly.
            for _ in range(get_rank(qt_sp_ap_values) - 1):
                rewards = tf.expand_dims(rewards, axis=1)

            # Ignore Q(s'a') values if s' is a terminal state. Instead use 0.0 as the state-action value for s'a'.
            # Note that in that case, the next_state (s') is not the correct next state and should be disregarded.
            # See Chapter 3.4 in "RL - An Introduction" (2017 draft) by A. Barto and R. Sutton for a detailed analysis.
            qt_sp_ap_values = tf.where(
                condition=terminals, x=tf.zeros_like(qt_sp_ap_values), y=qt_sp_ap_values
            )

        elif get_backend() == "pytorch":
            if not isinstance(terminals, torch.ByteTensor):
                terminals = terminals.byte()
            # Add batch dim in case of single sample.
            if qt_values_sp.dim() == 1:
                rewards = rewards.unsqueeze(-1)
                terminals = terminals.unsqueeze(-1)
                q_values_sp = q_values_sp.unsqueeze(-1)
                qt_values_sp = qt_values_sp.unsqueeze(-1)

            # Make sure the target policy's outputs are treated as constant when calculating gradients.
            qt_values_sp = qt_values_sp.detach()
            if self.double_q:
                # For double-Q, we no longer use the max(a')Qt(s'a') value.
                # Instead, the a' used to get the Qt(s'a') is given by argmax(a') Q(s',a') <- Q=q-net, not target net!
                a_primes = torch.argmax(q_values_sp, dim=-1, keepdim=True)

                # Now lookup Q(s'a') with the calculated a'.
                one_hot = pytorch_one_hot(a_primes, depth=self.flat_action_space[key].num_categories)
                qt_sp_ap_values = torch.sum(qt_values_sp * one_hot.squeeze(), dim=-1)
            else:
                # Qt(s',a') -> Use the max(a') value (from the target network).
                qt_sp_ap_values = torch.max(qt_values_sp, -1)[0]

            # Make sure the rewards vector (batch) is broadcast correctly.
            for _ in range(get_rank(qt_sp_ap_values) - 1):
                rewards = torch.unsqueeze(rewards, dim=1)

            # Ignore Q(s'a') values if s' is a terminal state. Instead use 0.0 as the state-action value for s'a'.
            # Note that in that case, the next_state (s') is not the correct next state and should be disregarded.
            # See Chapter 3.4 in "RL - An Introduction" (2017 draft) by A. Barto and R. Sutton for a detailed analysis.
            # torch.where cannot broadcast here, so tile and reshape to same shape.
            if qt_sp_ap_values.dim() > 1:
                num_tiles = np.prod(qt_sp_ap_values.shape[1:])
                terminals = pytorch_tile(terminals, num_tiles, -1).reshape(qt_sp_ap_values.shape)
            qt_sp_ap_values = torch.where(
                terminals, torch.zeros_like(qt_sp_ap_values), qt_sp_ap_values
            )
        td_targets = (rewards + (self.discount ** self.n_step) * qt_sp_ap_values)
        return td_targets

    @graph_fn(flatten_ops=True, split_ops=True, add_auto_key_as_first_param=True)
    def _graph_fn_loss_per_item(self, key, td_targets, q_values_s, actions, importance_weights=None):
        """
        Args:
            td_targets (SingleDataOp): The already calculated TD-target terms (r + gamma maxa'Qt(s',a')
                OR for double Q: r + gamma Qt(s',argmaxa'(Q(s',a'))))

            q_values_s (SingleDataOp): The batch of Q-values representing the expected accumulated discounted returns
                when in s and taking different actions a.

            actions (SingleDataOp): The batch of actions that were actually taken in states s (from a memory).

            importance_weights (Optional[SingleDataOp]): If 'self.importance_weights' is True: The batch of weights to
                apply to the losses.

        Returns:
            SingleDataOp: The loss values vector (one single value for each batch item).
        """
        # Numpy backend primarily for testing purposes.
        if self.backend == "python" or get_backend() == "python":
            from rlgraph.utils.numpy import one_hot

            actions_one_hot = one_hot(actions, depth=self.flat_action_space[key].num_categories)
            q_s_a_values = np.sum(q_values_s * actions_one_hot, axis=-1)

            td_delta = td_targets - q_s_a_values

            if td_delta.ndim > 1:
                if self.importance_weights:
                    td_delta = np.mean(
                        td_delta * importance_weights,
                        axis=list(range(1, self.ranks_to_reduce + 1))
                    )

                else:
                    td_delta = np.mean(td_delta, axis=list(range(1, self.ranks_to_reduce + 1)))

        elif get_backend() == "tf":
            # Q(s,a) -> Use the Q-value of the action actually taken before.
            one_hot = tf.one_hot(indices=actions, depth=self.flat_action_space[key].num_categories)
            q_s_a_values = tf.reduce_sum(input_tensor=(q_values_s * one_hot), axis=-1)

            # Calculate the TD-delta (target - current estimate).
            td_delta = td_targets - q_s_a_values

            # Reduce over the composite actions, if any.
            if get_rank(td_delta) > 1:
                td_delta = tf.reduce_mean(input_tensor=td_delta, axis=list(range(1, self.ranks_to_reduce + 1)))

        elif get_backend() == "pytorch":
            # Add batch dim in case of single sample.
            if q_values_s.dim() == 1:
                q_values_s = q_values_s.unsqueeze(-1)
                actions = actions.unsqueeze(-1)
                if self.importance_weights:
                    importance_weights = importance_weights.unsqueeze(-1)

            # Q(s,a) -> Use the Q-value of the action actually taken before.
            one_hot = pytorch_one_hot(actions, depth=self.flat_action_space[key].num_categories)
            q_s_a_values = torch.sum((q_values_s * one_hot), -1)

            # Calculate the TD-delta (target - current estimate).
            td_delta = td_targets - q_s_a_values

            # Reduce over the composite actions, if any.
            if get_rank(td_delta) > 1:
                td_delta = torch.mean(td_delta, tuple(range(1, self.ranks_to_reduce + 1)), keepdim=False)

        # Apply importance-weights from a prioritized replay to the loss.
        if self.importance_weights:
            return importance_weights * td_delta
        else:
            return td_delta

    @graph_fn
    def _graph_fn_apply_huber_loss_if_necessary(self, td_delta):
        if self.backend == "python" or get_backend() == "python":
            if self.huber_loss:
                return np.where(
                    condition=np.abs(td_delta) <= self.huber_delta,
                    x=0.5 * np.square(td_delta),
                    y=self.huber_delta * (np.abs(td_delta) - 0.5 * self.huber_delta)
                )
            else:
                return 0.5 * np.square(x=td_delta)
        elif get_backend() == "tf":
            if self.huber_loss:
                return tf.where(
                    condition=tf.abs(x=td_delta) <= self.huber_delta,
                    x=0.5 * tf.square(x=td_delta),
                    y=self.huber_delta * (tf.abs(x=td_delta) - 0.5 * self.huber_delta)
                )
            else:
                return 0.5 * tf.square(x=td_delta)
        elif get_backend() == "pytorch":
            if self.huber_loss:
                # Not certain if arithmetics need to be expressed via torch operators.
                return torch.where(
                    torch.abs(td_delta) <= self.huber_delta,
                    # PyTorch has no `square`
                    0.5 * torch.pow(td_delta, 2),
                    self.huber_delta * (torch.abs(td_delta) - 0.5 * self.huber_delta)
                )
            else:
                return 0.5 * td_delta * td_delta
