# -*- coding: utf-8 -*-
"""
演示二值图像的膨胀算法。
"""
from binary_image_common import *
import scipy.ndimage.morphology as m

def dilation_demo(a, structure=None):
    b = m.binary_dilation(a, structure)
    img = expand_image(a, 255)
    return expand_image(np.logical_xor(a,b), 150, out=img)

a = make_text_image(15,15,4,-2,16,127,"A")
img1 = expand_image(a, 255)

img2 = dilation_demo(a)
img3 = dilation_demo(a, [[1,1,1],[1,1,1],[1,1,1]])
show_image(img1, img2, img3)

img4 = dilation_demo(a, [[0,0,0],[1,1,1],[0,0,0]])
img5 = dilation_demo(a, [[0,1,0],[0,1,0],[0,1,0]])
img6 = dilation_demo(a, [[0,1,0],[0,1,0],[0,0,0]])
pl.figure()
show_image(img4, img5, img6)

pl.show()