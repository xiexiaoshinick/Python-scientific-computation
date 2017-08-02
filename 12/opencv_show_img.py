# -*- coding: utf-8 -*-
import pyopencv as cv
import sys

try:
    filename = sys.argv[1]
except:
    filename = "lena.jpg"
img = cv.imread( filename )
cv.namedWindow("demo1")
cv.imshow("demo1", img)
cv.waitKey(0)