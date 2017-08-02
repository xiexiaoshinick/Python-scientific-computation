# -*- coding: utf-8 -*-
import os
os.environ['PYGLET_SHADOW_WINDOW']="0"

from sympy import *
x = Symbol("x")
p = Plot(x/2, linewidth=2.0)
p.append(x**2)
p.append(log(x))
p.append(sin(x), cos(x))
p.append(cos(2*x),"mode=polar")
p.axes._label_axes=True # 可能因OpenGL的版本出错
p.saveimage("sympy_plot2d.png")