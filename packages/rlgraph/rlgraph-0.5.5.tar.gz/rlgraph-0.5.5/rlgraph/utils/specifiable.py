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

import importlib
import json
import logging
import os
import re
from copy import deepcopy
from functools import partial

import yaml

from rlgraph.utils.rlgraph_errors import RLGraphError
from rlgraph.utils.util import default_dict, force_list


class Specifiable(object):
    """
    Members of this class support the methods from_file, from_spec and from_mixed.
    """
    # An optional python dict with supported str-to-ctor mappings for this class.
    __lookup_classes__ = None
    # An optional default constructor to use without any arguments in case `spec` is None
    # and args/kwargs are both empty. This may be a functools.partial object.
    __default_constructor__ = None

    # TODO: Remove from here. Only Specifyables that really need a Logger should have this. Creates problems when
    # TODO: deepcopying.
    logger = logging.getLogger(__name__)

    # Analogous to: http://effbot.org/pyfaq/how-do-i-get-a-list-of-all-instances-of-a-given-class.htm
    #_instances = list()

    def __init__(self):
        pass
        #self._instances.append(weakref.ref(self))

    @classmethod
    def from_spec(cls, spec=None, **kwargs):
        """
        Uses the given spec to create an object.
        If `spec` is a dict, an optional "type" key can be used as a "constructor hint" to specify a certain class
        of the object.
        If `spec` is not a dict, `spec`'s value is used directly as the "constructor hint".

        The rest of `spec` (if it's a dict) will be used as kwargs for the (to-be-determined) constructor.
        Additional keys in **kwargs will always have precedence (overwrite keys in `spec` (if a dict)).
        Also, if the spec-dict or **kwargs contains the special key "_args", it will be popped from the dict
        and used as *args list to be passed separately to the constructor.

        The following constructor hints are valid:
        - None: Use `cls` as constructor.
        - An already instantiated object: Will be returned as is; no constructor call.
        - A string or an object that is a key in `cls`'s `__lookup_classes__` dict: The value in `__lookup_classes__`
            for that key will be used as the constructor.
        - A python callable: Use that as constructor.
        - A string: Either a json filename or the name of a python module+class (e.g. "rlgraph.components.Component")
            to be Will be used to

        Args:
            spec (Optional[dict]): The specification dict.

        Keyword Args:
            kwargs (any): Optional possibility to pass the c'tor arguments in here and use spec as the type-only info.
                Then we can call this like: from_spec([type]?, [**kwargs for ctor])
                If `spec` is already a dict, then `kwargs` will be merged with spec (overwriting keys in `spec`) after
                "type" has been popped out of `spec`.
                If a constructor of a Specifiable needs an *args list of items, the special key `_args` can be passed
                inside `kwargs` with a list type value (e.g. kwargs={"_args": [arg1, arg2, arg3]}).

        Returns:
            The object generated from the spec.
        """
        # specifiable_type is already a created object of this class -> Take it as is.
        if isinstance(spec, cls):
            return spec

        # `specifiable_type`: Indicator for the Specifiable's constructor.
        # `ctor_args`: *args arguments for the constructor.
        # `ctor_kwargs`: **kwargs arguments for the constructor.
        # Copy so caller can reuse safely.
        spec = deepcopy(spec)
        if isinstance(spec, dict):
            if "type" in spec:
                specifiable_type = spec.pop("type", None)
            else:
                specifiable_type = None
            ctor_kwargs = spec
            ctor_kwargs.update(kwargs)  # give kwargs priority
        else:
            specifiable_type = spec
            if specifiable_type is None and "type" in kwargs:
                specifiable_type = kwargs.pop("type")
            ctor_kwargs = kwargs
        # Special `_args` field in kwargs for *args-utilizing constructors.
        ctor_args = force_list(ctor_kwargs.pop("_args", []))

        # Figure out the actual constructor (class) from `type_`.
        # None: Try __default__object (if no args/kwargs), only then constructor of cls (using args/kwargs).
        if specifiable_type is None:
            # We have a default constructor that was defined directly by cls (not by its children).
            if cls.__default_constructor__ is not None and ctor_args == [] and \
                    (not hasattr(cls.__bases__[0], "__default_constructor__") or
                     cls.__bases__[0].__default_constructor__ is None or
                     cls.__bases__[0].__default_constructor__ is not cls.__default_constructor__
                    ):
                constructor = cls.__default_constructor__
                # Default partial's keywords into ctor_kwargs.
                if isinstance(constructor, partial):
                    kwargs = default_dict(ctor_kwargs, constructor.keywords)
                    constructor = partial(constructor.func, **kwargs)
                    ctor_kwargs = {} # erase to avoid duplicate kwarg error
            # Try our luck with this class itself.
            else:
                constructor = cls
        # Try the __lookup_classes__ of this class.
        else:
            constructor = cls.lookup_class(specifiable_type)

            # Found in cls.__lookup_classes__.
            if constructor is not None:
                pass
            # Python callable.
            elif callable(specifiable_type):
                constructor = specifiable_type
            # A string: Filename or a python module+class.
            elif isinstance(specifiable_type, str):
                if re.search(r'\.(yaml|yml|json)$', specifiable_type):
                    return cls.from_file(specifiable_type, *ctor_args, **ctor_kwargs)
                elif specifiable_type.find('.') != -1:
                    module_name, function_name = specifiable_type.rsplit(".", 1)
                    module = importlib.import_module(module_name)
                    constructor = getattr(module, function_name)
                else:
                    raise RLGraphError(
                        "ERROR: String specifier ({}) in from_spec must be a filename, a module+class, or a key "
                        "into {}.__lookup_classes__!".format(specifiable_type, cls.__name__)
                    )

        if not constructor:
            raise RLGraphError("Invalid type: {}".format(specifiable_type))

        # Create object with inferred constructor.
        specifiable_object = constructor(*ctor_args, **ctor_kwargs)
        assert isinstance(specifiable_object, constructor.func if isinstance(constructor, partial) else constructor)

        return specifiable_object

    @classmethod
    def from_file(cls, filename, *args, **kwargs):
        """
        Create object from spec saved in filename. Expects json or yaml format.

        Args:
            filename: file containing the spec (json or yaml)

        Keyword Args:
            Used as additional parameters for call to constructor.

        Returns:
            object
        """
        path = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(path):
            raise RLGraphError('No such file: {}'.format(filename))

        with open(path, 'rt') as fp:
            if path.endswith('.yaml') or path.endswith('.yml'):
                spec = yaml.load(fp)
            else:
                spec = json.load(fp)

        # Add possible *args.
        spec["_args"] = args
        return cls.from_spec(spec=spec, **kwargs)

    @classmethod
    def lookup_class(cls, lookup_type):
        if isinstance(cls.__lookup_classes__, dict) and \
            (lookup_type in cls.__lookup_classes__ or (isinstance(lookup_type, str)
             and re.sub(r'[\W_]', '', lookup_type.lower()) in cls.__lookup_classes__)):
            available_class_for_type = cls.__lookup_classes__.get(lookup_type)
            if available_class_for_type is None:
                available_class_for_type = cls.__lookup_classes__[re.sub(r'[\W_]', '', lookup_type.lower())]
            return available_class_for_type
        return None
