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

from rlgraph import get_backend
from rlgraph.components.action_adapters import ActionAdapter
from rlgraph.utils.decorators import graph_fn
from rlgraph.utils.ops import DataOpTuple
from rlgraph.utils.util import MIN_LOG_STDDEV, MAX_LOG_STDDEV


if get_backend() == "tf":
    import tensorflow as tf
elif get_backend() == "pytorch":
    import torch


class SquashedNormalDistributionAdapter(ActionAdapter):
    """
    Action adapter for the Squashed-normal distribution.
    """
    def get_units_and_shape(self):
        # Add moments (2x for each action item).
        units = 2 * self.action_space.flat_dim  # Those two dimensions are the mean and log sd
        if self.action_space.shape == ():
            new_shape = (2,)
        else:
            new_shape = tuple(list(self.action_space.shape[:-1]) + [self.action_space.shape[-1] * 2])
        return units, new_shape

    @graph_fn
    def _graph_fn_get_parameters_from_adapter_outputs(self, adapter_outputs):
        if get_backend() == "tf":
            mean, log_sd = tf.split(adapter_outputs, num_or_size_splits=2, axis=-1)
            log_sd = tf.clip_by_value(log_sd, MIN_LOG_STDDEV, MAX_LOG_STDDEV)

            # Turn log sd into sd to ascertain always positive stddev values.
            sd = tf.exp(log_sd)

            mean._batch_rank = 0
            sd._batch_rank = 0

        elif get_backend() == "pytorch":
            mean, log_sd = torch.split(adapter_outputs, split_size_or_sections=2, dim=1)
            log_sd = torch.clamp(log_sd, min=MIN_LOG_STDDEV, max=MAX_LOG_STDDEV)

            # Turn log sd into sd.
            sd = torch.exp(log_sd)

        parameters = DataOpTuple([mean, sd])
        return parameters, None, None
