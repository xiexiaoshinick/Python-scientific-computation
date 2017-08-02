# -*- coding: utf-8 -*-
from enthought.tvtk.api import tvtk
import numpy as np

def make_points_array(x, y, z):
    return np.c_[x.ravel(), y.ravel(), z.ravel()]
    
z, y, x = np.mgrid[:3.0, :5.0, :4.0] 
x *= (4-z)/3 
y *= (4-z)/3 
s1 = tvtk.StructuredGrid()
s1.points = make_points_array(x, y, z) 
s1.dimensions = x.shape[::-1] 
s1.point_data.scalars = np.arange(0, s1.number_of_points)
s1.point_data.scalars.name = 'scalars'

r, theta, z2 = np.mgrid[2:3:3j, -np.pi/2:np.pi/2:6j, 0:4:7j]
x2 = np.cos(theta)*r
y2 = np.sin(theta)*r

s2 = tvtk.StructuredGrid(dimensions=x2.shape[::-1])
s2.points = make_points_array(x2, y2, z2)
s2.point_data.scalars = np.arange(0, s2.number_of_points)
s2.point_data.scalars.name = 'scalars'
