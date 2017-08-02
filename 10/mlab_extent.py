# -*- coding: utf-8 -*-
from enthought.mayavi import mlab
import numpy as np
x, y = np.ogrid[-10:10:100j, -1:1:100j]
z = np.sin(5*((x/10)**2+y**2))
mlab.figure(bgcolor=(1,1,1), fgcolor=(0,0,0))
mlab.surf(x, y, z)
mlab.axes()

mlab.figure(bgcolor=(1,1,1), fgcolor=(0,0,0))
mlab.surf(x, y, z, extent=(-1,1,-1,1,-0.5,0.5))
mlab.axes(nb_labels=5)

mlab.figure(bgcolor=(1,1,1), fgcolor=(0,0,0))
mlab.surf(x, y, z, extent=(-1,1,-1,1,-0.5,0.5))
mlab.axes(ranges=(x.min(),x.max(),y.min(),y.max(),z.min(),z.max()), nb_labels=5)

mlab.show()