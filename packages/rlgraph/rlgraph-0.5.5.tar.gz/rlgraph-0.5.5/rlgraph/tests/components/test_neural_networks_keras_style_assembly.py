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
from rlgraph.components.layers.nn import DenseLayer, LSTMLayer, ConcatLayer, Conv2DLayer
from rlgraph.components.layers.preprocessing.reshape import ReShape
from rlgraph.components.layers.strings import StringToHashBucket, EmbeddingLookup
from rlgraph.components.neural_networks import NeuralNetwork
from rlgraph.spaces import FloatBox, TextBox, IntBox, Tuple, Dict
from rlgraph.tests.component_test import ComponentTest
from rlgraph.utils.numpy import dense_layer, relu, lstm_layer, one_hot


class TestNeuralNetworkKerasStyleAssembly(unittest.TestCase):
    """
    Tests for assembling from json and running different NeuralNetworks.
    """
    def test_keras_style_simple_nn(self):
        # Input Space of the network.
        input_space = FloatBox(shape=(3,), add_batch_rank=True)

        # Create a DenseLayer with a fixed `call` method input space for the arg `inputs`.
        output1 = DenseLayer(units=5, activation="linear", scope="a")(input_space)
        # Create a DenseLayer whose `inputs` arg is the resulting DataOpRec of output1's `call` output.
        output2 = DenseLayer(units=7, activation="relu", scope="b")(output1)

        # This will trace back automatically through the given output DataOpRec(s) and add all components
        # on the way to the input-space to this network.
        neural_net = NeuralNetwork(outputs=output2)

        test = ComponentTest(component=neural_net, input_spaces=dict(inputs=input_space))

        # Batch of size=n.
        input_ = input_space.sample(5)
        # Calculate output manually.
        var_dict = neural_net.get_variables("a/dense/kernel", "a/dense/bias", "b/dense/kernel", "b/dense/bias", global_scope=False)
        w1_value = test.read_variable_values(var_dict["a/dense/kernel"])
        b1_value = test.read_variable_values(var_dict["a/dense/bias"])
        w2_value = test.read_variable_values(var_dict["b/dense/kernel"])
        b2_value = test.read_variable_values(var_dict["b/dense/bias"])

        expected = relu(dense_layer(dense_layer(input_, w1_value, b1_value), w2_value, b2_value))

        test.test(("call", input_), expected_outputs=expected, decimals=5)

        test.terminate()

    def test_keras_style_one_output_is_discarded(self):
        # Input Space of the network.
        input_space = FloatBox(shape=(3,), add_batch_rank=True, add_time_rank=True)

        # Pass input through an LSTM and get two outputs (output and internal states), only one of which will be used.
        lstm_out, _ = LSTMLayer(units=2, return_sequences=False)(input_space)

        # A NN with 1 output (don't return internal_states of LSTM).
        neural_net = NeuralNetwork(outputs=lstm_out)

        test = ComponentTest(component=neural_net, input_spaces=dict(inputs=input_space))

        # Batch of size=n.
        input_ = input_space.sample((5, 3))
        # Calculate output manually.
        var_dict = neural_net.variable_registry
        w1_value = test.read_variable_values(var_dict["neural-network/lstm-layer/lstm-cell/kernel"])
        b1_value = test.read_variable_values(var_dict["neural-network/lstm-layer/lstm-cell/bias"])

        expected_out, _ = lstm_layer(input_, w1_value, b1_value)
        expected_out = expected_out[:, -1, :]  # last time step only

        # Don't expect internal states (our NN does not return these as per the functional API definition above).
        test.test(("call", input_), expected_outputs=expected_out, decimals=5)

        test.terminate()

    def test_keras_style_two_separate_input_spaces(self):
        # Define two input Spaces first. Independently (no container).
        input_space_1 = IntBox(3, add_batch_rank=True)
        input_space_2 = FloatBox(shape=(4,), add_batch_rank=True)

        # One-hot flatten the int tensor.
        flatten_layer_out = ReShape(flatten=True, flatten_categories=True)(input_space_1)
        # Run the float tensor through two dense layers.
        dense_1_out = DenseLayer(units=3, scope="d1")(input_space_2)
        dense_2_out = DenseLayer(units=5, scope="d2")(dense_1_out)
        # Concat everything.
        cat_out = ConcatLayer()(flatten_layer_out, dense_2_out)

        # Use the `outputs` arg to allow your network to trace back the data flow until the input space.
        neural_net = NeuralNetwork(inputs=[input_space_1, input_space_2], outputs=cat_out)

        test = ComponentTest(component=neural_net, input_spaces=dict(inputs=[input_space_1, input_space_2]))

        var_dict = neural_net.variable_registry
        w1_value = test.read_variable_values(var_dict["neural-network/d1/dense/kernel"])
        b1_value = test.read_variable_values(var_dict["neural-network/d1/dense/bias"])
        w2_value = test.read_variable_values(var_dict["neural-network/d2/dense/kernel"])
        b2_value = test.read_variable_values(var_dict["neural-network/d2/dense/bias"])

        # Batch of size=n.
        input_ = [input_space_1.sample(4), input_space_2.sample(4)]

        expected = np.concatenate([  # concat everything
            one_hot(input_[0]),  # int flattening
            dense_layer(dense_layer(input_[1], w1_value, b1_value), w2_value, b2_value)  # float -> 2 x dense
        ], axis=-1)
        out = test.test(("call", input_), expected_outputs=expected)

        test.terminate()

    def test_keras_style_one_container_input_space(self):
        # Define one container input Space.
        input_space = Tuple(IntBox(3), FloatBox(shape=(4,)), add_batch_rank=True)

        # One-hot flatten the int tensor.
        flatten_layer_out = ReShape(flatten=True, flatten_categories=True)(input_space[0])
        # Run the float tensor through two dense layers.
        dense_1_out = DenseLayer(units=3, scope="d1")(input_space[1])
        dense_2_out = DenseLayer(units=5, scope="d2")(dense_1_out)
        # Concat everything.
        cat_out = ConcatLayer()(flatten_layer_out, dense_2_out)

        # Use the `outputs` arg to allow your network to trace back the data flow until the input space.
        # `inputs` is not needed  here as we only have one single input (the Tuple).
        neural_net = NeuralNetwork(outputs=cat_out)

        test = ComponentTest(component=neural_net, input_spaces=dict(inputs=input_space))

        var_dict = neural_net.variable_registry
        w1_value = test.read_variable_values(var_dict["neural-network/d1/dense/kernel"])
        b1_value = test.read_variable_values(var_dict["neural-network/d1/dense/bias"])
        w2_value = test.read_variable_values(var_dict["neural-network/d2/dense/kernel"])
        b2_value = test.read_variable_values(var_dict["neural-network/d2/dense/bias"])

        # Batch of size=n.
        input_ = input_space.sample(4)

        expected = np.concatenate([  # concat everything
            one_hot(input_[0]),  # int flattening
            dense_layer(dense_layer(input_[1], w1_value, b1_value), w2_value, b2_value)  # float -> 2 x dense
        ], axis=-1)
        out = test.test(("call", tuple([input_])), expected_outputs=expected)

        test.terminate()

    def test_keras_style_multi_stream_nn(self):
        # Input Space of the network.
        input_space = Dict({
            "img": FloatBox(shape=(6, 6, 3)),  # some RGB img
            "txt": TextBox()  # some text
        }, add_batch_rank=True, add_time_rank=True)

        # Complex NN assembly via our Keras-style functional API.
        # Fold text input into single batch rank.
        folded_text = ReShape(fold_time_rank=True)(input_space["txt"])
        # String layer will create batched AND time-ranked (individual words) hash outputs (int64).
        string_bucket_out, lengths = StringToHashBucket(num_hash_buckets=5)(folded_text)
        # Batched and time-ranked embedding output (floats) with embed dim=n.
        embedding_out = EmbeddingLookup(embed_dim=10, vocab_size=5)(string_bucket_out)
        # Pass embeddings through a text LSTM and use last output (reduce time-rank).
        string_lstm_out, _ = LSTMLayer(units=2, return_sequences=False, scope="lstm-layer-txt")(
            embedding_out, sequence_length=lengths
        )
        # Unfold to get original time-rank back.
        string_lstm_out_unfolded = ReShape(unfold_time_rank=True)(string_lstm_out, input_space["txt"])

        # Parallel image stream via 1 CNN layer plus dense.
        folded_img = ReShape(fold_time_rank=True, scope="img-fold")(input_space["img"])
        cnn_out = Conv2DLayer(filters=1, kernel_size=2, strides=2)(folded_img)
        unfolded_cnn_out = ReShape(unfold_time_rank=True, scope="img-unfold")(cnn_out, input_space["img"])
        unfolded_cnn_out_flattened = ReShape(flatten=True, scope="img-flat")(unfolded_cnn_out)
        dense_out = DenseLayer(units=2, scope="dense-0")(unfolded_cnn_out_flattened)

        # Concat everything.
        concat_out = ConcatLayer()(string_lstm_out_unfolded, dense_out)

        # LSTM output has batch+time.
        main_lstm_out, internal_states = LSTMLayer(units=2, scope="lstm-layer-main")(concat_out)

        dense1_after_lstm_out = DenseLayer(units=3, scope="dense-1")(main_lstm_out)
        dense2_after_lstm_out = DenseLayer(units=2, scope="dense-2")(dense1_after_lstm_out)
        dense3_after_lstm_out = DenseLayer(units=1, scope="dense-3")(dense2_after_lstm_out)

        # A NN with 3 outputs.
        neural_net = NeuralNetwork(outputs=[dense3_after_lstm_out, main_lstm_out, internal_states])

        test = ComponentTest(component=neural_net, input_spaces=dict(inputs=input_space))

        # Batch of size=n.
        sample_shape = (4, 2)
        input_ = input_space.sample(sample_shape)

        out = test.test(("call", input_), expected_outputs=None)
        # Main output (Dense out after LSTM).
        self.assertTrue(out[0].shape == sample_shape + (1,))  # 1=1 unit in dense layer
        self.assertTrue(out[0].dtype == np.float32)
        # main-LSTM out.
        self.assertTrue(out[1].shape == sample_shape + (2,))  # 2=2 LSTM units
        self.assertTrue(out[1].dtype == np.float32)
        # main-LSTM internal-states.
        self.assertTrue(out[2][0].shape == sample_shape[:1] + (2,))  # 2=2 LSTM units
        self.assertTrue(out[2][0].dtype == np.float32)
        self.assertTrue(out[2][1].shape == sample_shape[:1] + (2,))  # 2=2 LSTM units
        self.assertTrue(out[2][1].dtype == np.float32)

        test.terminate()

    def test_keras_style_complex_multi_stream_nn(self):
        # 3 inputs.
        input_spaces = [
            Dict({
                "img": FloatBox(shape=(6, 6, 3)),
                "int": IntBox(3)
            }, add_batch_rank=True, add_time_rank=True),
            FloatBox(shape=(2,), add_batch_rank=True),
            Tuple(IntBox(2), TextBox(), add_batch_rank=True, add_time_rank=True)
        ]

        # Same NN as in test above, only using some of the sub-Spaces from the input spaces.
        # Tests whether this NN can add automatically the correct splitters.
        folded_text = ReShape(fold_time_rank=True)(input_spaces[2][1])
        # String layer will create batched AND time-ranked (individual words) hash outputs (int64).
        string_bucket_out, lengths = StringToHashBucket(num_hash_buckets=5)(folded_text)
        # Batched and time-ranked embedding output (floats) with embed dim=n.
        embedding_out = EmbeddingLookup(embed_dim=10, vocab_size=5)(string_bucket_out)
        # Pass embeddings through a text LSTM and use last output (reduce time-rank).
        string_lstm_out, _ = LSTMLayer(units=2, return_sequences=False, scope="lstm-layer-txt")(
            embedding_out, sequence_length=lengths
        )
        # Unfold to get original time-rank back.
        string_lstm_out_unfolded = ReShape(unfold_time_rank=True)(string_lstm_out, input_spaces[2][1])

        # Parallel image stream via 1 CNN layer plus dense.
        folded_img = ReShape(fold_time_rank=True, scope="img-fold")(input_spaces[0]["img"])
        cnn_out = Conv2DLayer(filters=1, kernel_size=2, strides=2)(folded_img)
        unfolded_cnn_out = ReShape(unfold_time_rank=True, scope="img-unfold")(cnn_out, input_spaces[0]["img"])
        unfolded_cnn_out_flattened = ReShape(flatten=True, scope="img-flat")(unfolded_cnn_out)
        dense_out = DenseLayer(units=2, scope="dense-0")(unfolded_cnn_out_flattened)

        # Concat everything.
        concat_out = ConcatLayer()(string_lstm_out_unfolded, dense_out)

        # LSTM output has batch+time.
        main_lstm_out, internal_states = LSTMLayer(units=2, scope="lstm-layer-main")(concat_out)

        dense1_after_lstm_out = DenseLayer(units=3, scope="dense-1")(main_lstm_out)
        dense2_after_lstm_out = DenseLayer(units=2, scope="dense-2")(dense1_after_lstm_out)
        dense3_after_lstm_out = DenseLayer(units=1, scope="dense-3")(dense2_after_lstm_out)

        # A NN with 3 outputs.
        neural_net = NeuralNetwork(inputs=input_spaces, outputs=[dense3_after_lstm_out, main_lstm_out, internal_states])

        test = ComponentTest(component=neural_net, input_spaces=dict(inputs=input_spaces))

        # Batch of size=n.
        sample_shape = (4, 2)
        input_ = [input_spaces[0].sample(sample_shape), input_spaces[1].sample(sample_shape[0]),
                  input_spaces[2].sample(sample_shape)]

        out = test.test(("call", tuple(input_)), expected_outputs=None)
        # Main output (Dense out after LSTM).
        self.assertTrue(out[0].shape == sample_shape + (1,))  # 1=1 unit in dense layer
        self.assertTrue(out[0].dtype == np.float32)
        # main-LSTM out.
        self.assertTrue(out[1].shape == sample_shape + (2,))  # 2=2 LSTM units
        self.assertTrue(out[1].dtype == np.float32)
        # main-LSTM internal-states.
        self.assertTrue(out[2][0].shape == sample_shape[:1] + (2,))  # 2=2 LSTM units
        self.assertTrue(out[2][0].dtype == np.float32)
        self.assertTrue(out[2][1].shape == sample_shape[:1] + (2,))  # 2=2 LSTM units
        self.assertTrue(out[2][1].dtype == np.float32)

        test.terminate()
