# coding=utf-8
from itertools import izip
import numpy as np
from visual import *
scene.background = 1,1,1 # 场景背景颜色
color = 0.7,0.7,0.7 # 模型颜色
r = 10.0 #水雷半径

s = sphere(radius=r*1.02, color=color) 

# 在球坐标系中计算半径为r的球面上的坐标点
t, f = np.mgrid[0:pi:5j,0:2*pi:10j] 
xp = r*np.sin(t)*cos(f)
yp = r*np.sin(t)*sin(f)
zp = r*np.cos(t)

for pos in izip(xp.flat, yp.flat, zp.flat): 
    cone(pos = pos, axis=pos, length=r/5, radius=r/10, color=color) 