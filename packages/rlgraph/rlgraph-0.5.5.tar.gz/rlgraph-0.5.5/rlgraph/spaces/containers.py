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

import numpy as np

from rlgraph.spaces.space import Space
from rlgraph.utils.ops import DataOpDict, DataOpTuple, FLAT_TUPLE_OPEN, FLAT_TUPLE_CLOSE, unflatten_op, flat_key_lookup
from rlgraph.utils.rlgraph_errors import RLGraphError


class ContainerSpace(Space):
    """
    A simple placeholder class for Spaces that contain other Spaces.
    """
    def sample(self, size=None, fill_value=None, horizontal=False):
        """
        Child classes must overwrite this one again with support for the `horizontal` parameter.

        Args:
            horizontal (bool): False: Within this container, sample each child-space `size` times.
                True: Produce `size` single containers in an np.array of len `size`.
        """
        raise NotImplementedError

    def flat_key_lookup(self, flat_key, custom_scope_separator=None):
        return flat_key_lookup(self, flat_key, custom_scope_separator)


class Dict(ContainerSpace, dict):
    """
    A Dict space (an ordered and keyed combination of n other spaces).
    Supports nesting of other Dict/Tuple spaces (or any other Space types) inside itself.
    """
    def __init__(self, spec=None, **kwargs):
        add_batch_rank = kwargs.pop("add_batch_rank", False)
        add_time_rank = kwargs.pop("add_time_rank", False)
        time_major = kwargs.pop("time_major", False)

        ContainerSpace.__init__(self, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major)

        # Allow for any spec or already constructed Space to be passed in as values in the python-dict.
        # Spec may be part of kwargs.
        if spec is None:
            spec = kwargs

        space_dict = {}
        for key in sorted(spec.keys()):
            # Keys must be strings.
            if not isinstance(key, str):
                raise RLGraphError("ERROR: No non-str keys allowed in a Dict-Space!")
            # Prohibit reserved characters (for flattened syntax).
            #if re.search(r'/|{}\d+{}'.format(FLAT_TUPLE_OPEN, FLAT_TUPLE_CLOSE), key):
            #    raise RLGraphError("ERROR: Key to Dict must not contain '/' or '{}\d+{}'! Key='{}'.".
            #                       format(FLAT_TUPLE_OPEN, FLAT_TUPLE_CLOSE, key))
            value = spec[key]
            # Value is already a Space: Copy it (to not affect original Space) and maybe add/remove batch/time-ranks.
            if isinstance(value, Space):
                w_batch_w_time = value.with_extra_ranks(add_batch_rank, add_time_rank, time_major)
                space_dict[key] = w_batch_w_time
            # Value is a list/tuple -> treat as Tuple space.
            elif isinstance(value, (list, tuple)):
                space_dict[key] = Tuple(
                    *value, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major
                )
            # Value is a spec (or a spec-dict with "type" field) -> produce via `from_spec`.
            elif (isinstance(value, dict) and "type" in value) or not isinstance(value, dict):
                space_dict[key] = Space.from_spec(
                    value, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major
                )
            # Value is a simple dict -> recursively construct another Dict Space as a sub-space of this one.
            else:
                space_dict[key] = Dict(
                    value, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major
                )
            # Set the parent of the added Space to `self`.
            space_dict[key].parent = self

        dict.__init__(self, space_dict)

    def _add_batch_rank(self, add_batch_rank=False):
        super(Dict, self)._add_batch_rank(add_batch_rank)
        for v in self.values():
            v._add_batch_rank(add_batch_rank)

    def _add_time_rank(self, add_time_rank=False, time_major=False):
        super(Dict, self)._add_time_rank(add_time_rank, time_major)
        for v in self.values():
            v._add_time_rank(add_time_rank, time_major)

    def force_batch(self, samples, horizontal=False):
        # Return a batch of dicts.
        if horizontal is True:
            # Input is already batched.
            if isinstance(samples, (np.ndarray, list, tuple)):
                return samples, False  # False=batch rank was not added
            # Input is a single dict, return batch=1 sample.
            else:
                return np.array([samples]), True  # True=batch rank was added
        # Return a dict of batched data.
        else:
            # `samples` is already a batched structure (list, tuple, ndarray).
            if isinstance(samples, (np.ndarray, list, tuple)):
                return dict({key: self[key].force_batch([s[key] for s in samples], horizontal=horizontal)[0]
                             for key in sorted(self.keys())}), False
            # `samples` is already a container (underlying data could be batched or not).
            else:
                # Figure out, whether underlying data is already batched.
                first_key = next(iter(samples))
                batch_was_added = self[first_key].force_batch(samples[first_key], horizontal=horizontal)[1]
                return dict({key: self[key].force_batch(samples[key], horizontal=horizontal)[0]
                             for key in sorted(self.keys())}), batch_was_added

    @property
    def shape(self):
        return tuple([self[key].shape for key in sorted(self.keys())])

    def get_shape(self, with_batch_rank=False, with_time_rank=False, time_major=None, with_category_rank=False):
        return tuple([self[key].get_shape(
            with_batch_rank=with_batch_rank, with_time_rank=with_time_rank, time_major=time_major,
            with_category_rank=with_category_rank
        ) for key in sorted(self.keys())])

    @property
    def rank(self):
        return tuple([self[key].rank for key in sorted(self.keys())])

    @property
    def flat_dim(self):
        return int(np.sum([c.flat_dim for c in self.values()]))

    @property
    def dtype(self):
        return DataOpDict([(key, subspace.dtype) for key, subspace in self.items()])

    def get_variable(self, name, is_input_feed=False, add_batch_rank=None, add_time_rank=None, time_major=None,
                     **kwargs):
        return DataOpDict(
            [(key, subspace.get_variable(
                name + "/" + key, is_input_feed=is_input_feed, add_batch_rank=add_batch_rank,
                add_time_rank=add_time_rank, time_major=time_major, **kwargs
            )) for key, subspace in self.items()]
        )

    def _flatten(self, mapping, custom_scope_separator, scope_separator_at_start, return_as_dict_space,
                 scope_, list_):
        # Iterate through this Dict.
        scope_ += custom_scope_separator if len(scope_) > 0 or scope_separator_at_start else ""
        for key in sorted(self.keys()):
            self[key].flatten(
                mapping, custom_scope_separator, scope_separator_at_start, return_as_dict_space, scope_ + key, list_
            )

    def sample(self, size=None, fill_value=None, horizontal=False):
        if horizontal:
            return np.array([{key: self[key].sample(fill_value=fill_value) for key in sorted(self.keys())}] *
                            (size or 1))
        else:
            return {key: self[key].sample(size=size, fill_value=fill_value) for key in sorted(self.keys())}

    def zeros(self, size=None):
        return DataOpDict([(key, subspace.zeros(size=size)) for key, subspace in self.items()])

    def contains(self, sample):
        return isinstance(sample, dict) and all(self[key].contains(sample[key]) for key in self.keys())

    def map(self, mapping):
        flattened_self = self.flatten(mapping=mapping)
        return Dict(
            dict(unflatten_op(flattened_self)),
            add_batch_rank=self.has_batch_rank, add_time_rank=self.has_time_rank, time_major=self.time_major
        )

    def __repr__(self):
        return "Dict({})".format([(key, self[key].__repr__()) for key in self.keys()])

    def __eq__(self, other):
        if not isinstance(other, Dict):
            return False
        return dict(self) == dict(other)


class Tuple(ContainerSpace, tuple):
    """
    A Tuple space (an ordered sequence of n other spaces).
    Supports nesting of other container (Dict/Tuple) spaces inside itself.
    """
    def __new__(cls, *components, **kwargs):
        if isinstance(components[0], (list, tuple)) and not isinstance(components[0], Tuple):
            assert len(components) == 1
            components = components[0]

        add_batch_rank = kwargs.get("add_batch_rank", False)
        add_time_rank = kwargs.get("add_time_rank", False)
        time_major = kwargs.get("time_major", False)

        # Allow for any spec or already constructed Space to be passed in as values in the python-list/tuple.
        list_ = list()
        for value in components:
            # Value is already a Space: Copy it (to not affect original Space) and maybe add/remove batch-rank.
            if isinstance(value, Space):
                list_.append(value.with_extra_ranks(add_batch_rank, add_time_rank, time_major))
            # Value is a list/tuple -> treat as Tuple space.
            elif isinstance(value, (list, tuple)):
                list_.append(
                    Tuple(*value, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major)
                )
            # Value is a spec (or a spec-dict with "type" field) -> produce via `from_spec`.
            elif (isinstance(value, dict) and "type" in value) or not isinstance(value, dict):
                list_.append(Space.from_spec(
                    value, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major
                ))
            # Value is a simple dict -> recursively construct another Dict Space as a sub-space of this one.
            else:
                list_.append(Dict(
                    value, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major
                ))

        return tuple.__new__(cls, list_)

    def __init__(self, *components, **kwargs):
        add_batch_rank = kwargs.get("add_batch_rank", False)
        add_time_rank = kwargs.get("add_time_rank", False)
        time_major = kwargs.get("time_major", False)
        super(Tuple, self).__init__(add_batch_rank=add_batch_rank, add_time_rank=add_time_rank, time_major=time_major)

        # Set the parent of the added Space to `self`.
        for c in self:
            c.parent = self

    def _add_batch_rank(self, add_batch_rank=False):
        super(Tuple, self)._add_batch_rank(add_batch_rank)
        for v in self:
            v._add_batch_rank(add_batch_rank)

    def _add_time_rank(self, add_time_rank=False, time_major=False):
        super(Tuple, self)._add_time_rank(add_time_rank, time_major)
        for v in self:
            v._add_time_rank(add_time_rank, time_major)

    def force_batch(self, samples, horizontal=False):
        return tuple([c.force_batch(samples[i])[0] for i, c in enumerate(self)])

    @property
    def shape(self):
        return tuple([c.shape for c in self])

    def get_shape(self, with_batch_rank=False, with_time_rank=False, time_major=None, with_category_rank=False):
        return tuple([c.get_shape(
            with_batch_rank=with_batch_rank, with_time_rank=with_time_rank, time_major=time_major,
            with_category_rank=with_category_rank
        ) for c in self])

    @property
    def rank(self):
        return tuple([c.rank for c in self])

    @property
    def flat_dim(self):
        return np.sum([c.flat_dim for c in self])

    @property
    def dtype(self):
        return DataOpTuple([c.dtype for c in self])

    def get_variable(self, name, is_input_feed=False, add_batch_rank=None, add_time_rank=None, time_major=None,
                     **kwargs):
        return DataOpTuple(
            [subspace.get_variable(
                name+"/"+str(i), is_input_feed=is_input_feed, add_batch_rank=add_batch_rank,
                add_time_rank=add_time_rank, time_major=time_major, **kwargs
            ) for i, subspace in enumerate(self)]
        )

    def _flatten(self, mapping, custom_scope_separator, scope_separator_at_start, return_as_dict_space, scope_, list_):
        # Iterate through this Tuple.
        scope_ += (custom_scope_separator if len(scope_) > 0 or scope_separator_at_start else "") + FLAT_TUPLE_OPEN
        for i, component in enumerate(self):
            component.flatten(
                mapping, custom_scope_separator, scope_separator_at_start, return_as_dict_space,
                scope_ + str(i) + FLAT_TUPLE_CLOSE, list_
            )

    def sample(self, size=None, fill_value=None, horizontal=False):
        if horizontal:
            return np.array([tuple(subspace.sample(fill_value=fill_value) for subspace in self)] * (size or 1))
        else:
            return tuple(x.sample(size=size, fill_value=fill_value) for x in self)

    def zeros(self, size=None):
        return tuple([c.zeros(size=size) for i, c in enumerate(self)])

    def contains(self, sample):
        return isinstance(sample, (tuple, list, np.ndarray)) and len(self) == len(sample) and \
               all(c.contains(xi) for c, xi in zip(self, sample))

    def map(self, mapping):
        flattened_self = self.flatten(mapping=mapping)
        return Tuple(
            unflatten_op(flattened_self),
            add_batch_rank=self.has_batch_rank, add_time_rank=self.has_time_rank, time_major=self.time_major
        )

    def __repr__(self):
        return "Tuple({})".format(tuple([cmp.__repr__() for cmp in self]))

    def __eq__(self, other):
        return tuple.__eq__(self, other)
