# -*- coding: utf-8 -*-
"""
演示二值图像的Hit和Miss算法。
"""
from binary_image_common import *
import scipy.ndimage.morphology as m

def hitmiss_demo(a, structure1, structure2):
    global b
    b = m.binary_hit_or_miss(a, structure1, structure2)
    img = expand_image(a, 100)
    return expand_image(b, 255, out=img)

a = make_text_image(15,15,4,-2,16,0,"A")
img1 = expand_image(a, 255)

img2 = hitmiss_demo(a, [[0,0,0],[0,1,0],[1,1,1]], [[1,0,0],[0,0,0],[0,0,0]])
img3 = hitmiss_demo(a, [[0,0,0],[0,0,0],[1,1,1]], [[1,0,0],[0,1,0],[0,0,0]])

show_image(img1, img2, img3)

pl.show()