# -*- coding: utf-8 -*-
"""
用mesh()绘制旋转抛物面
"""
import numpy as np
from enthought.mayavi import mlab

rho, theta = np.mgrid[0:1:40j, 0:2*np.pi:40j] 

z = rho*rho 

x = rho*np.cos(theta) 
y = rho*np.sin(theta) 

s = mlab.mesh(x,y,z)
mlab.show()