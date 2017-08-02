# -*- coding: utf-8 -*-
import random
import numpy as np
from enthought.traits.api import  HasTraits, Float, Instance, Array, Int
from enthought.traits.ui.api import Item, View, Handler
from enthought.enable.api import ComponentEditor, Component
from enthought.kiva.constants import PIXEL_MARKER
from enthought.pyface.timer.api import Timer

class DotComponent(Component):
    points = Array

    def projection_points(self, p):
        size = min(self.width, self.height) * 0.7
        tx = p[0,:]*size
        ty = p[1,:]*size
        tz = p[2,:]*size
        d = 3*size - tz
        nx = size*tx/d + self.width/2
        ny = self.height/2-size*ty/d
        self.points = np.array([nx, ny]).T
        
    def _draw_overlay(self, gc, view_bounds=None, mode="normal"):
        if self.points.ndim != 2: return
        gc.clear((0,0,0,1))
        gc.save_state()
        gc.set_fill_color((1,1,1))
        gc.draw_marker_at_points(self.points, 1, PIXEL_MARKER)
        gc.restore_state()  
        
class AnimationHandler(Handler):
    def init(self, info):
        super(AnimationHandler, self).init(info)
        info.object.timer = Timer(10, info.object.on_timer) 
    
    def closed(self, info, is_ok):
        super(AnimationHandler, self).closed(info, is_ok)
        info.object.timer.Stop() 
        
class AnimationDemo(HasTraits):
    numdots = Int(3000)
    box = Instance(DotComponent)
    points3d = Array
    target_points3d = Array
    angle_x = Float()
    angle_y = Float()
    angle_z = Float()
    frame_count = Int(0)
    view = View(
        Item("box", editor=ComponentEditor(),show_label=False),
        resizable=True,
        width = 600, 
        height = 600,
        title = u"变形",
        handler = AnimationHandler()
    )    
    
    def __init__(self, **traits):
        super(AnimationDemo, self).__init__(**traits)
        self.box = DotComponent()
        self.points3d = np.zeros((4, self.numdots))
        self.points3d[3,:] = 1
        self.target_points3d = np.zeros((4, self.numdots))
        self.target_points3d[3,:] = 1
        
        self.points3d[:3,:] = self.get_object_points()
        self.target_points3d[:3,:] = self.get_object_points()
        self.frame_count = 0
        
    def get_object_points(self):
        r = np.random.rand(self.numdots)
        t = np.linspace(0, np.pi*2, self.numdots)
        a = r * np.pi - np.pi/2
        l = [np.cos(a), np.cos(t), np.sin(a), np.sin(t), np.ones(self.numdots)]
        c = random.choice
        return c(l)*c(l), c(l)*c(l), c(l)*c(l)
            
    def make_matrix(self):
        s = np.sin([self.angle_x, self.angle_y, self.angle_z])
        c = np.cos([self.angle_x, self.angle_y, self.angle_z])
        #构造三个轴的旋转矩阵
        mx= np.eye(4)
        mx[[1,1,2,2],[1,2,1,2]] = c[2], -s[2], s[2], c[2]
        my = np.eye(4)
        my[[0,0,2,2], [0,2,0,2]] = c[1], s[1], -s[1], c[1]
        mz = np.eye(4)
        mz[[0,0,1,1], [0,1,0,1]] = c[0],-s[0],s[0],c[0]
        #进行坐标旋转
        return np.dot(mz, np.dot(my, mx))     
        
    def projection(self):
        m = self.make_matrix()
        result = np.dot(m, self.points3d)
        self.box.projection_points(result)
        
    def on_timer(self):
        self.angle_z += 0.02
        self.angle_x += 0.02
        self.projection()
        self.box.request_redraw()
        self.points3d[:3,:] += 0.04 * (self.target_points3d[:3,:] - self.points3d[:3,:])
        self.points3d[:3,:] += np.random.normal(0, 0.004, (3, self.numdots))
        self.frame_count += 1
        if self.frame_count > 300:
            self.frame_count = 0
            self.target_points3d[:3,:] = self.get_object_points()
    
if __name__ == "__main__":        
    p = AnimationDemo()
    p.configure_traits()
