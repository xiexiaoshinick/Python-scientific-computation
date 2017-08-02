# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np

y, x = np.ogrid[-1:1:250j,-1:1:250j]
z = np.sin(10*np.sqrt(x*x+y*y))*0.5 + 0.5 
np.round(z, decimals=1, out=z) 

img = cv.asMat(z) 

cv.namedWindow("demo1")
cv.imshow("demo1", img)

img2 = cv.Mat() 
cv.Laplacian(img, img2, img.depth(), ksize=3) 

cv.namedWindow("demo2")
cv.imshow("demo2", img2)
cv.waitKey(0)