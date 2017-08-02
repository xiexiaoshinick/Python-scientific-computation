# coding=utf-8
from visual import *

def line_plane_intersect(l0, l1, p, n):
    "计算过l0和l1两点的直线与过点p法线为n的平面的交点坐标"
    d = -dot(p, n)
    line_direct = (l1 - l0) / mag(l1-l0)
    t = (-d-dot(l0, n))/dot(line_direct, n)
    return l0+t*line_direct

pos2d = vector(-4, -0.3, -0.3)
camera_pos = vector(-8,0,0)
box_size = 1.5    
    
scene.center = (-4, 0, 0)
scene.background = (1,1,1)
box(size=(0.05, 5, 5))
sphere(radius=0.1, color=(0,1,0))
box(pos = (-2, 0, 0), color=(1,0,0), size=(box_size,box_size,box_size))
curve(pos=[(-4, -2,-2), (-4, -2, 2), (-4, 2,2), (-4,2,-2), (-4, -2,-2)], color=(0,0,0))
sphere(radius=0.2, pos=(-8, 0, 0), color=(0,0,1)) # camera pos
arrow(pos=camera_pos, axis=(1,0,0), shaftwidth=0.05, color=(0,0,1)) # camera forward
sphere(radius=0.1, pos=pos2d)
curve(pos=[camera_pos, pos2d+(pos2d-camera_pos)*2], color=(0,0,0))
pos = line_plane_intersect(camera_pos, pos2d, vector(0,0,0), vector(1,0,0))
sphere(radius=0.1, color=(0,1,1), pos=pos)
pickpos = line_plane_intersect(camera_pos, pos2d, vector(-2-box_size/2, 0, 0), vector(1,0,0))
sphere(radius=0.1, color=(0,1,1), pos=pickpos)

box_pos = line_plane_intersect(camera_pos, vector(-2-box_size/2, box_size/2, box_size/2), vector(-4,0,0), vector(1,0,0))
x,y,z = box_pos
curve(pos=[box_pos, box_pos-(0,0,2*z), box_pos-(0,2*y,2*z),box_pos-(0,2*y,0), box_pos], color=(0.5,0.5,0.5))

curve(pos=[camera_pos, vector(-2-box_size/2, box_size/2, box_size/2)], color=(0.5,0.5,0.5))
curve(pos=[camera_pos, vector(-2-box_size/2, -box_size/2, box_size/2)], color=(0.5,0.5,0.5))
curve(pos=[camera_pos, vector(-2-box_size/2, box_size/2, -box_size/2)], color=(0.5,0.5,0.5))
curve(pos=[camera_pos, vector(-2-box_size/2, -box_size/2, -box_size/2)], color=(0.5,0.5,0.5))
