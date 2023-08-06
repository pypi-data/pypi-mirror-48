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

import unittest

import numpy as np
from rlgraph.components.policies import Policy, SharedValueFunctionPolicy, DuelingPolicy
from rlgraph.spaces import *
from rlgraph.tests import ComponentTest
from rlgraph.tests.test_util import config_from_path, recursive_assert_almost_equal
from rlgraph.utils import sigmoid, softmax, relu, MAX_LOG_STDDEV, MIN_LOG_STDDEV, SMALL_NUMBER
from scipy.stats import beta, norm


class TestPolicies(unittest.TestCase):

    def test_policy_for_boolean_action_space(self):
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        state_space = FloatBox(shape=(4,), add_batch_rank=True)

        # action_space (simple boolean).
        action_space = BoolBox(add_batch_rank=True)

        policy = Policy(network_spec=config_from_path("configs/test_simple_nn.json"), action_space=action_space)
        test = ComponentTest(
            component=policy,
            input_spaces=dict(
                nn_inputs=state_space,
                actions=action_space,
            ),
            action_space=action_space
        )
        policy_params = test.read_variable_values(policy.variable_registry)

        # Some NN inputs.
        batch_size = 32
        states = state_space.sample(batch_size)
        # Raw NN-output.
        expected_nn_output = np.matmul(
            states, ComponentTest.read_params("policy/test-network/hidden-layer", policy_params)
        )

        test.test(("get_nn_outputs", states), expected_outputs=expected_nn_output, decimals=5)

        # Raw action layer output; Expected shape=(): 2=batch
        expected_action_layer_output = np.squeeze(np.matmul(
            expected_nn_output,
            ComponentTest.read_params("policy/action-adapter-0/action-network/action-layer", policy_params)
        ), axis=-1)
        test.test(
            ("get_adapter_outputs", states), expected_outputs=dict(
                adapter_outputs=expected_action_layer_output, nn_outputs=expected_nn_output
            ), decimals=5
        )

        # Logits, parameters (probs) and skip log-probs (numerically unstable for small probs).
        expected_probs_output = sigmoid(expected_action_layer_output)
        test.test(
            ("get_adapter_outputs_and_parameters", states, ["adapter_outputs", "parameters", "log_probs"]),
            expected_outputs=dict(
                adapter_outputs=expected_action_layer_output,
                parameters=expected_probs_output,
                log_probs=np.log(expected_probs_output)
            ), decimals=5
        )

        expected_actions = expected_action_layer_output > 0.0
        test.test(("get_action", states, ["action"]), expected_outputs=dict(action=expected_actions))

        # Get action AND log-llh.
        out = test.test(("get_action_and_log_likelihood", states))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-probs.
        expected_action_log_llh_output = np.log(np.array([
            expected_probs_output[i] if action[i] else 1.0 - expected_probs_output[i] for i in range(batch_size)
        ]))
        test.test(
            ("get_log_likelihood", [states, action], "log_likelihood"),
            expected_outputs=dict(log_likelihood=expected_action_log_llh_output),
            decimals=5
        )
        recursive_assert_almost_equal(expected_action_log_llh_output, llh, decimals=5)

        # Stochastic sample.
        out = test.test(("get_stochastic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.bool_)
        self.assertTrue(out["action"].shape == (batch_size,))

        # Deterministic sample.
        test.test(("get_deterministic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.bool_)
        self.assertTrue(out["action"].shape == (batch_size,))

        # Distribution's entropy.
        out = test.test(("get_entropy", states), expected_outputs=None)
        self.assertTrue(out["entropy"].dtype == np.float32)
        self.assertTrue(out["entropy"].shape == (batch_size,))

    def test_policy_for_discrete_action_space(self):
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        state_space = FloatBox(shape=(4,), add_batch_rank=True)

        # action_space (5 possible actions).
        action_space = IntBox(5, add_batch_rank=True)

        policy = Policy(network_spec=config_from_path("configs/test_simple_nn.json"), action_space=action_space)
        test = ComponentTest(
            component=policy,
            input_spaces=dict(
                nn_inputs=state_space,
                actions=action_space,
            ),
            action_space=action_space
        )
        policy_params = test.read_variable_values(policy.variable_registry)

        # Some NN inputs (4 input nodes, batch size=2).
        states = np.array([[-0.08, 0.4, -0.05, -0.55], [13.0, -14.0, 10.0, -16.0]])
        # Raw NN-output.
        expected_nn_output = np.matmul(
            states, ComponentTest.read_params("policy/test-network/hidden-layer", policy_params)
        )

        test.test(("get_nn_outputs", states), expected_outputs=expected_nn_output, decimals=5)

        # Raw action layer output; Expected shape=(2,5): 2=batch, 5=action categories
        expected_action_layer_output = np.matmul(
            expected_nn_output,
            ComponentTest.read_params("policy/action-adapter-0/action-network/action-layer", policy_params)
        )
        test.test(
            ("get_adapter_outputs", states), expected_outputs=dict(
                adapter_outputs=expected_action_layer_output, nn_outputs=expected_nn_output
            ), decimals=5
        )

        # Logits, parameters (probs) and skip log-probs (numerically unstable for small probs).
        expected_probs_output = softmax(expected_action_layer_output, axis=-1)
        test.test(
            ("get_adapter_outputs_and_parameters", states, ["adapter_outputs", "parameters", "log_probs"]),
            expected_outputs=dict(
                adapter_outputs=expected_action_layer_output,
                parameters=np.array(expected_action_layer_output, dtype=np.float32),
                log_probs=np.log(expected_probs_output)
            ), decimals=5
        )

        expected_actions = np.argmax(expected_action_layer_output, axis=-1)
        test.test(("get_action", states, ["action"]), expected_outputs=dict(action=expected_actions))

        # Get action AND log-llh.
        out = test.test(("get_action_and_log_likelihood", states))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-probs.
        expected_action_log_llh_output = np.log(np.array([
            expected_probs_output[0][action[0]],
            expected_probs_output[1][action[1]]
        ]))
        test.test(
            ("get_log_likelihood", [states, action], "log_likelihood"),
            expected_outputs=dict(log_likelihood=expected_action_log_llh_output),
            decimals=5
        )
        recursive_assert_almost_equal(expected_action_log_llh_output, llh, decimals=5)

        # Stochastic sample.
        out = test.test(("get_stochastic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (2,))

        # Deterministic sample.
        test.test(("get_deterministic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (2,))

        # Distribution's entropy.
        out = test.test(("get_entropy", states), expected_outputs=None)
        self.assertTrue(out["entropy"].dtype == np.float32)
        self.assertTrue(out["entropy"].shape == (2,))

    def test_shared_value_function_policy_for_discrete_action_space(self):
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        state_space = FloatBox(shape=(4,), add_batch_rank=True)

        # action_space (3 possible actions).
        action_space = IntBox(3, add_batch_rank=True)

        # Policy with baseline action adapter.
        shared_value_function_policy = SharedValueFunctionPolicy(
            network_spec=config_from_path("configs/test_lrelu_nn.json"),
            action_space=action_space
        )
        test = ComponentTest(
            component=shared_value_function_policy,
            input_spaces=dict(
                nn_inputs=state_space,
                actions=action_space,
            ),
            action_space=action_space,
        )
        policy_params = test.read_variable_values(shared_value_function_policy.variable_registry)

        # Some NN inputs (4 input nodes, batch size=3).
        states = state_space.sample(size=3)
        # Raw NN-output (3 hidden nodes). All weights=1.5, no biases.
        expected_nn_output = relu(np.matmul(
            states, ComponentTest.read_params("shared-value-function-policy/test-network/hidden-layer", policy_params)
        ), 0.1)

        test.test(("get_nn_outputs", states), expected_outputs=expected_nn_output, decimals=5)

        # Raw action layer output; Expected shape=(3,3): 3=batch, 2=action categories + 1 state value
        expected_action_layer_output = np.matmul(
            expected_nn_output,
            ComponentTest.read_params("shared-value-function-policy/action-adapter-0/action-network/action-layer/",
                                      policy_params)
        )
        test.test(("get_adapter_outputs", states),
                  expected_outputs=dict(adapter_outputs=expected_action_layer_output, nn_outputs=expected_nn_output),
                  decimals=5)

        # State-values: One for each item in the batch.
        expected_state_value_output = np.matmul(
            expected_nn_output,
            ComponentTest.read_params("shared-value-function-policy/value-function-node/dense-layer", policy_params)
        )
        test.test(("get_state_values", states, ["state_values"]),
                  expected_outputs=dict(state_values=expected_state_value_output), decimals=5)

        # Logits-values.
        test.test(("get_state_values_adapter_outputs_and_parameters", states,
                   ["state_values", "adapter_outputs"]),
                  expected_outputs=dict(
                      state_values=expected_state_value_output, adapter_outputs=expected_action_layer_output
                  ),
                  decimals=5)

        # Parameter (probabilities). Softmaxed logits.
        expected_probs_output = softmax(expected_action_layer_output, axis=-1)
        test.test(("get_adapter_outputs_and_parameters", states, ["adapter_outputs", "parameters"]),
                  expected_outputs=dict(
                      adapter_outputs=expected_action_layer_output,
                      parameters=expected_action_layer_output
                  ), decimals=5)

        print("Probs: {}".format(expected_probs_output))

        expected_actions = np.argmax(expected_action_layer_output, axis=-1)
        test.test(("get_action", states, ["action"]), expected_outputs=dict(action=expected_actions))

        # Get action AND log-llh.
        out = test.test(("get_action_and_log_likelihood", states))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-llh.
        expected_action_log_llh_output = np.log(np.array([
            expected_probs_output[0][action[0]],
            expected_probs_output[1][action[1]],
            expected_probs_output[2][action[2]],
        ]))
        test.test(
            ("get_log_likelihood", [states, action], "log_likelihood"),
            expected_outputs=dict(log_likelihood=expected_action_log_llh_output),
            decimals=5
        )
        recursive_assert_almost_equal(expected_action_log_llh_output, llh)

        # Stochastic sample.
        out = test.test(("get_stochastic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (3,))

        # Deterministic sample.
        out = test.test(("get_deterministic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (3,))

        # Distribution's entropy.
        out = test.test(("get_entropy", states), expected_outputs=None)
        self.assertTrue(out["entropy"].dtype == np.float32)
        self.assertTrue(out["entropy"].shape == (3,))

    def test_shared_value_function_policy_for_discrete_action_space_with_time_rank_folding(self):
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        state_space = FloatBox(shape=(3,), add_batch_rank=True, add_time_rank=True)

        # action_space (4 possible actions).
        action_space = IntBox(4, add_batch_rank=True, add_time_rank=True)
        flat_float_action_space = FloatBox(shape=(4,), add_batch_rank=True, add_time_rank=True)

        # Policy with baseline action adapter AND batch-apply over the entire policy (NN + ActionAdapter + distr.).
        network_spec = config_from_path("configs/test_lrelu_nn.json")
        # Add folding and unfolding to network.
        network_spec["fold_time_rank"] = True
        network_spec["unfold_time_rank"] = True
        shared_value_function_policy = SharedValueFunctionPolicy(
            network_spec=network_spec,
            action_adapter_spec=dict(fold_time_rank=True, unfold_time_rank=True),
            action_space=action_space,
            value_fold_time_rank=True,
            value_unfold_time_rank=True
        )
        test = ComponentTest(
            component=shared_value_function_policy,
            input_spaces=dict(
                nn_inputs=state_space,
                actions=action_space,
            ),
            action_space=action_space,
        )
        policy_params = test.read_variable_values(shared_value_function_policy.variable_registry)

        # Some NN inputs.
        states = state_space.sample(size=(2, 3))
        states_folded = np.reshape(states, newshape=(6, 3))
        # Raw NN-output (3 hidden nodes). All weights=1.5, no biases.
        expected_nn_output = np.reshape(relu(np.matmul(
            states_folded,
            ComponentTest.read_params("shared-value-function-policy/test-network/hidden-layer", policy_params)
        ), 0.1), newshape=states.shape)
        test.test(("get_nn_outputs", states), expected_outputs=expected_nn_output, decimals=5)

        # Raw action layer output; Expected shape=(3,3): 3=batch, 2=action categories + 1 state value
        expected_action_layer_output = np.matmul(
            expected_nn_output,
            ComponentTest.read_params("shared-value-function-policy/action-adapter-0/action-network/action-layer/",
                                      policy_params))

        expected_action_layer_output = np.reshape(expected_action_layer_output, newshape=(2, 3, 4))
        test.test(
            ("get_adapter_outputs", states),
            expected_outputs=dict(adapter_outputs=expected_action_layer_output, nn_outputs=expected_nn_output),
            decimals=5
        )

        # State-values: One for each item in the batch.
        expected_state_value_output = np.matmul(
            expected_nn_output,
            ComponentTest.read_params("shared-value-function-policy/value-function-node/dense-layer", policy_params)
        )
        expected_state_value_output_unfolded = np.reshape(expected_state_value_output, newshape=(2, 3, 1))
        test.test(("get_state_values", states, ["state_values"]),
                  expected_outputs=dict(state_values=expected_state_value_output_unfolded),
                  decimals=5)

        expected_action_layer_output_unfolded = np.reshape(expected_action_layer_output, newshape=(2, 3, 4))
        test.test((
            "get_state_values_adapter_outputs_and_parameters", states, ["state_values", "adapter_outputs"]
        ), expected_outputs=dict(
            state_values=expected_state_value_output_unfolded,
            adapter_outputs=expected_action_layer_output_unfolded
        ), decimals=5)

        # Parameter (probabilities). Softmaxed logits.
        expected_probs_output = softmax(expected_action_layer_output_unfolded, axis=-1)
        test.test(
            ("get_adapter_outputs_and_parameters", states, ["adapter_outputs", "parameters", "nn_outputs"]),
            expected_outputs=dict(
                nn_outputs=expected_nn_output,
                adapter_outputs=expected_action_layer_output_unfolded,
                parameters=expected_action_layer_output_unfolded
            ), decimals=5
        )

        print("Probs: {}".format(expected_probs_output))

        expected_actions = np.argmax(expected_action_layer_output_unfolded, axis=-1)
        test.test(("get_action", states, ["action"]), expected_outputs=dict(action=expected_actions))

        out = test.test(("get_action_and_log_likelihood", states))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-llh.
        expected_action_log_llh_output = np.log(np.array([[
            expected_probs_output[0][0][action[0][0]],
            expected_probs_output[0][1][action[0][1]],
            expected_probs_output[0][2][action[0][2]],
        ], [
            expected_probs_output[1][0][action[1][0]],
            expected_probs_output[1][1][action[1][1]],
            expected_probs_output[1][2][action[1][2]],
        ]]))
        test.test(("get_log_likelihood", [states, action]), expected_outputs=dict(
            log_likelihood=expected_action_log_llh_output,
            adapter_outputs=expected_action_layer_output_unfolded
        ), decimals=5)
        recursive_assert_almost_equal(expected_action_log_llh_output, llh, decimals=5)

        # Deterministic sample.
        out = test.test(("get_deterministic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (2, 3))  # Make sure output is unfolded.

        # Stochastic sample.
        out = test.test(("get_stochastic_action", states), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (2, 3))  # Make sure output is unfolded.

        # Distribution's entropy.
        out = test.test(("get_entropy", states), expected_outputs=None)
        self.assertTrue(out["entropy"].dtype == np.float32)
        self.assertTrue(out["entropy"].shape == (2, 3))  # Make sure output is unfolded.

    def test_policy_for_discrete_action_space_with_dueling_layer(self):
        # np.random.seed(10)
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        nn_input_space = FloatBox(shape=(3,), add_batch_rank=True)

        # action_space (2 possible actions).
        action_space = IntBox(2, add_batch_rank=True)
        # flat_float_action_space = FloatBox(shape=(2,), add_batch_rank=True)

        # Policy with dueling logic.
        policy = DuelingPolicy(
            network_spec=config_from_path("configs/test_lrelu_nn.json"),
            action_adapter_spec=dict(
                pre_network_spec=[
                    dict(type="dense", units=10, activation="lrelu", activation_params=[0.1])
                ]
            ),
            units_state_value_stream=10,
            action_space=action_space
        )
        test = ComponentTest(
            component=policy,
            input_spaces=dict(
                nn_inputs=nn_input_space,
                actions=action_space,
            ),
            action_space=action_space
        )
        policy_params = test.read_variable_values(policy.variable_registry)

        # Some NN inputs.
        nn_input = nn_input_space.sample(size=3)
        # Raw NN-output.
        expected_nn_output = relu(np.matmul(
            nn_input,
            ComponentTest.read_params("dueling-policy/test-network/hidden-layer", policy_params)), 0.1
        )
        test.test(("get_nn_outputs", nn_input), expected_outputs=expected_nn_output)

        # Single state values.
        expected_state_values = np.matmul(relu(np.matmul(
            expected_nn_output,
            ComponentTest.read_params("dueling-policy/dense-layer-state-value-stream", policy_params)
        )),
            ComponentTest.read_params("dueling-policy/state-value-node", policy_params))
        test.test(
            ("get_state_values", nn_input, ["state_values", "nn_outputs"]),
            expected_outputs=dict(state_values=expected_state_values, nn_outputs=expected_nn_output),
            decimals=5
        )

        # Raw action layer output.
        expected_raw_advantages = np.matmul(relu(np.matmul(
            expected_nn_output,
            ComponentTest.read_params("dueling-policy/action-adapter-0/action-network/dense-layer", policy_params)
        ), 0.1),
            ComponentTest.read_params("dueling-policy/action-adapter-0/action-network/action-layer", policy_params))

        # Q-values: One for each item in the batch.
        expected_q_values_output = expected_state_values + expected_raw_advantages - \
            np.mean(expected_raw_advantages, axis=-1, keepdims=True)
        test.test(
            ("get_adapter_outputs", nn_input, ["adapter_outputs", "advantages"]),
            expected_outputs=dict(adapter_outputs=expected_q_values_output, advantages=expected_raw_advantages),
            decimals=5
        )

        # Parameter (probabilities). Softmaxed q_values.
        expected_probs_output = softmax(expected_q_values_output, axis=-1)
        test.test(
            ("get_adapter_outputs_and_parameters", nn_input, ["adapter_outputs", "parameters"]),
            expected_outputs=dict(adapter_outputs=expected_q_values_output, parameters=expected_q_values_output),
            decimals=5
        )

        print("Probs: {}".format(expected_probs_output))

        expected_actions = np.argmax(expected_q_values_output, axis=-1)
        test.test(("get_action", nn_input, ["action"]), expected_outputs=dict(action=expected_actions))

        out = test.test(("get_action_and_log_likelihood", nn_input))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-probs.
        expected_action_log_llh_output = np.log(np.array([
            expected_probs_output[0][action[0]],
            expected_probs_output[1][action[1]],
            expected_probs_output[2][action[2]],
        ]))
        test.test(
            ("get_log_likelihood", [nn_input, action]),
            expected_outputs=dict(
                log_likelihood=expected_action_log_llh_output, adapter_outputs=expected_q_values_output
            ),
            decimals=5
        )
        recursive_assert_almost_equal(expected_action_log_llh_output, llh, decimals=5)

        # Stochastic sample.
        out = test.test(("get_stochastic_action", nn_input), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (3,))

        # Deterministic sample.
        out = test.test(("get_deterministic_action", nn_input), expected_outputs=None)
        self.assertTrue(out["action"].dtype == np.int32 or (out["action"].dtype == np.int64))
        self.assertTrue(out["action"].shape == (3,))

        # Distribution's entropy.
        out = test.test(("get_entropy", nn_input), expected_outputs=None)
        self.assertTrue(out["entropy"].dtype == np.float32)
        self.assertTrue(out["entropy"].shape == (3,))

    def test_policy_for_bounded_continuous_action_space_using_beta(self):
        """
        https://github.com/rlgraph/rlgraph/issues/43
        """
        nn_input_space = FloatBox(shape=(4,), add_batch_rank=True)
        action_space = FloatBox(low=-1.0, high=1.0, shape=(1,), add_batch_rank=True)
        # Double the shape for alpha/beta params.
        # action_space_parameters = Tuple(FloatBox(shape=(1,)), FloatBox(shape=(1,)), add_batch_rank=True)

        policy = Policy(network_spec=config_from_path("configs/test_simple_nn.json"), action_space=action_space)
        test = ComponentTest(
            component=policy,
            input_spaces=dict(
                nn_inputs=nn_input_space,
                actions=action_space,
            ),
            action_space=action_space
        )

        policy_params = test.read_variable_values(policy.variable_registry)

        # Some NN inputs.
        nn_input = nn_input_space.sample(size=3)
        # Raw NN-output.
        expected_nn_output = np.matmul(nn_input,
                                       ComponentTest.read_params("policy/test-network/hidden-layer", policy_params))
        test.test(("get_nn_outputs", nn_input), expected_outputs=expected_nn_output)

        # Raw action layer output.
        expected_raw_logits = np.matmul(
            expected_nn_output,
            ComponentTest.read_params("policy/action-adapter-0/action-network/action-layer", policy_params)
        )
        test.test(
            ("get_adapter_outputs", nn_input),
            expected_outputs=dict(adapter_outputs=expected_raw_logits, nn_outputs=expected_nn_output),
            decimals=5
        )

        # Parameter (alpha/betas).
        expected_alpha_parameters = np.log(np.exp(expected_raw_logits[:, 0:1]) + 1.0) + 1.0
        expected_beta_parameters = np.log(np.exp(expected_raw_logits[:, 1:]) + 1.0) + 1.0
        expected_parameters = tuple([expected_alpha_parameters, expected_beta_parameters])
        test.test(
            ("get_adapter_outputs_and_parameters", nn_input, ["adapter_outputs", "parameters"]),
            expected_outputs=dict(adapter_outputs=expected_raw_logits, parameters=expected_parameters),
            decimals=5
        )

        print("Params: {}".format(expected_parameters))

        action = test.test(("get_action", nn_input))["action"]
        self.assertTrue(action.dtype == np.float32)
        self.assertGreaterEqual(action.min(), -1.0)
        self.assertLessEqual(action.max(), 1.0)
        self.assertTrue(action.shape == (3, 1))

        out = test.test(("get_action_and_log_likelihood", nn_input))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-probs.
        actions_scaled_back = (action + 1.0) / 2.0
        expected_action_log_llh_output = np.log(
            beta.pdf(actions_scaled_back, expected_alpha_parameters, expected_beta_parameters)
        )
        # expected_action_log_prob_output = np.array([[expected_action_log_prob_output[0][0]],
        # [expected_action_log_prob_output[1][1]], [expected_action_log_prob_output[2][2]]])
        test.test(
            ("get_log_likelihood", [nn_input, action], "log_likelihood"),
            expected_outputs=dict(log_likelihood=expected_action_log_llh_output),
            decimals=5
        )
        recursive_assert_almost_equal(expected_action_log_llh_output, llh, decimals=5)

        # Stochastic sample.
        actions = test.test(("get_stochastic_action", nn_input))["action"]
        self.assertTrue(actions.dtype == np.float32)
        self.assertGreaterEqual(actions.min(), -1.0)
        self.assertLessEqual(actions.max(), 1.0)
        self.assertTrue(actions.shape == (3, 1))

        # Deterministic sample.
        actions = test.test(("get_deterministic_action", nn_input))["action"]
        self.assertTrue(actions.dtype == np.float32)
        self.assertGreaterEqual(actions.min(), -1.0)
        self.assertLessEqual(actions.max(), 1.0)
        self.assertTrue(actions.shape == (3, 1))

        # Distribution's entropy.
        entropy = test.test(("get_entropy", nn_input))["entropy"]
        self.assertTrue(entropy.dtype == np.float32)
        self.assertTrue(entropy.shape == (3, 1))

    def test_policy_for_bounded_continuous_action_space_using_squashed_normal(self):
        """
        Same test case, but with different bounded continuous distribution (squashed normal).
        """
        nn_input_space = FloatBox(shape=(4,), add_batch_rank=True)
        action_space = FloatBox(low=-2.0, high=1.0, shape=(1,), add_batch_rank=True)

        policy = Policy(network_spec=config_from_path("configs/test_simple_nn.json"), action_space=action_space,
                        distributions_spec=dict(bounded_distribution_type="squashed-normal"))
        test = ComponentTest(
            component=policy,
            input_spaces=dict(
                nn_inputs=nn_input_space,
                actions=action_space,
            ),
            action_space=action_space
        )

        policy_params = test.read_variable_values(policy.variable_registry)

        # Some NN inputs.
        nn_input = nn_input_space.sample(size=3)
        # Raw NN-output.
        expected_nn_output = np.matmul(
            nn_input, ComponentTest.read_params("policy/test-network/hidden-layer", policy_params)
        )
        test.test(("get_nn_outputs", nn_input), expected_outputs=expected_nn_output)

        # Raw action layer output.
        expected_raw_logits = np.matmul(
            expected_nn_output,
            ComponentTest.read_params("policy/action-adapter-0/action-network/action-layer", policy_params)
        )
        test.test(
            ("get_adapter_outputs", nn_input),
            expected_outputs=dict(adapter_outputs=expected_raw_logits, nn_outputs=expected_nn_output),
            decimals=5
        )

        # Parameter (mean/stddev).
        expected_mean_parameters = expected_raw_logits[:, 0:1]
        expected_log_stddev_parameters = np.clip(expected_raw_logits[:, 1:2], MIN_LOG_STDDEV, MAX_LOG_STDDEV)
        expected_parameters = tuple([expected_mean_parameters, np.exp(expected_log_stddev_parameters)])
        test.test(
            ("get_adapter_outputs_and_parameters", nn_input, ["adapter_outputs", "parameters"]),
            expected_outputs=dict(adapter_outputs=expected_raw_logits, parameters=expected_parameters),
            decimals=5
        )

        print("Params: {}".format(expected_parameters))

        action = test.test(("get_action", nn_input))["action"]
        self.assertTrue(action.dtype == np.float32)
        self.assertGreaterEqual(action.min(), -2.0)
        self.assertLessEqual(action.max(), 1.0)
        self.assertTrue(action.shape == (3, 1))

        out = test.test(("get_action_and_log_likelihood", nn_input))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-probs.
        actions_tanh_d = (action + 2.0) / 3.0 * 2.0 - 1.0
        actions_unsquashed = np.arctanh(actions_tanh_d)
        expected_action_log_llh_output = np.log(
            norm.pdf(actions_unsquashed, loc=expected_parameters[0], scale=expected_parameters[1])
        )
        expected_action_log_llh_output -= np.sum(np.log(1 - actions_tanh_d ** 2 + SMALL_NUMBER), axis=-1, keepdims=True)
        # expected_action_log_prob_output = np.array([[expected_action_log_prob_output[0][0]],
        # [expected_action_log_prob_output[1][1]], [expected_action_log_prob_output[2][2]]])
        test.test(
            ("get_log_likelihood", [nn_input, action], "log_likelihood"),
            expected_outputs=dict(log_likelihood=expected_action_log_llh_output),
            decimals=5
        )
        recursive_assert_almost_equal(expected_action_log_llh_output, llh, decimals=5)

        # Stochastic sample.
        actions = test.test(("get_stochastic_action", nn_input))["action"]
        self.assertTrue(actions.dtype == np.float32)
        self.assertGreaterEqual(actions.min(), -2.0)
        self.assertLessEqual(actions.max(), 1.0)
        self.assertTrue(actions.shape == (3, 1))

        # Deterministic sample.
        actions = test.test(("get_deterministic_action", nn_input))["action"]
        self.assertTrue(actions.dtype == np.float32)
        self.assertGreaterEqual(actions.min(), -2.0)
        self.assertLessEqual(actions.max(), 1.0)
        self.assertTrue(actions.shape == (3, 1))

        # Distribution's entropy.
        entropy = test.test(("get_entropy", nn_input))["entropy"]
        self.assertTrue(entropy.dtype == np.float32)
        self.assertTrue(entropy.shape == (3, 1))
