# -*- coding: utf-8 -*-
from visual import *
import numpy as np

scene.background=1,1,1

pos = np.array([
    [0,0,0], # 顶点1坐标
    [1,0,0], # 顶点2坐标
    [0,1,0], # 顶点3坐标
], dtype=np.float)

normal = np.array([
    [0,0,1], # 顶点1法线方向
    [0,0,1], # 顶点2法线方向
    [0,0,1], # 顶点3法线方向
], dtype=np.float)

color = np.array([
    [0,0,1], # 顶点1颜色
    [0,1,0], # 顶点2颜色
    [1,0,0], # 顶点3颜色
], dtype=np.float)

def single_face():
    faces(pos=pos, normal=normal, color=color)
   
single_face()     

  
def double_face(pos, normal, color):
    triangle = frame()
    f = faces(
        pos=np.vstack([pos, pos[::-1]]),
        normal=np.vstack([normal, normal[::-1]]),
        color=np.vstack([color, color[::-1]]),
        frame=triangle)
    return triangle

triangle = double_face(pos, normal, color)
triangle.pos = -1, -1, 0
