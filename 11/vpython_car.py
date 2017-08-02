# coding=utf-8
from visual import *
from vpython_xmodel import read_directx_model
        
def make_floor(size, n):
    f = frame()
    c = (0.9, 0.9, 0.9)
    c_flag = 1

    for i in xrange(0, n-1):
        for j in xrange(0, n-1):
            tmpbox = box(length = size, height = size, width = 0.1, color = c, frame = f)
            if c_flag==1:
                c_flag=2
                c = (0.9, 0.9, 0.9)
            else:
                c_flag=1
                c = (0.5, 0.5, 0.5)
            tmpbox.pos = ((i - n/2.0 + 1)*size,( j - 3)*size, 0)
    return f
    
if __name__ == "__main__":    
    HALF_TIRE_HEIGHT = 1.65
    FLOOR_SIZE = 150.0
    scene = display(title='VPython faces Demo', width=600, height=600,  center=(0,0,0), background=(0,1,1))
    scene.forward = (1,0,0)
    scene.up = (0,0,1)
    scene.forward = (0,1,-0.3)
    scene.autoscale = 0
    scene.range = (35,35,35)
            
    left_front_tire = read_directx_model("tire_left.x", False)
    left_front_tire.pos = (-4.2, 6.5, 0)
    right_front_tire = read_directx_model("tire_right.x", False)
    right_front_tire.pos = (4.2, 6.5, 0)
    front_tire_angle = 0.0

    left_back_tire = read_directx_model("tire_left.x", False)
    left_back_tire.pos = (-4.2, -6.3, 0)
    right_back_tire = read_directx_model("tire_right.x", false)
    right_back_tire.pos = (4.2, -6.3, 0)
    back_tire_angle = 0.0

    car_body = read_directx_model("car_body.x", True)
    car_body.pos = (0,0,1.6)
    car_body_xangle = 0.0

    floor = make_floor(FLOOR_SIZE/2, 14)
    floor.pos = (0,0,-HALF_TIRE_HEIGHT)
    center_x = 0.0
    center_y = 0.0

    speed = 10.0
    car_angle = 0.0

    flag = 0

    while True:
        rate(30)
        
        # 地面的移动
        tmp = floor.pos
        tmp += (0 , -speed, 0)
        center_x += speed * sin(car_angle)
        center_y -= speed * cos(car_angle)
        if center_x > FLOOR_SIZE:
            center_x -= FLOOR_SIZE
            tmp -= (FLOOR_SIZE*cos(car_angle), -FLOOR_SIZE*sin(car_angle), 0)
        if center_x < -FLOOR_SIZE:
            center_x += FLOOR_SIZE
            tmp += (FLOOR_SIZE*cos(car_angle), -FLOOR_SIZE*sin(car_angle), 0)
        if center_y > FLOOR_SIZE:
            center_y -= FLOOR_SIZE
            tmp -= (FLOOR_SIZE*sin(car_angle), FLOOR_SIZE*cos(car_angle), 0)
        if center_y <-FLOOR_SIZE:
            center_y += FLOOR_SIZE
            tmp += (FLOOR_SIZE*sin(car_angle), FLOOR_SIZE*cos(car_angle), 0)
        floor.pos = tmp
        
        # 实现轮胎的滚动效果
        #   这里不能围绕世界坐标系的X轴旋转，必须围绕轮胎坐标系的X轴旋转才能达到滚动效果
        #   轮胎围绕世界坐标系的Z轴旋转改变方向之后，轮胎坐标系的X轴的方向已经改变
        #   因此需要计算出轮胎坐标系的X轴的方向
        left_front_tire.rotate(angle=0.5, axis=(-cos(front_tire_angle),sin(front_tire_angle),0))
        right_front_tire.rotate(angle=0.5, axis=(-cos(front_tire_angle),sin(front_tire_angle),0))
        
        left_back_tire.rotate(angle=0.5, axis=(-cos(back_tire_angle),sin(back_tire_angle),0))
        right_back_tire.rotate(angle=0.5, axis=(-cos(back_tire_angle),sin(back_tire_angle),0))
           
        if scene.kb.keys:
            s = scene.kb.getkey()
            if s=='a':
                car_angle -= 0.05
                floor.rotate(angle=0.05, axis=(0,0,1), origin=(0, 0, 0))
            if s=='s':
                car_angle += 0.05
                floor.rotate(angle=-0.05, axis=(0,0,1), origin=(0, 0, 0))
            if s=='x':
                # 围绕世界坐标系的Z轴旋转
                left_front_tire.rotate(angle=0.05, axis=(0,0,1))
                right_front_tire.rotate(angle=0.05, axis=(0,0,1))
                front_tire_angle -= 0.05
            if s=='z':
                left_front_tire.rotate(angle=0.05, axis=(0,0,-1))
                right_front_tire.rotate(angle=0.05, axis=(0,0,-1))                
                front_tire_angle += 0.05