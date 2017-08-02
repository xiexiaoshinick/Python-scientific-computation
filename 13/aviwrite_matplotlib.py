# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pyopencv as cv

y, x = np.ogrid[-2:2:300j,-2:2:300j]
z = (x**2+y**2-1)**3 - x**2*y**3

fig = plt.figure(figsize=(4,4))
w, h = fig.bbox.width, fig.bbox.height

video = None
for level in np.linspace(-0.2,0.2,101):
    fig.clear() 
    axe = fig.add_subplot(111, aspect=1)
    plt.contour(x.ravel(), y.ravel(), z, levels=[level])
    plt.title("level=%5.3f" % level)
    axe.xaxis.set_ticks([])
    axe.yaxis.set_ticks([])
    fig.canvas.draw() 
    buf = fig.canvas.buffer_rgba(0,0) 
    array = np.frombuffer(buf, np.uint8) 
    array.shape = h, w, 4
    
    if not video:
        video = cv.VideoWriter()
        size = cv.Size2i(int(w),int(h))
        #video.open("contour.avi", cv.CV_FOURCC(*"DIB "), 30, size)
        video.open("contour.avi", cv.CV_FOURCC(*"ffds"), 30, size)
        image = cv.Mat(size, cv.CV_8UC3)
    image[:] = array[:,:,2::-1] 
    video << image
del video
