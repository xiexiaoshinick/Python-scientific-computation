# -*- coding: utf-8 -*-
from enthought.tvtk.api import tvtk
import numpy as np

x = np.array([0,3,9,15])
y = np.array([0,1,5])
z = np.array([0,2,3])
r = tvtk.RectilinearGrid()
r.x_coordinates = x 
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x), len(y), len(z) 

r.point_data.scalars = np.arange(0.0,r.number_of_points)
r.point_data.scalars.name = 'scalars'
