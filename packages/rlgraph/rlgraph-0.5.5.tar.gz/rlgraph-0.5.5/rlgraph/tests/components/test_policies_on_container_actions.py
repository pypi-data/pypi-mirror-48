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
from rlgraph.utils import sigmoid, softmax, relu, SMALL_NUMBER


class TestPoliciesOnContainerActions(unittest.TestCase):

    def test_policy_for_discrete_container_action_space(self):
        # state_space.
        state_space = FloatBox(shape=(4,), add_batch_rank=True)

        # Container action space.
        action_space = dict(
            type="dict",
            a=BoolBox(),
            b=IntBox(3),
            add_batch_rank=True
        )

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

        # Some NN inputs (batch size=32).
        batch_size = 32
        states = state_space.sample(batch_size)
        # Raw NN-output.
        expected_nn_output = np.matmul(states, policy_params["policy/test-network/hidden-layer/dense/kernel"])
        test.test(("get_nn_outputs", states), expected_outputs=expected_nn_output, decimals=6)

        # Raw action layers' output.
        expected_action_layer_outputs = dict(
            a=np.squeeze(np.matmul(expected_nn_output, policy_params["policy/action-adapter-0/action-network/action-layer/dense/kernel"])),
            b=np.matmul(expected_nn_output, policy_params["policy/action-adapter-1/action-network/action-layer/dense/kernel"])
        )
        test.test(
            ("get_adapter_outputs", states),
            expected_outputs=dict(adapter_outputs=expected_action_layer_outputs, nn_outputs=expected_nn_output),
            decimals=5
        )

        # Logits, parameters (probs) and skip log-probs (numerically unstable for small probs).
        expected_probs_output = dict(
            a=np.array(sigmoid(expected_action_layer_outputs["a"]), dtype=np.float32),
            b=np.array(softmax(expected_action_layer_outputs["b"], axis=-1), dtype=np.float32)
        )
        test.test(
            ("get_adapter_outputs_and_parameters", states, ["adapter_outputs", "parameters"]),
            expected_outputs=dict(
                adapter_outputs=expected_action_layer_outputs,
                parameters=dict(a=expected_probs_output["a"], b=expected_action_layer_outputs["b"])
            ), decimals=5
        )

        print("Probs: {}".format(expected_probs_output))

        expected_actions = dict(
            a=expected_probs_output["a"] > 0.5,
            b=np.argmax(expected_action_layer_outputs["b"], axis=-1)
        )
        test.test(("get_action", states, ["action"]), expected_outputs=dict(action=expected_actions))

        out = test.test(("get_action_and_log_likelihood", states))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-likelihood (sum of the composite llhs).
        expected_action_llh_output = \
            np.log(np.array([expected_probs_output["a"][i] if action["a"][i] else 1.0 - expected_probs_output["a"][i] for i in range(batch_size)])) + \
            np.log(np.array([expected_probs_output["b"][i][action["b"][i]] for i in range(batch_size)]))
        test.test(
            ("get_log_likelihood", [states, action]), expected_outputs=dict(
                log_likelihood=expected_action_llh_output, adapter_outputs=expected_action_layer_outputs
            ), decimals=5
        )
        recursive_assert_almost_equal(expected_action_llh_output, llh, decimals=5)

        # Stochastic sample.
        out = test.test(("get_stochastic_action", states), expected_outputs=None)  # dict(action=expected_actions))
        self.assertTrue(out["action"]["a"].dtype == np.bool_)
        self.assertTrue(out["action"]["a"].shape == (batch_size,))
        self.assertTrue(out["action"]["b"].dtype == np.int32)
        self.assertTrue(out["action"]["b"].shape == (batch_size,))

        # Deterministic sample.
        test.test(("get_deterministic_action", states), expected_outputs=None)  # dict(action=expected_actions))
        self.assertTrue(out["action"]["a"].dtype == np.bool_)
        self.assertTrue(out["action"]["a"].shape == (batch_size,))
        self.assertTrue(out["action"]["b"].dtype == np.int32)
        self.assertTrue(out["action"]["b"].shape == (batch_size,))

        # Distribution's entropy.
        out = test.test(("get_entropy", states), expected_outputs=None)  # dict(entropy=expected_h), decimals=3)
        self.assertTrue(out["entropy"]["a"].dtype == np.float32)
        self.assertTrue(out["entropy"]["a"].shape == (batch_size,))
        self.assertTrue(out["entropy"]["b"].dtype == np.float32)
        self.assertTrue(out["entropy"]["b"].shape == (batch_size,))

    def test_shared_value_function_policy_for_discrete_container_action_space(self):
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        state_space = FloatBox(shape=(5,), add_batch_rank=True)

        # action_space (complex nested container action space).
        action_space = dict(
            type="dict",
            a=IntBox(2),
            b=Dict(b1=IntBox(3), b2=IntBox(4)),
            add_batch_rank=True
        )
        #flat_float_action_space = dict(
        #    type="dict",
        #    a=FloatBox(shape=(2,)),
        #    b=Dict(b1=FloatBox(shape=(3,)), b2=FloatBox(shape=(4,))),
        #    add_batch_rank=True
        #)

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

        base_scope = "shared-value-function-policy/action-adapter-"

        # Some NN inputs (batch size=2).
        states = state_space.sample(size=2)
        # Raw NN-output.
        expected_nn_output = relu(np.matmul(
            states, policy_params["shared-value-function-policy/test-network/hidden-layer/dense/kernel"]
        ), 0.1)
        test.test(("get_nn_outputs", states), expected_outputs=expected_nn_output, decimals=5)

        # Raw action layers' output.
        expected_action_layer_outputs = dict(
            a=np.matmul(expected_nn_output, policy_params[base_scope + "0/action-network/action-layer/dense/kernel"]),
            b=dict(b1=np.matmul(expected_nn_output, policy_params[base_scope + "1/action-network/action-layer/dense/kernel"]),
                   b2=np.matmul(expected_nn_output, policy_params[base_scope + "2/action-network/action-layer/dense/kernel"]))
        )
        test.test(
            ("get_adapter_outputs", states),
            expected_outputs=dict(adapter_outputs=expected_action_layer_outputs, nn_outputs=expected_nn_output),
                decimals=5
        )

        # State-values.
        expected_state_value_output = np.matmul(
            expected_nn_output, policy_params["shared-value-function-policy/value-function-node/dense-layer/dense/kernel"]
        )
        test.test(
            ("get_state_values", states, ["state_values"]),
            expected_outputs=dict(state_values=expected_state_value_output),
            decimals=5
        )

        # logits-values: One for each action-choice per item in the batch (simply take the remaining out nodes).
        test.test(
            ("get_state_values_adapter_outputs_and_parameters", states, ["state_values", "adapter_outputs"]),
            expected_outputs=dict(
                state_values=expected_state_value_output, adapter_outputs=expected_action_layer_outputs
            ),
            decimals=5
        )

        # Parameter (probabilities). Softmaxed logits.
        expected_probs_output = dict(
            a=softmax(expected_action_layer_outputs["a"], axis=-1),
            b=dict(
                b1=softmax(expected_action_layer_outputs["b"]["b1"], axis=-1),
                b2=softmax(expected_action_layer_outputs["b"]["b2"], axis=-1)
            )
        )
        test.test(("get_adapter_outputs_and_parameters", states, ["adapter_outputs", "parameters"]), expected_outputs=dict(
            adapter_outputs=expected_action_layer_outputs,
            parameters=expected_action_layer_outputs
        ), decimals=5)

        print("Probs: {}".format(expected_probs_output))

        # Action sample.
        expected_actions = dict(
            a=np.argmax(expected_action_layer_outputs["a"], axis=-1),
            b=dict(
                b1=np.argmax(expected_action_layer_outputs["b"]["b1"], axis=-1),
                b2=np.argmax(expected_action_layer_outputs["b"]["b2"], axis=-1)
            )
        )
        test.test(("get_action", states, ["action"]), expected_outputs=dict(action=expected_actions))

        out = test.test(("get_action_and_log_likelihood", states))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-likelihood.
        expected_action_llh_output = np.log(np.array([expected_probs_output["a"][0][action["a"][0]],
                                                      expected_probs_output["a"][1][action["a"][1]]])) + \
                                     np.log(np.array([expected_probs_output["b"]["b1"][0][action["b"]["b1"][0]],
                                                      expected_probs_output["b"]["b1"][1][action["b"]["b1"][1]]
                                                      ])
                                            ) + \
                                     np.log(np.array([expected_probs_output["b"]["b2"][0][action["b"]["b2"][0]],
                                                      expected_probs_output["b"]["b2"][1][action["b"]["b2"][1]],
                                                      ])
                                            )
        test.test(
            ("get_log_likelihood", [states, action]), expected_outputs=dict(
                log_likelihood=expected_action_llh_output, adapter_outputs=expected_action_layer_outputs
            ), decimals=5
        )
        recursive_assert_almost_equal(expected_action_llh_output, llh, decimals=5)

        # Stochastic sample.
        out = test.test(("get_stochastic_action", states), expected_outputs=None)["action"]
        self.assertTrue(out["a"].dtype == np.int32)
        self.assertTrue(out["a"].shape == (2,))
        self.assertTrue(out["b"]["b1"].dtype == np.int32)
        self.assertTrue(out["b"]["b1"].shape == (2,))
        self.assertTrue(out["b"]["b2"].dtype == np.int32)
        self.assertTrue(out["b"]["b2"].shape == (2,))

        # Deterministic sample.
        out = test.test(("get_deterministic_action", states), expected_outputs=None)["action"]
        self.assertTrue(out["a"].dtype == np.int32)
        self.assertTrue(out["a"].shape == (2,))
        self.assertTrue(out["b"]["b1"].dtype == np.int32)
        self.assertTrue(out["b"]["b1"].shape == (2,))
        self.assertTrue(out["b"]["b2"].dtype == np.int32)
        self.assertTrue(out["b"]["b2"].shape == (2,))

        # Distribution's entropy.
        out = test.test(("get_entropy", states), expected_outputs=None)["entropy"]
        self.assertTrue(out["a"].dtype == np.float32)
        self.assertTrue(out["a"].shape == (2,))
        self.assertTrue(out["b"]["b1"].dtype == np.float32)
        self.assertTrue(out["b"]["b1"].shape == (2,))
        self.assertTrue(out["b"]["b2"].dtype == np.float32)
        self.assertTrue(out["b"]["b2"].shape == (2,))

    def test_shared_value_function_policy_for_discrete_container_action_space_with_time_rank_folding(self):
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        state_space = FloatBox(shape=(6,), add_batch_rank=True, add_time_rank=True)

        # Action_space.
        action_space = Tuple(
            IntBox(2),
            IntBox(3),
            Dict(
                a=IntBox(4),
            ),
            add_batch_rank=True,
            add_time_rank=True
        )
        #flat_float_action_space = Tuple(
        #    FloatBox(shape=(2,)),
        #    FloatBox(shape=(3,)),
        #    Dict(
        #        a=FloatBox(shape=(4,)),
        #    ),
        #    add_batch_rank=True,
        #    add_time_rank=True
        #)

        # Policy with baseline action adapter AND batch-apply over the entire policy (NN + ActionAdapter + distr.).
        network_spec = config_from_path("configs/test_lrelu_nn.json")
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
        base_scope = "shared-value-function-policy/action-adapter-"

        # Some NN inputs.
        states = state_space.sample(size=(2, 3))
        states_folded = np.reshape(states, newshape=(6, 6))
        # Raw NN-output (still folded).
        expected_nn_output = np.reshape(relu(np.matmul(
            states_folded, policy_params["shared-value-function-policy/test-network/hidden-layer/dense/kernel"]
        ), 0.1), newshape=(2, 3, 3))
        test.test(("get_nn_outputs", states), expected_outputs=expected_nn_output, decimals=5)

        # Raw action layer output; Expected shape=(3,3): 3=batch, 2=action categories + 1 state value
        expected_action_layer_output = tuple([
            np.matmul(expected_nn_output, policy_params[base_scope + "0/action-network/action-layer/dense/kernel"]),
            np.matmul(expected_nn_output, policy_params[base_scope + "1/action-network/action-layer/dense/kernel"]),
            dict(
                a=np.matmul(expected_nn_output, policy_params[base_scope + "2/action-network/action-layer/dense/kernel"])
            )
        ])
        expected_action_layer_output_unfolded = tuple([
            np.reshape(expected_action_layer_output[0], newshape=(2, 3, 2)),
            np.reshape(expected_action_layer_output[1], newshape=(2, 3, 3)),
            dict(
                a=np.reshape(expected_action_layer_output[2]["a"], newshape=(2, 3, 4))
            )
        ])
        test.test(
            ("get_adapter_outputs", states),
            expected_outputs=dict(adapter_outputs=expected_action_layer_output_unfolded, nn_outputs=expected_nn_output),
            decimals=5
        )

        # State-values: One for each item in the batch.
        expected_state_value_output = np.matmul(
            expected_nn_output,
            policy_params["shared-value-function-policy/value-function-node/dense-layer/dense/kernel"]
        )
        expected_state_value_output_unfolded = np.reshape(expected_state_value_output, newshape=(2, 3, 1))
        test.test(
            ("get_state_values", states, ["state_values"]),
            expected_outputs=dict(state_values=expected_state_value_output_unfolded),
            decimals=5
        )

        test.test(
            ("get_state_values_adapter_outputs_and_parameters", states, ["state_values", "adapter_outputs"]),
            expected_outputs=dict(
                state_values=expected_state_value_output_unfolded, adapter_outputs=expected_action_layer_output_unfolded
            ),
            decimals=5
        )

        # Parameter (probabilities). Softmaxed logits.
        expected_probs_output = tuple([
            softmax(expected_action_layer_output_unfolded[0], axis=-1),
            softmax(expected_action_layer_output_unfolded[1], axis=-1),
            dict(
                a=softmax(expected_action_layer_output_unfolded[2]["a"], axis=-1)
            )
        ])
        test.test(
            ("get_adapter_outputs_and_parameters", states, ["adapter_outputs", "parameters"]),
            expected_outputs=dict(
                adapter_outputs=expected_action_layer_output_unfolded, parameters=expected_action_layer_output_unfolded
            ),
            decimals=5
        )

        print("Probs: {}".format(expected_probs_output))

        expected_actions = tuple([
            np.argmax(expected_action_layer_output_unfolded[0], axis=-1),
            np.argmax(expected_action_layer_output_unfolded[1], axis=-1),
            dict(
                a=np.argmax(expected_action_layer_output_unfolded[2]["a"], axis=-1),
            )
        ])
        test.test(("get_action", states, ["action"]), expected_outputs=dict(action=expected_actions))

        out = test.test(("get_action_and_log_likelihood", states))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-likelihood.
        expected_action_llh_output = np.log(np.array([[
            expected_probs_output[0][0][0][action[0][0][0]],
            expected_probs_output[0][0][1][action[0][0][1]],
            expected_probs_output[0][0][2][action[0][0][2]],
        ], [
            expected_probs_output[0][1][0][action[0][1][0]],
            expected_probs_output[0][1][1][action[0][1][1]],
            expected_probs_output[0][1][2][action[0][1][2]],
        ]])) + np.log(np.array([[
            expected_probs_output[1][0][0][action[1][0][0]],
            expected_probs_output[1][0][1][action[1][0][1]],
            expected_probs_output[1][0][2][action[1][0][2]],
        ], [
            expected_probs_output[1][1][0][action[1][1][0]],
            expected_probs_output[1][1][1][action[1][1][1]],
            expected_probs_output[1][1][2][action[1][1][2]],
        ]])) + np.log(np.array([[
            expected_probs_output[2]["a"][0][0][action[2]["a"][0][0]],
            expected_probs_output[2]["a"][0][1][action[2]["a"][0][1]],
            expected_probs_output[2]["a"][0][2][action[2]["a"][0][2]],
        ], [
            expected_probs_output[2]["a"][1][0][action[2]["a"][1][0]],
            expected_probs_output[2]["a"][1][1][action[2]["a"][1][1]],
            expected_probs_output[2]["a"][1][2][action[2]["a"][1][2]],
        ]]))
        test.test(
            ("get_log_likelihood", [states, action]), expected_outputs=dict(
                log_likelihood=expected_action_llh_output, adapter_outputs=expected_action_layer_output_unfolded
            ), decimals=5
        )
        recursive_assert_almost_equal(expected_action_llh_output, llh, decimals=5)

        # Deterministic sample.
        out = test.test(("get_deterministic_action", states), expected_outputs=None)
        self.assertTrue(out["action"][0].dtype == np.int32)
        self.assertTrue(out["action"][0].shape == (2, 3))  # Make sure output is unfolded.
        self.assertTrue(out["action"][1].dtype == np.int32)
        self.assertTrue(out["action"][1].shape == (2, 3))  # Make sure output is unfolded.
        self.assertTrue(out["action"][2]["a"].dtype == np.int32)
        self.assertTrue(out["action"][2]["a"].shape == (2, 3))  # Make sure output is unfolded.

        # Stochastic sample.
        out = test.test(("get_stochastic_action", states), expected_outputs=None)
        self.assertTrue(out["action"][0].dtype == np.int32)
        self.assertTrue(out["action"][0].shape == (2, 3))  # Make sure output is unfolded.
        self.assertTrue(out["action"][1].dtype == np.int32)
        self.assertTrue(out["action"][1].shape == (2, 3))  # Make sure output is unfolded.
        self.assertTrue(out["action"][2]["a"].dtype == np.int32)
        self.assertTrue(out["action"][2]["a"].shape == (2, 3))  # Make sure output is unfolded.

        # Distribution's entropy.
        out = test.test(("get_entropy", states), expected_outputs=None)
        self.assertTrue(out["entropy"][0].dtype == np.float32)
        self.assertTrue(out["entropy"][0].shape == (2, 3))  # Make sure output is unfolded.
        self.assertTrue(out["entropy"][1].dtype == np.float32)
        self.assertTrue(out["entropy"][1].shape == (2, 3))  # Make sure output is unfolded.
        self.assertTrue(out["entropy"][2]["a"].dtype == np.float32)
        self.assertTrue(out["entropy"][2]["a"].shape == (2, 3))  # Make sure output is unfolded.

    def test_policy_for_discrete_action_space_with_dueling_layer(self):
        # state_space (NN is a simple single fc-layer relu network (2 units), random biases, random weights).
        nn_input_space = FloatBox(shape=(5,), add_batch_rank=True)

        # Action space.
        action_space = Dict(dict(
            a=Tuple(IntBox(2), IntBox(3)),
            b=Dict(dict(ba=IntBox(4)))
        ), add_batch_rank=True)
        #flat_float_action_space = Dict(dict(
        #    a=Tuple(FloatBox(shape=(2,)), FloatBox(shape=(3,))),
        #    b=Dict(dict(ba=FloatBox(shape=(4,))))
        #), add_batch_rank=True)

        # Policy with dueling logic.
        policy = DuelingPolicy(
            network_spec=config_from_path("configs/test_lrelu_nn.json"),
            # Make all sub action adapters the same.
            action_adapter_spec=dict(
                pre_network_spec=[
                    dict(type="dense", units=5, activation="lrelu", activation_params=[0.2])
                ]
            ),
            units_state_value_stream=2,
            action_space=action_space
        )
        test = ComponentTest(
            component=policy,
            input_spaces=dict(
                nn_inputs=nn_input_space,
                actions=action_space,
                #logits=flat_float_action_space,
                #parameters=flat_float_action_space
            ),
            action_space=action_space
        )
        policy_params = test.read_variable_values(policy.variable_registry)

        # Some NN inputs.
        nn_input = nn_input_space.sample(size=3)
        # Raw NN-output.
        expected_nn_output = relu(np.matmul(
            nn_input, policy_params["dueling-policy/test-network/hidden-layer/dense/kernel"]), 0.2
        )
        test.test(("get_nn_outputs", nn_input), expected_outputs=expected_nn_output, decimals=5)

        # Raw action layer output.
        expected_raw_advantages = dict(
            a=(
                np.matmul(
                    relu(np.matmul(
                        expected_nn_output,
                        policy_params["dueling-policy/action-adapter-0/action-network/dense-layer/dense/kernel"]
                    ), 0.2), policy_params["dueling-policy/action-adapter-0/action-network/action-layer/dense/kernel"]
                ),
                np.matmul(
                    relu(np.matmul(
                        expected_nn_output,
                        policy_params["dueling-policy/action-adapter-1/action-network/dense-layer/dense/kernel"]
                    ), 0.2), policy_params["dueling-policy/action-adapter-1/action-network/action-layer/dense/kernel"]
                ),
            ),
            b=dict(ba=np.matmul(
                relu(np.matmul(
                    expected_nn_output,
                    policy_params["dueling-policy/action-adapter-2/action-network/dense-layer/dense/kernel"]
                ), 0.2), policy_params["dueling-policy/action-adapter-2/action-network/action-layer/dense/kernel"]
            ))
        )

        # Single state values.
        expected_state_values = np.matmul(relu(np.matmul(
            expected_nn_output,
            policy_params["dueling-policy/dense-layer-state-value-stream/dense/kernel"]
        )), policy_params["dueling-policy/state-value-node/dense/kernel"])
        test.test(
            ("get_state_values", nn_input, ["state_values"]),
            expected_outputs=dict(state_values=expected_state_values),
            decimals=5
        )

        # State-values: One for each item in the batch.
        expected_q_values_output = dict(
            a=(
                expected_state_values + expected_raw_advantages["a"][0] - np.mean(expected_raw_advantages["a"][0],
                                                                                  axis=-1, keepdims=True),
                expected_state_values + expected_raw_advantages["a"][1] - np.mean(expected_raw_advantages["a"][1],
                                                                                  axis=-1, keepdims=True),
            ),
            b=dict(ba=expected_state_values + expected_raw_advantages["b"]["ba"] - np.mean(
                expected_raw_advantages["b"]["ba"], axis=-1, keepdims=True))
        )
        test.test(
            ("get_adapter_outputs", nn_input),
            expected_outputs=dict(
                adapter_outputs=expected_q_values_output, nn_outputs=expected_nn_output,
                advantages=expected_raw_advantages, q_values=expected_q_values_output
            ),
            decimals=5
        )

        test.test(
            ("get_adapter_outputs_and_parameters", nn_input, ["adapter_outputs"]),
            expected_outputs=dict(adapter_outputs=expected_q_values_output),
            decimals=5
        )

        # Parameter (probabilities). Softmaxed q_values.
        expected_probs_output = dict(
            a=(
                softmax(expected_q_values_output["a"][0], axis=-1),
                softmax(expected_q_values_output["a"][1], axis=-1)
            ),
            b=dict(ba=np.maximum(softmax(expected_q_values_output["b"]["ba"], axis=-1), SMALL_NUMBER))
        )
        expected_log_probs_output = dict(
            a=(np.log(expected_probs_output["a"][0]),
               np.log(expected_probs_output["a"][1])),
            b=dict(ba=np.log(expected_probs_output["b"]["ba"]))
        )
        test.test(
            ("get_adapter_outputs_and_parameters", nn_input, ["adapter_outputs", "parameters", "log_probs"]),
            expected_outputs=dict(
                adapter_outputs=expected_q_values_output, parameters=expected_q_values_output,
                log_probs=expected_log_probs_output
            ),
            decimals=5
        )

        print("Probs: {}".format(expected_probs_output))

        expected_actions = dict(
            a=(np.argmax(expected_q_values_output["a"][0], axis=-1),
               np.argmax(expected_q_values_output["a"][1], axis=-1)),
            b=dict(ba=np.argmax(expected_q_values_output["b"]["ba"], axis=-1))
        )
        test.test(("get_action", nn_input, ["action"]), expected_outputs=dict(action=expected_actions))

        out = test.test(("get_action_and_log_likelihood", nn_input))
        action = out["action"]
        llh = out["log_likelihood"]

        # Action log-likelihood.
        expected_action_llh_output = np.array([
            expected_log_probs_output["a"][0][0][action["a"][0][0]],
            expected_log_probs_output["a"][0][1][action["a"][0][1]],
            expected_log_probs_output["a"][0][2][action["a"][0][2]],
        ]) + np.array([
            expected_log_probs_output["a"][1][0][action["a"][1][0]],
            expected_log_probs_output["a"][1][1][action["a"][1][1]],
            expected_log_probs_output["a"][1][2][action["a"][1][2]],
        ]) + np.array([
            expected_log_probs_output["b"]["ba"][0][action["b"]["ba"][0]],
            expected_log_probs_output["b"]["ba"][1][action["b"]["ba"][1]],
            expected_log_probs_output["b"]["ba"][2][action["b"]["ba"][2]],
        ])
        test.test(
            ("get_log_likelihood", [nn_input, action]), expected_outputs=dict(
                log_likelihood=expected_action_llh_output, adapter_outputs=expected_q_values_output
            ), decimals=5
        )
        recursive_assert_almost_equal(expected_action_llh_output, llh, decimals=5)

        # Stochastic sample.
        out = test.test(("get_stochastic_action", nn_input), expected_outputs=None)
        self.assertTrue(out["action"]["a"][0].dtype == np.int32)
        self.assertTrue(out["action"]["a"][0].shape == (3,))
        self.assertTrue(out["action"]["a"][1].dtype == np.int32)
        self.assertTrue(out["action"]["a"][1].shape == (3,))
        self.assertTrue(out["action"]["b"]["ba"].dtype == np.int32)
        self.assertTrue(out["action"]["b"]["ba"].shape == (3,))

        # Deterministic sample.
        out = test.test(("get_deterministic_action", nn_input), expected_outputs=None)
        self.assertTrue(out["action"]["a"][0].dtype == np.int32)
        self.assertTrue(out["action"]["a"][0].shape == (3,))
        self.assertTrue(out["action"]["a"][1].dtype == np.int32)
        self.assertTrue(out["action"]["a"][1].shape == (3,))
        self.assertTrue(out["action"]["b"]["ba"].dtype == np.int32)
        self.assertTrue(out["action"]["b"]["ba"].shape == (3,))

        # Distribution's entropy.
        out = test.test(("get_entropy", nn_input), expected_outputs=None)
        self.assertTrue(out["entropy"]["a"][0].dtype == np.float32)
        self.assertTrue(out["entropy"]["a"][0].shape == (3,))
        self.assertTrue(out["entropy"]["a"][1].dtype == np.float32)
        self.assertTrue(out["entropy"]["a"][1].shape == (3,))
        self.assertTrue(out["entropy"]["b"]["ba"].dtype == np.float32)
        self.assertTrue(out["entropy"]["b"]["ba"].shape == (3,))
