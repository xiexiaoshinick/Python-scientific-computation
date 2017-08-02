# -*- coding: utf-8 -*-
from distutils.core import *
from distutils import sysconfig
import numpy

demo_module = Extension(
    '_demo',
    ['demo.i', 'demo.cpp'],
    include_dirs = [numpy.get_include()],
    swig_opts=["-c++"]
)

setup(
    name = 'demo',
    version = '1.0',
    author      = "SWIG Docs",
    description = """SWIG + NumPy demo""",
    ext_modules = [demo_module],
    py_modules = ["demo"]
)