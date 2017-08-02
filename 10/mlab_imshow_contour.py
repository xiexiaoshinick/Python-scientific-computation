# -*- coding: utf-8 -*-
import numpy as np
from enthought.mayavi import mlab

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2)

mlab.figure(1)
pl = mlab.imshow(x, y, z)

mlab.figure(2)
pl = mlab.contour_surf(x, y, z, contours=20)
mlab.show()