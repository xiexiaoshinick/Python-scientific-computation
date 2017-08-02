# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
import time 

img = cv.asMat(np.random.rand(1000,1000)) 

row = cv.getGaussianKernel(7, -1) 
col = cv.getGaussianKernel(5, -1)

kernel = cv.asMat(np.dot(col[:], row[:].T), force_single_channel=True) 

img2 = cv.Mat()
img3 = cv.Mat()

start = time.clock()
cv.filter2D(img, img2, -1, kernel) 
print "filter2D:", time.clock() - start

start = time.clock()
cv.sepFilter2D(img, img3, -1, row, col) 
print "sepFilter3D:", time.clock() - start

print "error=", np.max(np.abs(img2[:] - img3[:])) 