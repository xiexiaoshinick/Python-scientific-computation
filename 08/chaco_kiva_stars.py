# -*- coding: utf-8 -*-
"""
使用Kiva在NumPy数组上绘制星星
"""

import numpy as np
from enthought.kiva.image import GraphicsContext

import pylab as pl


def star_polygon(x, y, r, theta, n, s): 
    angles = np.arange(0, 2*np.pi+2*np.pi/2/n, 2*np.pi/2/n) + theta
    xs = r * np.cos(angles)
    ys = r * np.sin(angles)
    xs[1::2] *= s
    ys[1::2] *= s
    xs += x
    ys += y
    return np.vstack([xs, ys]).T

def draw_star(gc, x, y, r, c, theta, n, s): 
    gc.save_state()
    gc.set_antialias(True)
    gc.set_stroke_color(c + (0.8,))
    gc.set_fill_color(c + (0.4,))    
    gc.lines(star_polygon(x, y, r, theta, n, s))
    gc.draw_path()
    gc.restore_state()



if __name__ == "__main__":

    img = np.zeros((500,800,4), dtype=np.uint8) 
    img[:,:,:3] = 0 # 全黑的图像
    img[:,:,3] = 255
    gc = GraphicsContext(img) 
    for i in range(1000):
        randint = np.random.randint
        rand = np.random.rand
        draw_star(gc, randint(800), randint(500), randint(5,10),  
            (rand(),rand(),rand()), rand()*2*np.pi, randint(3,9), rand()*0.6+0.1)
    gc.save("stars.png")  
    
    pl.imshow(img)
    pl.axis("off")
    pl.show()
