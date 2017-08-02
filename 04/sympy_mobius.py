# -*- coding: utf-8 -*-
import os
os.environ['PYGLET_SHADOW_WINDOW']="0"

from sympy import *
u, v = symbols("u,v")

x = (1+v/2*cos(u/2))*cos(u)
y = (1+v/2*cos(u/2))*sin(u)
z = v/2*sin(u/2)

Plot(x, y, z, [u, 0, 2*pi], [v, -1, 1])
