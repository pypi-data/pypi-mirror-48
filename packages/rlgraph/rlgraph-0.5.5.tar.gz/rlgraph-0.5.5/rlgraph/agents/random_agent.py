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

from __future__ import absolute_import, division, print_function

from rlgraph.agents import Agent


class RandomAgent(Agent):
    """
    An Agent that picks random actions from the action Space.
    """
    def __init__(self, state_space, action_space, name="random-agent", **kwargs):
        super(RandomAgent, self).__init__(
            update_spec=dict(do_updates=False), state_space=state_space, action_space=action_space, name=name, **kwargs
        )
        self.action_space_batched = self.action_space.with_batch_rank()

    def get_action(self, states, internals=None, use_exploration=False, apply_preprocessing=True, extra_returns=None,
                   time_percentage=None):
        a = self.action_space_batched.sample(size=len(states[0]))
        if extra_returns is not None and "preprocessed_states" in extra_returns:
            return a, states
        else:
            return a

    def update(self, batch=None, time_percentage=None, **kwargs):
        # Return fake loss and loss-per-item.
        return 0.0, 0.0

    def _observe_graph(self, preprocessed_states, actions, internals, rewards, next_states, terminals):
        pass

    # Override these with pass so we can use them when testing distributed strategies.
    def set_weights(self, policy_weights, value_function_weights=None):
        pass

    def get_weights(self):
        pass

    def call_api_method(self, op, inputs=None, return_ops=None):
        pass

    def __repr__(self):
        return "RandomAgent()"
