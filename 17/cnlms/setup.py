# -*- coding: utf-8 -*-
from distutils.core import *
from distutils import sysconfig
import numpy

module = Extension(
    '_nlms_swig',
    ['cnlms.i', 'cnlms.cpp'],
    include_dirs = [numpy.get_include()],
    swig_opts=["-c++"]
)

setup(
    name = 'nlms_swig',
    version = '1.0',
    author      = "SWIG Docs",
    description = "NLMS algorithm",
    ext_modules = [module],
    py_modules = ["nlms_swig"]
)