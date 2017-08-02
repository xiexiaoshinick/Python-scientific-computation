# -*- coding: utf-8 -*-
"""
为Chaco添加圆形选择工具，可选择以某点为中心，在指定半径范围内的所有数据点
"""
import numpy as np
from enthought.traits.api import HasTraits, Instance, Enum, Property, Float, Event
from enthought.traits.ui.api import View, Item
from enthought.enable.api import color_table
from enthought.enable.component_editor import ComponentEditor 
from enthought.chaco.api import Plot, ArrayPlotData, AbstractController
from enthought.chaco.api import AbstractOverlay, ScatterInspectorOverlay


class CircleSelectionOverlay(AbstractOverlay): 
    metadata = Property(depends_on = 'component') 
    
    def _get_metadata(self):
        return self.component.index.metadata       
    
    def overlay(self, component, gc, view_bounds=None, mode="normal"):
        if self.metadata.has_key('circle_center'):
            x, y = self.metadata['circle_center'] 
            r = self.metadata['circle_radius']
            gc.save_state()
            gc.set_alpha(0.4)
            gc.set_fill_color(color_table["lightskyblue"])
            gc.set_stroke_color(color_table["dodgerblue"])
            gc.set_line_width(1)
            gc.set_line_dash(None)
            gc.arc(x, y, r, 0.0, 2*np.pi) 
            gc.draw_path()
            gc.restore_state()


class CircleSelection(AbstractController): 
    metadata = Property(depends_on = 'component')
    event_state = Enum('normal', 'selecting', 'selected', 'moving') 
    selection_update = Event 
    x = Float # 圆心X坐标
    y = Float # 圆心Y坐标
    r = Float # 半径
    mx = Float # 移动开始时的鼠标的X坐标
    my = Float # 移动开始时的鼠标的Y坐标
    x0 = Float # 移动开始时的圆心X坐标
    y0 = Float # 移动开始时的圆心Y坐标

    def _get_metadata(self):
        return self.component.index.metadata
    

    def normal_left_down(self, event):
        self.x, self.y  = event.x, event.y
        self.metadata['circle_center'] = self.x, self.y
        self.metadata['circle_radius'] = 0
        self.event_state = 'selecting'
        
    def selecting_mouse_move(self, event):
        self.r = np.sqrt((self.x-event.x)**2 + (self.y-event.y)**2)
        self.metadata['circle_radius'] = self.r
        self._update_selection()
        
    def selecting_left_up(self, event):
        self.event_state = 'selected'
        
    def selected_left_down(self, event):
        r = np.sqrt((self.x-event.x)**2 + (self.y-event.y)**2)
        if r > self.r:
            del self.metadata['circle_center']
            del self.metadata['circle_radius']
            del self.metadata['selections']
            self.selection_update = True
            self.event_state = 'normal'
        else:
            self.mx, self.my = event.x, event.y
            self.x0, self.y0 = self.x, self.y
            self.event_state = 'moving'
            
    def moving_mouse_move(self, event):
        self.x = self.x0 + event.x - self.mx
        self.y = self.y0 + event.y - self.my
        self.metadata['circle_center'] = self.x, self.y
        self._update_selection()
        
    def moving_left_up(self, event):
        self.event_state = 'selected'
     
      
    def _update_selection(self):
        points = np.transpose(np.array((self.component.index.get_data(), 
            self.component.value.get_data()))) 
        screen_points = self.component.map_screen(points) 
        tmp = screen_points - np.array([self.x, self.y])
        tmp **= 2
        dist = np.sum(tmp, axis=1)
        self.metadata['selections'] = dist < self.r*self.r 
        self.selection_update = True


class CircleSelectionDemo(HasTraits):
    plot = Instance(Plot) 
    data = Instance(ArrayPlotData)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False), 
        width=500, height=500, resizable=True, title="Circle Selection Plot")
        
    def __init__(self, **traits):
        super(CircleSelectionDemo, self).__init__(**traits)
        x = np.random.random(100)*2
        y = np.random.random(100)
        data = ArrayPlotData(x=x, y=y) 
        plot = Plot(data) 
        
        scatter = plot.plot(("x", "y"), type="scatter", color="blue")[0]
        scatter.tools.append( CircleSelection(scatter) )
        scatter.overlays.append( ScatterInspectorOverlay(scatter,  
            selection_color="red", selection_marker="circle", 
            selection_outline_color = "black",
            selection_marker_size = 6) )
        scatter.overlays.append( CircleSelectionOverlay(scatter) )
        
        self.plot = plot
        self.data = data

if __name__ == "__main__":
    p = CircleSelectionDemo()
    p.configure_traits()        