# -*- coding: utf-8 -*-
"""
本程序有BUG，不能正常运行。在IPython中执行本程序进行调试。
"""
import pylab as pl
import numpy as np

def test_debug():
    x = np.linspace(1, 50, 10000)
    img = np.sin(x*np.cos(x))
    pl.imshow(img)
    pl.show()
    
test_debug()    