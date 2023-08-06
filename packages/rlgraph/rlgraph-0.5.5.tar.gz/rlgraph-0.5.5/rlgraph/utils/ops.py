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

import re
from collections import OrderedDict

# Defines how to generate auto-keys for flattened Tuple-Space items.
# _T\d+_
FLAT_TUPLE_OPEN = "_T"
FLAT_TUPLE_CLOSE = "_"
FLATTEN_SCOPE_PREFIX = "/"


class TraceContext(object):
    """
    Contains static trace context. Used to reconstruct data-flow in cases where normal
    stack-frame inspection fails, e.g. because when calling from within a lambda.
    """

    # Prior caller.
    PREV_CALLER = None

    # Define by run build tracing.
    DEFINE_BY_RUN_CONTEXT = None

    # Is there an active call context?
    ACTIVE_CALL_CONTEXT = False
    CONTEXT_START = None


class DataOp(object):
    """
    The basic class for any Socket-held operation or variable, or collection thereof.
    Each Socket (in or out) holds either one DataOp or a set of alternative DataOps.
    """
    def map(self, mapping):
        """
        A convenience method for mapping all (flattened) contents (primitive DataOps) of primitive
        as well as ContainerDataOps to something else.

        Args:
            mapping (callable): The mapping function taking a key and a DataOp as args and returning another DataOp.

        Returns:
            DataOp: The mapped DataOp (or ContainerDataOp).
        """
        return mapping("", self)


class SingleDataOp(DataOp):
    """
    A placeholder class for a simple (non-container) Tensor going into a GraphFunction or coming out of a GraphFunction,
    or a tf.no_op-like item.
    """
    pass


class ContainerDataOp(DataOp):
    """
    A placeholder class for any DataOp that's not a SingleDataOp, but a (possibly nested) container structure
    containing SingleDataOps as leave nodes.
    """
    def flat_key_lookup(self, flat_key, custom_scope_separator=None):
        """
        Returns an element within this DataOp following a given flat-key.

        Args:
            flat_key (str): The flat key to lookup (e.g. "/a/_T0_/b").
            custom_scope_separator (Optional[str]): The scope separator used in the flat-key. It's usually "/".

        Returns:
            any: The looked up item or None if nothing found.
        """
        return flat_key_lookup(self, flat_key, custom_scope_separator=custom_scope_separator)


class DataOpDict(ContainerDataOp, dict):
    """
    A hashable dict that's used to make (possibly nested) dicts of SingleDataOps hashable, so that
    we can store them in sets and use them as lookup keys in other dicts.
    Dict() Spaces produce DataOpDicts when methods like `get_variable` are called on them.
    """
    def map(self, mapping):
        """
        Maps this DataOpDict via a given mapping function to another, corresponding DataOpDict where all individual
        SingleDataOps are mapped to new SingleDataOps.

        Args:
            mapping (callable): The mapping function to use on each SingeDataOp.

        Returns:
            DataOpDict: A copy of this DataOpDict, but all SingeDataOps are mapped via the given mapping function.
        """
        flattened_self = flatten_op(self)
        ret = {}
        for key, value in flattened_self.items():
            ret[key] = mapping(key, value)
        return DataOpDict(dict(unflatten_op(ret)))

    def __hash__(self):
        """
        Hash based on sequence of sorted items (keys are all strings, values are always other DataOps).
        """
        return hash(tuple(sorted(self.items())))


class DataOpTuple(ContainerDataOp, tuple):
    """
    A simple wrapper for a (possibly nested) tuple that contains other DataOps.
    """
    def map(self, mapping):
        """
        Maps this DataOpTuple via a given mapping function to another, corresponding DataOpTuple where all individual
        SingleDataOps are mapped to new SingleDataOps.

        Args:
            mapping (callable): The mapping function to use on each SingeDataOp.

        Returns:
            DataOpTuple: A copy of this DataOpTuple, but all SingeDataOps are mapped via the given mapping function.
        """
        flattened_self = flatten_op(self)
        ret = {}
        for key, value in flattened_self.items():
            ret[key] = mapping(key, value)
        return DataOpTuple(*unflatten_op(ret))

    def __new__(cls, *components):
        if isinstance(components[0], (list, tuple)):
            assert len(components) == 1
            components = components[0]

        return tuple.__new__(cls, components)


class FlattenedDataOp(DataOp, OrderedDict):
    """
    An OrderedDict-type placeholder class that only contains str as keys and SingleDataOps
    (as opposed to ContainerDataOps) as values.
    """
    # TODO: enforce str as keys?
    pass


def flatten_op(
        op, key_scope="", op_tuple_list=None, custom_scope_separator=None, scope_separator_at_start=True, mapping=None,
        flatten_alongside=None
):
    """
    Flattens a single ContainerDataOp or a native python dict/tuple into a FlattenedDataOp with auto-key generation.

    Args:
        op (Union[ContainerDataOp,dict,tuple]): The item to flatten.
        key_scope (str): The recursive scope for auto-key generation.
        op_tuple_list (list): The list of tuples (key, value) to be converted into the final FlattenedDataOp.

        custom_scope_separator (str): The separator to use in the returned dict for scopes.
            Default: '/'.

        scope_separator_at_start (bool): Whether to add the scope-separator also at the beginning.
            Default: False.

        mapping (Optional[callable]): An optional mapping function for op (and all nested ops) to be passed through.

        flatten_alongside (Optional[dict]): If given, flatten only according to this dictionary, not any further down
            the nested input structure of `op`. This is useful to flatten e.g. along some action-space, but not
            further down (e.g. into the tuple of a distribution's parameters).

    Returns:
        FlattenedDataOp: The flattened representation of the op.
    """
    ret = False

    # Are we in the non-recursive (first) call?
    if op_tuple_list is None:
        # Flatten a SingleDataOp -> return FlattenedDataOp with only-key="".
        # OR: flatten_alongside something, and that something is not flattened (its only key is "").
        if not isinstance(op, (ContainerDataOp, dict, tuple)) or \
                (flatten_alongside is not None and len(flatten_alongside) == 1 and "" in flatten_alongside):
            return FlattenedDataOp([("", op)])
        op_tuple_list = []
        ret = True

    if mapping is not None:
        op = mapping(op)

    flatten_scope_prefix = custom_scope_separator or FLATTEN_SCOPE_PREFIX

    if isinstance(op, dict):
        if scope_separator_at_start:
            key_scope += flatten_scope_prefix
        else:
            key_scope = ""
        for key in sorted(op.keys()):
            # Make sure we have no double slashes from flattening an already FlattenedDataOp.
            scope = (key_scope[:-1] if len(key) == 0 or key[0] == "/" else key_scope) + key
            # If current flat-key is already in `alongside` structure, stop the flattening here.
            if flatten_alongside is not None and scope in flatten_alongside:
                op_tuple_list.append((scope, op[key]))
            else:
                flatten_op(
                        op[key], key_scope=scope, op_tuple_list=op_tuple_list, scope_separator_at_start=True,
                        mapping=mapping, flatten_alongside=flatten_alongside
                )
    elif isinstance(op, tuple):
        if scope_separator_at_start:
            key_scope += flatten_scope_prefix + FLAT_TUPLE_OPEN
        else:
            key_scope += "" + FLAT_TUPLE_OPEN
        for i, c in enumerate(op):
            # If current flat-key is already in `alongside` structure, stop the flattening here.
            if flatten_alongside is not None and key_scope in flatten_alongside:
                op_tuple_list.append((key_scope, c))
            else:
                flatten_op(
                    c, key_scope=key_scope + str(i) + FLAT_TUPLE_CLOSE, op_tuple_list=op_tuple_list,
                    scope_separator_at_start=True, mapping=mapping, flatten_alongside=flatten_alongside
                )
    else:
        op_tuple_list.append((key_scope, op))

    # Non recursive (first) call -> Return the final FlattenedDataOp.
    if ret:
        return FlattenedDataOp(op_tuple_list)


def unflatten_op(op, custom_scope_separator=None):
    """
    Takes a FlattenedDataOp with auto-generated keys and returns the corresponding
    unflattened DataOp.
    If the only key in the input FlattenedDataOp is "", it returns the SingleDataOp under
    that key.

    Args:
        op (dict): The item to be unflattened (re-nested) into any DataOp. Usually a FlattenedDataOp, but can also
            be a plain dict.

    Returns:
        DataOp: The unflattened (re-nested) item.
    """
    # Special case: FlattenedDataOp with only 1 SingleDataOp (key="").
    if len(op) == 1 and "" in op:
        return op[""]

    # Normal case: FlattenedDataOp that came from a ContainerItem.
    base_structure = None

    flatten_scope_prefix = custom_scope_separator or FLATTEN_SCOPE_PREFIX

    op_names = sorted(op.keys())
    for op_name in op_names:
        op_val = op[op_name]
        parent_structure = None
        parent_key = None
        current_structure = None
        op_type = None

        # N.b. removed this because we do not prepend / any more before first key.
        if op_name.startswith(flatten_scope_prefix):
            op_name = op_name[1:]
        op_key_list = op_name.split("/")  # skip 1st char (/)
        for sub_key in op_key_list:
            mo = re.match(r'^{}(\d+){}$'.format(FLAT_TUPLE_OPEN, FLAT_TUPLE_CLOSE), sub_key)
            if mo:
                op_type = list
                idx = int(mo.group(1))
            else:
                op_type = DataOpDict
                idx = sub_key

            if current_structure is None:
                if base_structure is None:
                    base_structure = [None] if op_type == list else DataOpDict()
                current_structure = base_structure
            elif parent_key is not None:
                # DEBUG:
                #if isinstance(parent_structure, list) and len(parent_structure) <= parent_key:
                #    print("WARNING: parent_structure={} parent_key={} to-be-flattened-op={}".format(parent_structure, parent_key, op))
                # END: DEBUG

                if (isinstance(parent_structure, list) and (parent_structure[parent_key] is None)) or \
                        (isinstance(parent_structure, DataOpDict) and parent_key not in parent_structure):
                    current_structure = [None] if op_type == list else DataOpDict()
                    parent_structure[parent_key] = current_structure
                else:
                    current_structure = parent_structure[parent_key]
                    if op_type == list and len(current_structure) == idx:
                        current_structure.append(None)

            parent_structure = current_structure
            parent_key = idx
            if isinstance(parent_structure, list) and len(parent_structure) == parent_key:
                parent_structure.append(None)

        if op_type == list and len(current_structure) == parent_key:
            current_structure.append(None)
        current_structure[parent_key] = op_val

    # Deep conversion from list to tuple.
    return deep_tuple(base_structure)


def flat_key_lookup(container, flat_key, default=None, custom_scope_separator=None):
    """
    Looks up a flattened key (a sequence of simple lookups inside a deep nested dict/tuple)
    and returns the found item. Returns a  default value if no item under that flat-key was found.

    Args:
        container (any): The (non-flattened) structure (can be a dict, a ).
        flat_key (str): The flat key to look for.
        default (any): The default value if nothing was found. Default: None.
        custom_scope_separator (Optional[str]): The scope separator that's used in the flat-key string.
            Default: Value of `FLATTEN_SCOPE_PREFIX`.

    Returns:
        any: The found item under the flat key or a default value if nothing was found.
    """
    flatten_scope_prefix = custom_scope_separator or FLATTEN_SCOPE_PREFIX

    # Ignore starting scope-separators.
    if flat_key.startswith(flatten_scope_prefix):
        flat_key = flat_key[1:]

    key_sequence = flat_key.split(flatten_scope_prefix)
    result = container
    for key in key_sequence:
        mo = re.match(r'^{}(\d+){}$'.format(FLAT_TUPLE_OPEN, FLAT_TUPLE_CLOSE), key)
        # Tuple.
        if mo is not None:
            slot = int(mo.group(1))
            if len(result) > slot and default is not None:
                return default
            result = result[slot]
        # Dict.
        else:
            if key not in result and default is not None:
                return default
            result = result[key]
    return result


def deep_tuple(x):
    """
    Converts all lists inside the input into a DataOpTuple.

    Args:
        x (list): The arbitrarily nested input structure to be converted.

    Returns:
        any: The corresponding new structure for x.
    """
    # A list -> convert to DataOpTuple.
    if isinstance(x, list):
        return DataOpTuple(list(map(deep_tuple, x)))
    # A dict -> leave type as is and keep converting recursively.
    elif isinstance(x, dict):
        # type(x) b/c x could be DataOpDict as well.
        return type(x)(dict(map(lambda i: (i[0], deep_tuple(i[1])), x.items())))
    # A primitive -> keep as is.
    else:
        return x


def is_constant(op):
    return type(op).__name__ in ["int", "float", "bool", "ndarray"]
