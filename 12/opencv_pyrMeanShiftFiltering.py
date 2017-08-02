# -*- coding: utf-8 -*-
import pyopencv as cv
import matplotlib.pyplot as plt

img = cv.imread("fruits.jpg")

#srs = [20, 40, 80]
srs = [20]
for i, sr in enumerate(srs):
    img2 = img.clone()
    result = cv.pyrMeanShiftFiltering(img, img2, 20, sr, 1)
    plt.subplot(100+len(srs)*10+i+1)
    plt.imshow(img2[:,:,::-1])
    plt.gca().set_axis_off()
    
plt.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)    
plt.show()