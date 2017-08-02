# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.jpg")

plt.subplot(121)
for i in xrange(3):
    hist, x = np.histogram(img[:,:,i].flatten(), bins=256, range=(0,256)) 
    plt.plot(0.5*(x[:-1]+x[1:]), hist, label="Ch %d" % i, lw=i+1)
plt.legend(loc="upper left") 
plt.xlim((0,256))  

hist2, x2, y2 = np.histogram2d(  
    img[:,:,0].flatten(), img[:,:,2].flatten(), 
    bins=(100,100), range=[(0,256),(0,256)])

plt.subplot(122)    
plt.imshow(hist2, extent=(0,256,0,256), origin="lower")    
plt.ylabel("Ch0")
plt.xlabel("Ch2")
plt.show()    
