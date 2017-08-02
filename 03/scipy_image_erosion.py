# -*- coding: utf-8 -*-
"""
演示二值图像的腐蚀算法。
"""
from binary_image_common import *
import scipy.ndimage.morphology as m

def erosion_demo(a, structure=None):
    b = m.binary_erosion(a, structure)
    img = expand_image(a, 255)
    return expand_image(np.logical_xor(a,b), 100, out=img)

a = make_text_image(15,15,4,-2,16,0,"A")
img1 = expand_image(a, 255)

img2 = erosion_demo(a)
img3 = erosion_demo(a, [[1,1,1],[1,1,1],[1,1,1]])
show_image(img1, img2, img3)

pl.show()