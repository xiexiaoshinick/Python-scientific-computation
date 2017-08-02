# -*- coding: utf-8 -*-
"""
本程序使用Enable绘制双摆动画，通过TraitsUI制作GUI，可以动态地调节
双摆的质量和长度。

在动画绘图框上按住鼠标左键并拖动鼠标修改双摆的初始角度。
"""
import numpy as np
from enthought.traits.api import (HasTraits, Instance, Float, Bool,
                                  DelegatesTo, Int, Tuple, Range, Enum)
from enthought.traits.ui.api import View, Item, HGroup, VGroup
from enthought.enable.api import ComponentEditor, Component
from enthought.pyface.timer.api import Timer
from double_pendulum_odeint import double_pendulum_odeint, DoublePendulum

class DoublePendulumComponent(Component):
    gui = Instance("DoublePendulumGUI")
    m1 = DelegatesTo("gui")
    m2 = DelegatesTo("gui")
    l1 = DelegatesTo("gui")
    l2 = DelegatesTo("gui")
    p = Tuple((0.0,0.0,0.0,0.0))
    event_state = Enum('normal', 'adjusting')
    
    def _draw_overlay(self, gc, view_bounds=None, mode="normal"):
        scale = (self.height - 100) / (self.l1 + self.l2) / 1.5
        self.cx = cx = self.width / 2
        self.cy = cy = self.height - 100
        x0,y0,x1,y1 = self.p
        
        gc.save_state()
        gc.translate_ctm(cx, cy)
        gc.scale_ctm(scale, scale)
        gc.set_line_width(3)
        gc.move_to(0,0)
        gc.line_to(x0,y0)
        gc.line_to(x1,y1)
        gc.stroke_path()
        gc.arc(x0, y0, 3*np.sqrt(self.m1)/scale, 0.0, 2 * np.pi)
        gc.arc(x1, y1, 3*np.sqrt(self.m2)/scale, 0.0, 2 * np.pi)
        gc.draw_path()
        gc.restore_state()
        
    def normal_left_down(self, event):
        dx = event.x - self.cx
        dy = event.y - self.cy
        self.x0 = event.x
        self.y0 = event.y        
        self.a1 = np.arctan2(dx, -dy)
        self.a2 = 0
        self.event_state = "adjusting"
        self.gui.animation = False
        self.gui.pendulum.init_status[:] = self.a1, 0, 0, 0
        
    def adjusting_mouse_move(self, event):
        dx = event.x - self.x0
        dy = event.y - self.y0
        self.a2 = np.arctan2(dx, -dy)
        self.gui.pendulum.init_status[:] = self.a1, self.a2, 0, 0
        
    def adjusting_left_up(self, event):
        self.gui.animation = True
        self.event_state = "normal"
        
class DoublePendulumGUI(HasTraits):
    pendulum = Instance(DoublePendulum)
    m1 = Range(1.0, 10.0, 2.0)
    m2 = Range(1.0, 10.0, 2.0)
    l1 = Range(1.0, 10.0, 2.0)
    l2 = Range(1.0, 10.0, 2.0)
    positions = Tuple
    index = Int(0)
    timer = Instance(Timer)
    graph = Instance(DoublePendulumComponent)
    animation = Bool(True)
    
    view = View(
        HGroup(
            VGroup(
                Item("m1"),
                Item("m2"),
                Item("l1"),
                Item("l2"),
            ),
            Item("graph", editor=ComponentEditor(), show_label=False),
        ),
        width = 600,
        height = 400,
        title = u"双摆演示",
        resizable = True
    )
    def __init__(self):
        self.pendulum = DoublePendulum(self.m1, self.m2, self.l1, self.l2)
        self.pendulum.init_status[:] = 1.0, 2.0, 0, 0
        self.graph = DoublePendulumComponent()
        self.graph.gui = self    
        self.timer = Timer(10, self.on_timer)
        
    def on_timer(self, *args):
        if len(self.positions) == 0 or self.index == len(self.positions[0]):
            self.pendulum.m1 = self.m1
            self.pendulum.m2 = self.m2
            self.pendulum.l1 = self.l1
            self.pendulum.l2 = self.l2        
            if self.animation:
                self.positions = double_pendulum_odeint(self.pendulum, 0, 0.5, 0.02)
            else:
                self.positions = double_pendulum_odeint(self.pendulum, 0, 0.00001, 0.00001)
            self.index = 0
        self.graph.p = tuple(array[self.index] for array in self.positions)
        self.index += 1
        self.graph.request_redraw()
        
gui = DoublePendulumGUI()
gui.configure_traits()        