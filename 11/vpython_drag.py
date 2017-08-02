# coding=utf-8
from visual import *

def drag_plane(mouse):
    "返回鼠标射线与X-Y平面的交点"
    return mouse.project(normal=(0,0,1), point=(0,0,0)) 

scene.range = 5 # 固定场景范围
ball = sphere(pos=(-3,0,0), color=color.cyan)
cube = box(pos=(+3,0,0), size=(2,2,2), color=color.red)
box(pos=(0,0,-1), size=(8,8,0.05))

pick = None # 当前鼠标拖动的物体

while True: 
    if scene.mouse.events: 
        mevent = scene.mouse.getevent() 
        if mevent.drag and mevent.pick: # 如果是拖动事件，并且选中了某物体
            drag_pos = drag_plane(mevent)  # 拖动的起始位置 
            pick = mevent.pick 
        elif mevent.drop: # 如果是释放事件
            pick = None 
    if pick:
        # 鼠标投射到与X-Y平面上的坐标
        new_pos = drag_plane(scene.mouse) 
        if new_pos != drag_pos: # 如果鼠标移动了
            pick.pos += new_pos - drag_pos  # 修改物体的位置 
            drag_pos = new_pos # 更新拖动的起始位置 