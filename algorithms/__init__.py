#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Stores a list of module string names in __all__
import os
import glob
from importlib import import_module
files = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(f)[:-3] for f in files if "__init__" not in f]
modules = {}
for module_name in __all__:
    modules[module_name] = import_module(f"{__name__}.{module_name}")
