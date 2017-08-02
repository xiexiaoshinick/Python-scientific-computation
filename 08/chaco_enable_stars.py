# -*- coding: utf-8 -*-
"""
使用Enable的组件制作绘制星星的应用程序
"""
import numpy as np
from enthought.traits.api import (HasTraits, Instance, List, Enum, 
                                    Float, Color, Tuple, Range)
from enthought.traits.ui.api import Item, View, HGroup

from enthought.enable.api import ComponentEditor, Component
from chaco_kiva_stars import draw_star, star_polygon


def convert_color(c):
    if c.__class__.__name__ == "QColor":
        return (c.red()/255.0, c.green()/255.0, c.blue()/255.0)
    else:
        return (c[0]/255.0, c[1]/255.0, c[2]/255.0)
        

class Star(HasTraits):
    x = Float
    y = Float
    r = Float
    theta = Float
    n = Range(3, 10)
    s = Float
    c = Tuple
    def polygon(self):
        return star_polygon(self.x, self.y, self.r, self.theta, self.n, self.s)
       

class StarComponent(Component):
    stars = List(Star)
    star_color = Color((255,255,255))
    edges = Range(3, 10, 5)
    sx = Float # 移动开始时的星星中心X坐标
    sy = Float # 移动开始时的星星中心Y坐标
    mx = Float # 移动开始时的鼠标X坐标
    my = Float # 移动开始时的鼠标Y坐标
    moving_star = Instance(Star)
    
    event_state = Enum("normal", "drawing", "moving") 


    def normal_left_down(self, event):
        "添加一个Star对象进stars列表，并切换到drawing状态"
        self.stars.append(
            Star(x=event.x, y=event.y, r=0, theta=0, n=self.edges,
                s = 0.5, c=convert_color(self.star_color)))
        self.event_state = "drawing" 
        self.request_redraw()
        
    def drawing_mouse_move(self, event):
        "修改stars中最后一个Star对象的半径和起始角度"
        star = self.stars[-1]
        star.r = np.sqrt((event.x-star.x)**2+(event.y-star.y)**2)
        star.theta = np.arctan2(event.y-star.y, event.x-star.x)
        self.request_redraw()
        
    def drawing_left_up(self, event):
        "完成一个星形的绘制，回到normal状态"
        self.event_state = "normal"        
        
    def normal_mouse_wheel(self, event):
        "找到包含鼠标坐标的星形，并修改其半径比例"
        star = self.find_star(event.x, event.y) 
        if star is not None:
            star.s += event.mouse_wheel * 0.02
            if star.s < 0.05: star.s = 0.05
            self.request_redraw()
                
    def normal_right_down(self, event):
        "找到包含鼠标坐标的星形，用moving_star属性保存它，并进入moving状态"
        star = self.find_star(event.x, event.y)
        if star is not None:
            self.mx, self.my = event.x, event.y # 记录鼠标位置
            self.sx, self.sy = star.x, star.y # 记录星形的中心位置
            self.moving_star = star
            self.event_state = "moving"
    
    def moving_mouse_move(self, event):
        "修改moving_star的x,y坐标，实现星形的移动"
        self.moving_star.x = self.sx + event.x - self.mx
        self.moving_star.y = self.sy + event.y - self.my
        self.request_redraw()
        
    def moving_right_up(self, event):
        "移动操作结束，回到normal状态"
        self.event_state = "normal"

        
    def _draw_overlay(self, gc, view_bounds=None, mode="normal"):
        gc.clear((0,0,0,1)) #填充为全黑
        gc.save_state()
        for star in self.stars:
            draw_star(gc, star.x, star.y, star.r, star.c, star.theta, star.n, star.s)
            gc.draw_path()
        gc.restore_state()        


    def find_star(self, x, y):
        from enthought.kiva.agg import points_in_polygon
        for star in self.stars[::-1]:
            if points_in_polygon((x, y), star.polygon()):        
                return star
        return None
        


class StarDesign(HasTraits):
    box = Instance(StarComponent)
    
    view = View(
        HGroup(Item("object.box.edges", label=u"顶角数"),
               Item("object.box.star_color", label=u"颜色")),
        Item("box", editor=ComponentEditor(),show_label=False),
        resizable=True,
        width = 600, 
        height = 400,
        title = u"星空设计"
    )
    
    def __init__(self, **traits):
        super(StarDesign, self).__init__(**traits)
        self.box = StarComponent()


if __name__ == "__main__":        
    p = StarDesign()
    p.configure_traits()
