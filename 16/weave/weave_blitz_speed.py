# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
from timeit import timeit
from scipy import weave, ndimage

def numpy01(p):
    return p[:-2,1:-1] - p[2:,1:-1] + p[1:-1,:-2] - p[1:-1,2:]
    
def numpy02(p):
    e1 = np.zeros((p.shape[0]-2, p.shape[1]-2), np.float)
    np.subtract(p[:-2,1:-1], p[2:,1:-1] , e1)
    np.add(e1, p[1:-1,:-2], e1)
    np.subtract(e1, p[1:-1,2:])
    return e1
    
def blitz(p):
    e2 = np.zeros((p.shape[0]-2, p.shape[1]-2), np.float)
    weave.blitz("e2 = p[:-2,1:-1]-p[2:,1:-1]+p[1:-1,:-2]-p[1:-1,2:]")
    return e2

p = sp.lena()
p = ndimage.interpolation.zoom(p, 2).astype(np.float)
blitz(p)

if __name__ == "__main__":
    import_str = "from __main__ import numpy01, numpy02, blitz, p"
    for s in ["numpy01", "numpy02", "blitz"]:
        print s, timeit(s+"(p)", import_str, number = 100)
