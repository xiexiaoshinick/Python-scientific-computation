# -*- coding: utf-8 -*-
"""
生成水波动画文件
"""

import numpy as np
import pyopencv as cv

class WaterWave(object): 
    def __init__(self, w, h, N, damping):
        self.width, self.height = w, h
        self.N = N
        self.damping = damping
        self.w1 = np.zeros((self.height, self.width), dtype=np.float)
        self.w2 = np.zeros((self.height, self.width), dtype=np.float)
        self.tmpbuf = np.zeros((self.height-2, self.width-2), dtype=np.float)
        self.bmp = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        h, w = self.height - 2, self.width - 2
        self.slice = [(slice(i,h+i), slice(j,w+j)) 
            for i in xrange(3) for j in xrange(3) if i!=1 or j!=1]

    def step(self):
        y = np.random.randint(1, self.height-1, self.N)
        x = np.random.randint(1, self.width-1, self.N)
        self.w1[y, x] = np.random.random(self.N) * 120 + 128
        
        self.tmpbuf[:] = 0
        for s in self.slice:
            self.tmpbuf += self.w1[s]
            
        self.tmpbuf /= 4
        self.w2[1:-1, 1:-1] *= -1
        self.w2[1:-1, 1:-1] += self.tmpbuf
        self.w2 *= self.damping
        self.w1, self.w2 = self.w2, self.w1
        
        self.bmp[:,:,0] = self.w1 + 128
        self.bmp[:,:,1] = self.bmp[:,:,0] - (self.bmp[:,:,0] >> 2)
        self.bmp[:,:,2] = self.bmp[:,:,1]
        return self.bmp

WIDTH, HEIGHT = 640, 480
video = cv.VideoWriter() 
#video.open("waterwave.avi", cv.CV_FOURCC(*"DIB "), 30, cv.Size2i(WIDTH, HEIGHT)) 
video.open("waterwave.avi", cv.CV_FOURCC(*"ffds"), 30, cv.Size2i(WIDTH, HEIGHT)) 
water = WaterWave(WIDTH, HEIGHT, 100, 0.97)
import time
start = time.clock()
for i in xrange(200):
    if i % 30 == 0: print i
    r = water.step()
    mat = cv.asMat(r)
    video << mat 
del video 
print time.clock() - start