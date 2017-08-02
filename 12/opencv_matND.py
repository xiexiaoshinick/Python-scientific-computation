# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np

m = np.arange(0, 20).astype(np.uint8)
m.shape = 4,5

n = cv.asMatND(m)

p = n.ndarray

print m
print "------------"
print p

print m.strides
print p.strides
