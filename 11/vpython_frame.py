# coding=utf-8
import numpy as np
from visual import *
scene.background = 1,1,1 # 场景背景颜色
scene.foreground = 0.7,0.7,0.7 # 模型颜色

f = frame()
ax = arrow(axis=(1,0,0), frame=f)
ay = arrow(axis=(0,1,0), frame=f)
az = arrow(axis=(0,0,1), frame=f)

f.pos = (-0.5, -0.5, 0)
f.rotate(angle=pi/4, axis=(0,0,1))
