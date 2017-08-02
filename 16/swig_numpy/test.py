# -*- coding: utf-8 -*-
import numpy as np
import demo

print "----- ARGOUT_ARRAY1, DIM1 -----"
print demo.drange(10)

print "----- ARGOUT_ARRAY2[3][3] -----"
print demo.rot2d(np.pi/4)

print "----- IN_ARRAY1, DIM1 -----"
print demo.sum_power([1,2,3])
x = np.arange(10)
print demo.sum_power(x[::2])

print "----- INPLACE_ARRAY1, DIM1 -----"
a = np.arange(10.0)
demo.power(a)
print a
