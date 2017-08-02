# -*- coding: utf-8 -*-
import numpy as np
from numpy import fft
import pyopencv as cv
import matplotlib.pyplot as plt


N = 256
img = cv.imread("lena_full.jpg")
img2 = cv.Mat()
cv.cvtColor(img, img2, cv.CV_BGR2GRAY)
img = cv.Mat()
cv.resize(img2, img, cv.Size(N, N))


fimg = fft.fft2(img[:])
mag_img = np.log10(np.abs(fimg))
shift_mag_img = fft.fftshift(mag_img)


rects = [(80,125,85,130),(90,90,95,95),
         (150, 10, 250, 250), (110, 110, 146, 146)]
         
filtered_results = []
for i, (x0, y0, x1, y1) in enumerate(rects):
    mask = np.zeros((N, N), dtype=np.bool) 
    mask[x0:x1+1, y0:y1+1] = True 
    mask[N-x1:N-x0+1, N-y1:N-y0+1] = True 
    mask = fft.fftshift(mask) 
    fimg2 = fimg * mask  
    filtered_img = fft.ifft2(fimg2).real 
    filtered_results.append(filtered_img)
    

### 绘图部分 ###    
plt.subplot(231)
plt.imshow(mag_img, cmap=plt.cm.gray)
plt.subplot(232)
plt.imshow(shift_mag_img, cmap=plt.cm.gray)    

ax = plt.gca()
for i, (x0, y0, x1, y1) in enumerate(rects):
    r = plt.Rectangle((x0, y0), x1-x0, y1-y0, alpha=0.2)
    ax.add_artist(r)
    plt.text((x0+x1)/2, (y0+y1)/2, str(i+1), color="white",
        transform=ax.transData, ha="center", va="center", alpha=0.8)

for i, result in enumerate(filtered_results):
    plt.subplot(230+i+3)
    plt.imshow(result, cmap=plt.cm.gray)

for ax in plt.gcf().axes:
    ax.set_axis_off()
    
plt.subplots_adjust(0.01, 0.01, 0.99, 0.99, 0.02, 0.02)
plt.show()
