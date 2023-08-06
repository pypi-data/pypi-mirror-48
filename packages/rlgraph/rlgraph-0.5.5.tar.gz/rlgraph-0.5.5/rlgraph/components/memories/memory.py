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

from rlgraph.utils.ops import FLATTEN_SCOPE_PREFIX
from rlgraph.components.component import Component, rlgraph_api
from rlgraph.utils import FlattenedDataOp


class Memory(Component):
    """
    Abstract memory component.

    API:
        insert_records(records) -> Triggers an insertion of records into the memory.
        get_records(num_records) -> Returns `num_records` records from the memory.
    """
    def __init__(self, capacity=1000, scope="memory", **kwargs):
        """
        Args:
            capacity (int): Maximum capacity of the memory.
        """
        super(Memory, self).__init__(scope=scope, **kwargs)

        # Variables (will be populated in create_variables).
        self.record_space = None
        self.memory = None
        self.flat_record_space = None
        self.capacity = capacity
        # The current size of the memory.
        self.size = None

        # Use this to get batch size.
        self.terminal_key = FLATTEN_SCOPE_PREFIX + "terminals"

    def create_variables(self, input_spaces, action_space=None):
        # Store our record-space for convenience.
        self.record_space = input_spaces["records"]
        self.flat_record_space = self.record_space.flatten()

        # Create the main memory as a flattened OrderedDict from any arbitrarily nested Space.
        self.memory = self.get_variable(
            name="memory", trainable=False,
            from_space=self.record_space,
            flatten=True,
            add_batch_rank=self.capacity,
            initializer=0
        )
        # Number of elements present.
        self.size = self.get_variable(name="size", dtype=int, trainable=False, initializer=0)

    @rlgraph_api(flatten_ops=True)
    def _graph_fn_insert_records(self, records):
        """
        Inserts one or more complex records.

        Args:
            records (FlattenedDataOp): FlattenedDataOp containing record data. Keys must match keys in record
                space.
        """
        raise NotImplementedError

    @rlgraph_api
    def _graph_fn_get_records(self, num_records=1):
        """
        Returns a number of records according to the retrieval strategy implemented by
        the memory.

        Args:
            num_records (int): Number of records to return.

        Returns:
            DataOpDict: The retrieved records.
        """
        raise NotImplementedError

    @rlgraph_api(returns=0)
    def _graph_fn_get_episodes(self, num_episodes=1):
        """
        Retrieves a given number of episodes.

        Args:
            num_episodes (int): Number of episodes to retrieve.

        Returns: The retrieved episodes.
        """
        pass

    def _read_records(self, indices):
        """
        Obtains record values for the provided indices.

        Args:
            indices (Union[ndarray,tf.Tensor]): Indices to read. Assumed to be not contiguous.

        Returns:
             FlattenedDataOp: Record value dict.
        """
        records = FlattenedDataOp()
        for name, variable in self.memory.items():
            records[name] = self.read_variable(variable, indices)
        return records

    @rlgraph_api
    def _graph_fn_get_size(self):
        """
        Returns the current size of the memory.

        Returns:
            SingleDataOp: The size (int) of the memory.
        """
        return self.read_variable(self.size)
