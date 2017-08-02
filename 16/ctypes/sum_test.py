# -*- coding: utf-8 -*-
from ctypes import *
import numpy as np

sum_test = np.ctypeslib.load_library("sum_test", ".")

sum_test.mysum.restype = c_double
sum_test.mysum.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    c_long
]

sum_test.mysum2.restype = c_double
sum_test.mysum2.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=2),
    POINTER(c_int),
    POINTER(c_int)
]

def mysum2(x):
    return sum_test.mysum2(x, x.ctypes.strides, x.ctypes.shape)

if __name__ == "__main__":   
    x = np.arange(1, 101, 1.0)
    print sum_test.mysum(x, len(x))

    x = np.arange(1, 101, 1.0).reshape((20, 5))
    print mysum2(x)