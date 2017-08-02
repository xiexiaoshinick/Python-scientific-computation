# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from numpy.random import normal

def hill2d(n, d):
    """
    绘制山脉曲面，曲面是一个(2**n + 1)*(2**n + 1)的图像，
    d为衰减系数
    """
    size = 2**n + 1
    scale = 1.0
    a = np.zeros((size, size))

    for i in xrange(n, 0, -1):
        s = 2**(i-1)
        s2 = s*2
        tmp = a[::s2,::s2]
        tmp1 = (tmp[1:,:] + tmp[:-1,:])*0.5 
        tmp2 = (tmp[:,1:] + tmp[:,:-1])*0.5
        tmp3 = (tmp1[:,1:] + tmp1[:,:-1])*0.5
        a[s::s2, ::s2] = tmp1 + normal(0,scale,tmp1.shape)
        a[::s2, s::s2] = tmp2 + normal(0,scale,tmp2.shape)
        a[s::s2,s::s2] = tmp3 + normal(0,scale,tmp3.shape)
        scale *= d

    return a
    
if __name__ == "__main__":    
    from enthought.mayavi import mlab
    from scipy.ndimage.filters import convolve
    a = hill2d(8, 0.5)
    a/= np.ptp(a) / (0.5*2**8) 
    a = convolve(a, np.ones((3,3))/9) 
    mlab.surf(a)
    mlab.show()