# -*- coding: utf-8 -*-

import threading
from visual import *
from enthought.traits.api import *
from enthought.traits.ui.api import *


class VisualTraitsUI(HasTraits):
    acceleration = Range(0.0, 20, 9.8)
    auto_scale = Bool(True)
    
    view = View(
        Item("acceleration", label=u"加速度"),
        Item("auto_scale", label=u"自动缩放"),
        title=u"动画控制面板"
    )
    

    def __init__(self, *args, **kwargs):
        super(VisualTraitsUI, self).__init__(*args, **kwargs)
        self.lock = threading.Lock() 
        self.finish_event = threading.Event() 
        self.init_scene()
       
    def init_scene(self):
        self.scene = display(title="TraitsUI Demo", background=(1,1,1)) 
        self.floor = box(length=4, height=0.5, width=4, color=color.blue)
        self.ball = sphere(pos=(0,4,0), color=color.red)
        self.ball.velocity = vector(0,-1,0)
        self.dt = 0.01
        self.g = self.acceleration
        self.scene.autoscale = self.auto_scale 
              

    def animation(self):
        while not self.finish_event.is_set(): 
            rate(100)
            self.lock.acquire() 
            self.ball.pos = self.ball.pos + self.ball.velocity*self.dt
            if self.ball.y < 1:
                self.ball.velocity.y = -self.ball.velocity.y
            else:
                self.ball.velocity.y = self.ball.velocity.y - self.g*self.dt
            self.lock.release() 
        self.scene.visible = False 
        
    def start_animation(self):
        self.thread = threading.Thread(None, self.animation)
        self.thread.start()
    
    def end_animation(self):
        self.finish_event.set() 
        self.thread.join() 
                 

    def _acceleration_changed(self):
        self.lock.acquire()
        self.g = self.acceleration
        self.lock.release()
        
    def _auto_scale_changed(self):
        self.scene.autoscale = self.auto_scale
        

class AnimateHandler(Handler):
    def init(self, info):
        info.object.start_animation()
        return True
            
    def closed(self, info, is_ok):
        info.object.end_animation()        

     
demo = VisualTraitsUI()
demo.configure_traits(handler = AnimateHandler())       
