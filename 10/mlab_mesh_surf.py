# -*- coding: utf-8 -*-
import numpy as np
from enthought.mayavi import mlab

x, y = np.mgrid[-2:2:20j, -2:2:20j] 
z = x * np.exp( - x**2 - y**2)
z *= 2
c = 2*x + y 

pl = mlab.mesh(x, y, z, scalars=c) 
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(pl)
mlab.show()
