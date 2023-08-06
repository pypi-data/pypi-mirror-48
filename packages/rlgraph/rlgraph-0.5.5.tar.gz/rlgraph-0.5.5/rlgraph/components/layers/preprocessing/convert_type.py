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
from rlgraph.components.layers.preprocessing.preprocess_layer import PreprocessLayer
from rlgraph.spaces import IntBox, FloatBox, BoolBox, ContainerSpace
from rlgraph.spaces.space_utils import get_space_from_op
from rlgraph.utils import util
from rlgraph.utils.decorators import rlgraph_api
from rlgraph.utils.rlgraph_errors import RLGraphError

if get_backend() == "tf":
    import tensorflow as tf
elif get_backend() == "pytorch":
    import torch


class ConvertType(PreprocessLayer):
    """
    Converts data types of inputs for static type checking.
    """
    def __init__(self, to_dtype, scope="convert-type", **kwargs):
        """
        Args:
            to_dtype (str): Target data type.
        """
        super(ConvertType, self).__init__(scope=scope, **kwargs)
        self.to_dtype = to_dtype

    def check_input_spaces(self, input_spaces, action_space=None):
        assert not isinstance(input_spaces, ContainerSpace)

    def get_preprocessed_space(self, space):
        # TODO map of allowed conversions in utils?
        if isinstance(space, IntBox):
            if self.to_dtype == "float" or self.to_dtype == "float32" or self.to_dtype == "np.float"\
                    or self.to_dtype == "tf.float32" or self.to_dtype == "torch.float32":
                return FloatBox(shape=space.shape, low=space.low, high=space.high,
                                add_batch_rank=space.has_batch_rank, add_time_rank=space.has_time_rank)
            elif self.to_dtype == "bool":
                if space.low == 0 and space.high == 1:
                    return BoolBox(shape=space.shape, add_batch_rank=space.has_batch_rank,
                                   add_time_rank=space.has_time_rank)
                else:
                    raise RLGraphError("ERROR: Conversion from IntBox to BoolBox not allowed if low is not 0 and "
                                       "high is not 1.")
        elif isinstance(space, BoolBox):
            if self.to_dtype == "float" or self.to_dtype == "float32" or self.to_dtype == "np.float" \
                 or self.to_dtype == "tf.float32" or self.to_dtype == "torch.float32":
                return FloatBox(shape=space.shape, low=0.0, high=1.0,
                                add_batch_rank=space.has_batch_rank, add_time_rank=space.has_time_rank)
            elif self.to_dtype == "int" or self.to_dtype == "int32" or self.to_dtype  == "np.int32" or \
                    self.to_dtype == "tf.int32" or self.to_dtype == "torch.int32":
                return IntBox(shape=space.shape, low=0, high=1,
                              add_batch_rank=space.has_batch_rank, add_time_rank=space.has_time_rank)
        elif isinstance(space, FloatBox):
            if self.to_dtype == "int" or self.to_dtype == "int32" or self.to_dtype  == "np.int32" or \
                 self.to_dtype == "tf.int32" or self.to_dtype == "torch.int32":
                return IntBox(shape=space.shape, low=space.low, high=space.high,
                              add_batch_rank=space.has_batch_rank, add_time_rank=space.has_time_rank)

        # Wrong conversion.
        else:
            raise RLGraphError("ERROR: Space conversion from: {} to type {} not supported".format(
                space, self.to_dtype
            ))

        # No conversion.
        return space

    @rlgraph_api
    def _graph_fn_call(self, inputs):
        if self.backend == "python" or get_backend() == "python":
            if isinstance(inputs, list):
                inputs = np.asarray(inputs)
            return inputs.astype(dtype=util.convert_dtype(self.to_dtype, to="np"))
        elif get_backend() == "pytorch":
            torch_dtype = util.convert_dtype(self.to_dtype, to="pytorch")
            if torch_dtype == torch.float or torch.float32:
                return inputs.float()
            elif torch_dtype == torch.int or torch.int32:
                return inputs.int()
            elif torch_dtype == torch.uint8:
                return inputs.byte()
        elif get_backend() == "tf":
            in_space = get_space_from_op(inputs)
            to_dtype = util.convert_dtype(self.to_dtype, to="tf")
            if inputs.dtype != to_dtype:
                ret = tf.cast(x=inputs, dtype=to_dtype)
                if in_space.has_batch_rank is True:
                    ret._batch_rank = 0 if in_space.time_major is False else 1
                if in_space.has_time_rank is True:
                    ret._time_rank = 0 if in_space.time_major is True else 1
                return ret
            else:
                return inputs
