# -*- coding: utf-8 -*-
"""
细线化算法的动画演示。
"""
import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib
matplotlib.use("WXAgg")
import matplotlib.pyplot as pl
import scipy.ndimage.morphology as m
import time

def make_text_image(width, height, x, y, size, text):
    img = Image.new("L", (width, height))
    font = ImageFont.truetype("arial.ttf", size)
    draw = ImageDraw.Draw(img)
    draw.text((x,y), text, font=font, fill=255)
    return np.asarray(img)>127

a = make_text_image(300, 100, 5, 5, 80, "HELLO")

fig = pl.figure()
ax = fig.add_subplot(211)
ax.imshow(a, cmap=pl.cm.gray, interpolation="nearest")
ax = fig.add_subplot(212)

h1 = np.array([[0, 0, 0],[0, 1, 0],[1, 1, 1]]) 
m1 = np.array([[1, 1, 1],[0, 0, 0],[0, 0, 0]]) 
h2 = np.array([[0, 0, 0],[1, 1, 0],[0, 1, 0]]) 
m2 = np.array([[0, 1, 1],[0, 0, 1],[0, 0, 0]]) 

hit_list = [] 
miss_list = []

for k in range(4):
    hit_list.append(np.rot90(h1, k))
    hit_list.append(np.rot90(h2, k))
    miss_list.append(np.rot90(m1, k))
    miss_list.append(np.rot90(m2, k))    
 
def update_data():
    global last, a
    last = a
    while True:
        last = a
        for hit, miss in zip(hit_list, miss_list): 
            hm = m.binary_hit_or_miss(a, hit, miss)
            a = np.logical_and(a, np.logical_not(hm))
            try:
                pl.imshow(a, cmap=pl.cm.gray, interpolation="nearest")        
                fig.canvas.draw_idle()
                yield
            except:
                import sys
                sys.exit()
        if np.abs(last - a).max() == 0: 
            yield

aa = update_data()
def update(idleevent):
    aa.next()
    time.sleep(0.1)

import wx
wx.EVT_IDLE(wx.GetApp(), update)
pl.show()
pl.subplot(212)
pl.imshow(a, cmap=pl.cm.gray, interpolation="nearest")
pl.show()
