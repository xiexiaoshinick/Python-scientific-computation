# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [
    Extension("mylib", ["mylib.pyx"],
        include_dirs = [numpy.get_include(),'.']),
    Extension("cython_matmul", ["cython_matmul.pyx"],
        include_dirs = [numpy.get_include(),'.'])        
]

setup(
  name = 'my cython library test',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)