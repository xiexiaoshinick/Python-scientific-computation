# -*- coding: utf-8 -*-

import pyopencv as cv
import numpy as np

img = cv.imread("fruits_section.jpg") 
img_hsv = cv.Mat()
cv.cvtColor(img, img_hsv, cv.CV_BGR2HSV) 

channels = cv.vector_int([0, 1])
result = cv.MatND()

r = cv.vector_float32([0, 256])
ranges = cv.vector_vector_float32([r, r])

cv.calcHist(cv.vector_Mat([img_hsv]), channels, cv.Mat(),  
            result, cv.vector_int([40, 40]), ranges) 

result[:] /= np.max(result[:]) / 255 
2###
img2 = cv.imread("fruits.jpg") 
img_hsv2 = cv.Mat()
cv.cvtColor(img2, img_hsv2, cv.CV_BGR2HSV)

img_bp = cv.Mat()
cv.calcBackProject(cv.vector_Mat([img_hsv2]), 
                   channels=channels, 
                   hist=result, 
                   backProject=img_bp, 
                   ranges = ranges) 
3###
img_th = cv.Mat()
cv.threshold(img_bp, img_th, 180, 255, cv.THRESH_BINARY) 
4###
struct = np.ones((3,3), np.uint8)
struct_mat = cv.asMat(struct, force_single_channel=True)
img_mp = cv.Mat()

cv.morphologyEx(img_th, img_mp, cv.MORPH_CLOSE, struct_mat, iterations=5) 


import pylab as pl
import matplotlib.cm as cm
pl.subplot(231)
pl.imshow(img[:,:,::-1])
pl.subplot(232)
pl.imshow(img2[:,:,::-1])
pl.subplot(233)
pl.imshow(result[:], cmap=cm.gray)
pl.subplot(234)
pl.imshow(img_bp[:], cmap=cm.gray)
pl.subplot(235)
pl.imshow(img_th[:], cmap=cm.gray)
pl.subplot(236)
pl.imshow(img_mp[:], cmap=cm.gray)

for axe in pl.gcf().axes:
    axe.set_axis_off()
pl.show()
