# rules/__init__.py


import collections
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
    collections.MutableMapping = collections.abc.MutableMapping

from .base_rules import Person, BaseRules

import importlib
import pkgutil
import os

__all__ = ["Person", "BaseRules"]

pkg_dir = os.path.dirname(__file__)
for finder, name, ispkg in pkgutil.iter_modules([pkg_dir]):
    if name in ("base_rules", "__pycache__"):
        continue
    module = importlib.import_module(f"rules.{name}")
    for attr in dir(module):
        if attr.lower().endswith("rules"):
            cls = getattr(module, attr)
            __all__.append(attr)
            globals()[attr] = cls


