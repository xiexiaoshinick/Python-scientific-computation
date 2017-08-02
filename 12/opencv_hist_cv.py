# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np

img = cv.imread("lena.jpg")
result = cv.MatND()

r = cv.vector_float32([0, 256]) 
ranges = cv.vector_vector_float32([r, r])

cv.calcHist(cv.vector_Mat([img]), 
    channels = cv.vector_int([0, 1]), 
    mask = cv.Mat(), 
    hist = result, 
    histSize=cv.vector_int([30, 20]), 
    ranges=ranges
    )
    
hist, _x, _y = np.histogram2d(img[:,:,0].flatten(), img[:,:,1].flatten(), 
    bins=(30,20), range=[(0,256),(0,256)])

print np.all(hist == result[:]) 
