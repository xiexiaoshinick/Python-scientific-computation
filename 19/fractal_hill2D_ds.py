#-*- coding:utf-8 -*- 
import numpy as np
from numpy.random import normal

def hill2d_ds(n, d):
    size = 2**n + 1
    scale = 1.0
    a = np.zeros((size, size))

    for i in xrange(n, 0, -1):
        s = 2**(i-1)
        s2 = 2*s
        
        # 方形平均
        t = a[::s2,::s2]
        t2 = (t[:-1,:-1] + t[1:,1:] + t[1:,:-1] + t[:-1,1:])/4
        tmp = a[s::s2,s::s2]
        tmp[...] = t2 + normal(0, scale, tmp.shape)
        
        buf = a[::s2, ::s2]
        
        # 菱形平均分两步，分别计算水平和垂直方向上的点
        t = a[::s2,s::s2]
        t[...] = buf[:,:-1] + buf[:,1:]
        t[:-1] += tmp
        t[1:]  += tmp
        t[[0,-1],:] /= 3 # 边上是3个值的平均
        t[1:-1,:] /= 4 # 中间的是4个值的平均
        t[...] += np.random.normal(0, scale, t.shape)

        t = a[s::s2,::s2]    
        t[...] = buf[:-1,:] + buf[1:,:]
        t[:,:-1] += tmp
        t[:,1:] += tmp
        t[:,[0,-1]] /= 3
        t[:,1:-1] /= 4
        t[...] += np.random.normal(0, scale, t.shape)
    
        scale *= d  
    return a
   
if __name__ == "__main__":
    from enthought.mayavi import mlab
    from scipy.ndimage.filters import convolve        
    a = hill2d_ds(8, 0.5)
    a/= np.ptp(a) / (0.5*2**8)
    a = convolve(a, np.ones((3,3))/9.0)    
    mlab.surf(a)
    mlab.show()  
