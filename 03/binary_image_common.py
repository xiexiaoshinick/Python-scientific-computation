# -*- coding: utf-8 -*-
"""
演示图像处理的一些辅助函数。
"""
import numpy as np
import pylab as pl
import Image, ImageDraw, ImageFont

def make_text_image(width, height, x, y, size, th, text):
    img = Image.new("L", (width, height))
    font = ImageFont.truetype("arial.ttf", size)
    draw = ImageDraw.Draw(img)
    draw.text((x,y), text, font=font, fill=255)
    return np.asarray(img)>th

def expand_image(img, value, out=None, size = 10):
    if out is None:
        w, h = img.shape
        out = np.zeros((w*size, h*size),dtype=np.uint8)
    
    tmp = np.repeat(np.repeat(img,size,0),size,1)
    out[:,:] = np.where(tmp, value, out)
    out[::size,:] = 0
    out[:,::size] = 0
    return out
    
def show_image(*imgs): 
    for idx, img in enumerate(imgs):
        subplot = 101 + len(imgs)*10 +idx
        pl.subplot(subplot)
        pl.imshow(img, cmap=pl.cm.gray)   
        pl.gca().set_axis_off()    
    pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)        