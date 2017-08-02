# -*- coding: utf-8 -*-
"""
setup.py file for SWIG example
"""

from distutils.core import *

demo_module = Extension(
    '_demo',
    ['demo.i', 'demo.cpp'],
    swig_opts=["-c++"]
)

setup(
    name = 'demo',
    version = '0.1',
    author      = "HYRY Studio",
    description = """Simple swig demo""",
    ext_modules = [demo_module],
    py_modules = ["demo"]
)