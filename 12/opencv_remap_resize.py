# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np

img = cv.imread("lena.jpg")
size = img.size()
w, h = size
img2 = cv.Mat()
map1, map2 = np.meshgrid(
    np.linspace(0,w*2,w).astype(np.float32),
    np.linspace(0,h*2,h).astype(np.float32),
)
map1 = cv.asMat(map1)
map2 = cv.asMat(map2)
cv.remap(img, img2, map1, map2, cv.INTER_LINEAR)

cv.namedWindow( "Remap Resize", cv.CV_WINDOW_AUTOSIZE )
cv.imshow("Remap Resize", img2)
cv.waitKey(0)

