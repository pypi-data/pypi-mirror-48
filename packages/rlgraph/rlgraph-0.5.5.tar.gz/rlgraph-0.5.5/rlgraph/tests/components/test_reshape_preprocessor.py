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

import unittest

import numpy as np

from rlgraph.components.layers import ReShape
from rlgraph.components.neural_networks.stack import Stack
from rlgraph.spaces import *
from rlgraph.tests import ComponentTest, recursive_assert_almost_equal
from rlgraph.utils.numpy import one_hot


class TestReShapePreprocessors(unittest.TestCase):

    def test_reshape(self):
        reshape = ReShape(new_shape=(3, 2))
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=FloatBox(shape=(6,), add_batch_rank=True)
        ))

        test.test("reset")
        # Batch=2
        inputs = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
        expected = np.array([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_flatten_option(self):
        # Test flattening while leaving batch and time rank as is.
        in_space = FloatBox(shape=(2, 3, 4), add_batch_rank=True, add_time_rank=True, time_major=True)
        reshape = ReShape(flatten=True)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # Time-rank=5, Batch=2
        inputs = in_space.sample(size=(5, 2))
        expected = np.reshape(inputs, newshape=(5, 2, 24))
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_flatten_option_only_time_rank(self):
        # Test flattening while leaving batch and time rank as is.
        in_space = FloatBox(shape=(2, 3), add_batch_rank=False, add_time_rank=True)
        reshape = ReShape(flatten=True)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # Time-rank=5, Batch=2
        inputs = in_space.sample(size=3)
        expected = np.reshape(inputs, newshape=(3, 6))
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_flatten_option_with_0D_shape(self):
        # Test flattening int with shape=().
        in_space = IntBox(3, shape=(), add_batch_rank=True)
        reshape = ReShape(flatten=True, flatten_categories=3)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # Time-rank=5, Batch=2
        inputs = in_space.sample(size=4)
        # Expect a by-int-category one-hot flattening.
        expected = one_hot(inputs, depth=3)
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_flatten_option_with_categories(self):
        # Test flattening while leaving batch and time rank as is, but flattening out int categories.
        in_space = IntBox(2, shape=(2, 3, 4), add_batch_rank=True, add_time_rank=True, time_major=False)
        reshape = ReShape(flatten=True, flatten_categories=2)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # Batch=3, time-rank=5
        inputs = in_space.sample(size=(3, 5))
        expected = np.reshape(one_hot(inputs, depth=2), newshape=(3, 5, 48)).astype(dtype=np.float32)
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_flatten_option_without_categories(self):
        # Test flattening while leaving batch and time rank as is.
        in_space = IntBox(3, shape=(2, 3, 4), add_batch_rank=True, add_time_rank=True, time_major=False)
        reshape = ReShape(flatten=True, flatten_categories=False)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # Batch=3, time-rank=5
        inputs = in_space.sample(size=(3, 5))
        expected = np.reshape(inputs, newshape=(3, 5, 24)).astype(dtype=np.float32)
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_time_rank(self):
        # Test with time-rank instead of batch-rank.
        in_space = FloatBox(shape=(4,), add_batch_rank=False, add_time_rank=True)
        reshape = ReShape(new_shape=(2, 2))
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        inputs = in_space.sample(size=3)
        expected = np.reshape(inputs, newshape=(3, 2, 2))
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_time_rank_folding(self):
        # Fold time rank into batch rank.
        in_space = FloatBox(shape=(4, 4), add_batch_rank=True, add_time_rank=True, time_major=True)
        reshape = ReShape(fold_time_rank=True)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # seq-len=3, batch-size=2
        inputs = in_space.sample(size=(3, 2))
        expected = np.reshape(inputs, newshape=(6, 4, 4))
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_time_rank_unfolding(self):
        # Unfold time rank from batch rank with given time-dimension (2 out of 8 -> batch will be 4 after unfolding).
        in_space = FloatBox(shape=(4, 4), add_batch_rank=True, add_time_rank=False)
        in_space_before_folding = FloatBox(shape=(4, 4), add_batch_rank=True, add_time_rank=True)
        reshape = ReShape(unfold_time_rank=True)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space, input_before_time_rank_folding=in_space_before_folding
        ))

        test.test("reset")
        # seq-len=2, batch-size=4 -> unfold from 8.
        inputs = in_space.sample(size=8)
        inputs_before_folding = in_space_before_folding.sample(size=(4, 2))
        expected = np.reshape(inputs, newshape=(4, 2, 4, 4))
        test.test(("call", (inputs, inputs_before_folding)), expected_outputs=expected)

    def test_reshape_python_with_time_rank_unfolding(self):
        # Unfold time rank from batch rank with given time-dimension (2 out of 8 -> batch will be 4 after unfolding).
        in_space = FloatBox(shape=(4, 4), add_batch_rank=True, add_time_rank=False)
        in_space_before_folding = FloatBox(shape=(4, 4), add_batch_rank=True, add_time_rank=True)
        reshape = ReShape(unfold_time_rank=True, backend="python")
        reshape.create_variables(dict(
            inputs=in_space, input_before_time_rank_folding=in_space_before_folding
        ))

        # seq-len=2, batch-size=4 -> unfold from 8.
        inputs = in_space.sample(size=8)
        inputs_before_folding = in_space_before_folding.sample(size=(4, 2))
        expected = np.reshape(inputs, newshape=(4, 2, 4, 4))
        out = reshape._graph_fn_call(inputs, inputs_before_folding)

        recursive_assert_almost_equal(out, expected)

    def test_reshape_with_time_and_batch_ranks_and_reshaping(self):
        in_space = FloatBox(shape=(5, 8), add_batch_rank=True, add_time_rank=True, time_major=True)
        reshape = ReShape(new_shape=(4, 10))
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # seq-len=2, batch-size=4
        inputs = in_space.sample(size=(2, 4))
        # Reshape without the first two ranks.
        expected = np.reshape(inputs, newshape=(2, 4, 4, 10))
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_batch_and_time_ranks_and_flattening(self):
        in_space = FloatBox(shape=(6, 4, 2), add_batch_rank=True, add_time_rank=True, time_major=False)
        reshape = ReShape(flatten=True)
        test = ComponentTest(component=reshape, input_spaces=dict(
            inputs=in_space
        ))

        test.test("reset")
        # batch-size=1, seq-len=3
        inputs = in_space.sample(size=(1, 3))
        # Reshape without the first two ranks.
        expected = np.reshape(inputs, newshape=(1, 3, 48))
        test.test(("call", inputs), expected_outputs=expected)

    def test_reshape_with_batch_and_time_ranks_and_with_folding_and_unfolding(self):
        # Flip time and batch rank via folding, then unfolding.
        in_space = FloatBox(shape=(3, 2), add_batch_rank=True, add_time_rank=True, time_major=False)
        reshape_fold = ReShape(fold_time_rank=True)
        reshape_unfold = ReShape(unfold_time_rank=True, time_major=False)

        def custom_call(self_, inputs):
            folded = reshape_fold.call(inputs)
            unfolded = reshape_unfold.call(folded, inputs)
            return unfolded

        stack = Stack(reshape_fold, reshape_unfold, api_methods={("call", custom_call)})

        test = ComponentTest(component=stack, input_spaces=dict(inputs=in_space))

        # batch-size=4, seq-len=2
        inputs = in_space.sample(size=(4, 2))

        test.test(("call", inputs), expected_outputs=inputs)

    def test_reshape_with_batch_and_time_ranks_with_folding_and_unfolding_0D_shape(self):
        # Flip time and batch rank via folding, then unfolding.
        in_space = FloatBox(shape=(), add_batch_rank=True, add_time_rank=True, time_major=True)
        reshape_fold = ReShape(fold_time_rank=True, scope="fold-time-rank")
        reshape_unfold = ReShape(unfold_time_rank=True, scope="unfold-time-rank", time_major=True)

        def custom_call(self_, inputs):
            folded = reshape_fold.call(inputs)
            unfolded = reshape_unfold.call(folded, inputs)
            return unfolded

        stack = Stack(reshape_fold, reshape_unfold, api_methods={("call", custom_call)})

        test = ComponentTest(component=stack, input_spaces=dict(inputs=in_space))

        # seq-len=16, batch-size=8
        inputs = in_space.sample(size=(16, 8))

        test.test(("call", inputs), expected_outputs=inputs)

    def test_reshape_with_batch_and_time_ranks_with_folding_and_explicit_unfolding(self):
        time_rank = 8
        in_space = FloatBox(shape=(2, 3), add_batch_rank=True, add_time_rank=True, time_major=True)
        reshape_fold = ReShape(fold_time_rank=True, scope="fold-time-rank")
        reshape_unfold = ReShape(unfold_time_rank=time_rank, scope="unfold-time-rank", time_major=True)

        def custom_call(self_, inputs):
            folded = reshape_fold.call(inputs)
            unfolded = reshape_unfold.call(folded)  # no need for orig input here as unfolding is explicit
            return unfolded

        stack = Stack(reshape_fold, reshape_unfold, api_methods={("call", custom_call)})

        test = ComponentTest(component=stack, input_spaces=dict(inputs=in_space))

        # seq-len=time_rank, batch-size=n
        inputs = in_space.sample(size=(time_rank, 12))

        test.test(("call", inputs), expected_outputs=inputs)
