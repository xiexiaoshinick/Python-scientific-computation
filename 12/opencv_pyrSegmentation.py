# -*- coding: utf-8 -*-
import pyopencv as cv
import matplotlib.pyplot as plt


img = cv.imread("fruits.jpg")
threshold2 = [10, 30, 60]
for i, th2 in enumerate(threshold2):
    img2 = img.clone()
    storage = cv.createMemStorage(0)    
    result = cv.pyrSegmentation(img, img2, storage, 4, 200, th2)
    
    plt.subplot(100+len(threshold2)*10+i+1)
    plt.imshow(img2[:,:,::-1])
    plt.gca().set_axis_off()
    
plt.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)    
plt.show()