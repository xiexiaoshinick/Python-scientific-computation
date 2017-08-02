# -*- coding: utf-8 -*-
from visual import display, box, sphere, arrow

height = 2
offsetx = 1.0
heightx = 0.5

scene=display(background=(1,1,1), range=5, width=1280, height=720)
img = box(pos=(0,0,0),length=4,height=4,width=0.02,opacity=0.3)
point = sphere(radius=0.05, pos=(offsetx,0,heightx), color=(1,0,0))
point2 = sphere(radius=0.05, pos=(offsetx,0,0), color=(1,0,0))
arrow(pos = (1,0,0), axis=(0,0,heightx), shaftwidth=0.02, fixedwidth=1)

arrow(pos = (0,0,0), axis=(0,0,height), shaftwidth=0.02, fixedwidth=1)
camera = sphere(radius=0.05, pos=(0,0,height), color=(0,1,0))
arrow(pos=(0,0,height), axis=(offsetx+heightx/(height-heightx), 0, -height), shaftwidth=0.04, fixedwidth=1)

sphere(pos=(offsetx+heightx/(height-heightx), 0, 0), radius=0.05, color=(0,0,1))

arrow(pos=(0,0,0),axis=(offsetx,0,0.0), shaftwidth=0.02, fixedwidth=1)
arrow(pos=(offsetx, 0, 0), axis=(heightx/(height-heightx), 0,0), shaftwidth=0.02, fixedwidth=1)
while True:
    pass