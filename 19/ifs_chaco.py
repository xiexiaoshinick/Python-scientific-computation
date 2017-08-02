# -*- coding: utf-8 -*-
import time
import pickle

import numpy as np
from enthought.enable.api import ComponentEditor
from enthought.traits.api import (HasTraits, Instance, Enum, List,
        Int, Event, Bool, Str, Button)
from enthought.traits.ui.api import Item, View, HGroup, EnumEditor
from enthought.traits.ui.menu import OKCancelButtons
from enthought.chaco.api import (ArrayPlotData, Plot, AbstractOverlay, 
        palette11, DataRange1D, ColorMapper)
from enthought.chaco.scatterplot import render_markers

from enthought.pyface.timer.api import Timer


from ifs_library import triangle_area, solve_eq, ifs

ITER_COUNT = 2000 # 一次ifs迭代的点数
ITER_TIMES = 20   # 总共调用ifs的次数

def make_color_map():
    return ColorMapper.from_palette_array(palette11, range=DataRange1D(low=0, high=10))

class TrianglesTool(AbstractOverlay):
    event_state = Enum('normal', 'moving')
    points = List()
    selected_index = Int(-1)
    changed = Event
    
    def __init__(self, component=None, *args, **kw):
        AbstractOverlay.__init__(self, component, *args, **kw)
        self.colors = make_color_map().map_screen(np.arange(0, 10))
    
    def normal_left_down(self, event):
        if len(self.points) >= 33: return
        self.points.append((event.x, event.y))
        self.changed = True
        self.request_redraw()
        
    def normal_right_down(self, event):
        if len(self.points) == 0: return 
        dist = np.array([(event.x-x)**2+(event.y-y)**2 for x,y in self.points])
        index = np.argmin(dist)
        if dist[index] < 100:
            if event.control_down:
                index = index // 3 * 3
                if index > 0:
                    del self.points[index:index+3]
                    self.changed = True
                    self.request_redraw()
            else:
                self.selected_index = index
                self.event_state = "moving"
            
    def moving_mouse_move(self, event):
        if self.selected_index >= 0 and self.selected_index < len(self.points):
            self.points[self.selected_index] = event.x, event.y
            self.changed = True
            self.request_redraw()
            
    def moving_right_up(self, event):
        self.selected_index = -1
        self.event_state = "normal"
        
    def overlay(self, component, gc, view_bounds=None, mode="normal"):
        gc.save_state()       
        count = len(self.points)
        for i in xrange(0,count,3):            
            if i==0:
                gc.set_line_width(2)
                gc.set_stroke_color((0,0,0,1))
            else:
                gc.set_line_width(1)
                gc.set_stroke_color( self.colors[(i-3)//3] )
                
            p1 = self.points[i]
            p2 = p3 = None
            if i+1 < count: p2 = self.points[i+1]
            if i+2 < count: p3 = self.points[i+2]
            
            if p2 != None:
                gc.move_to(*p1)
                gc.line_to(*p2)
            
            if p3 != None:
                gc.move_to(*p1)
                gc.line_to(*p3)
            
            if p2!=None and p3!=None:
                gc.move_to(*p2)
                gc.line_to(*p3)

            gc.draw_path()    
        gc.restore_state()
        render_markers(gc, self.points[0::3], "circle", 4, (1,0,0,0.5), 1, (1,0,0,0.5))
        render_markers(gc, self.points[1::3], "circle", 4, (0,1,0,0.5), 1, (0,1,0,0.5))
        render_markers(gc, self.points[2::3], "circle", 4, (0,0,1,0.5), 1, (0,0,1,0.5))
        
    def get_areas(self):
        """
        通过三角形的面积计算仿射方程的迭代概率
        """
        areas = []
        points = np.array(self.points)
        for i in range(1, len(self.points)/3):
            areas.append( triangle_area( np.array(points[i*3:i*3+3])) )
        s = sum(areas)
        return [x/s for x in areas]  

    def get_eqs(self):
        """
        计算所有的仿射方程
        """
        eqs = []
        points = np.array(self.points)
        for i in range(1,len(self.points)/3):
            eqs.append( solve_eq( points[:3], points[i*3:i*3+3]) )
        return eqs        
        
class AskName(HasTraits):
    name = Str("")
    view = View(
        Item("name", label = u"名称"),
        kind = "modal",
        buttons = OKCancelButtons,
        title = u"请输入名字"
    )
        
class IFSDesigner(HasTraits):
    plot = Instance(Plot)
    clear = Bool(False)
    draw = Bool(False)
    timer = Instance(Timer)
    ifs_names = List()
    ifs_points = List()
    current_name = Str()
    save_button = Button(u"保存当前IFS")
    unsave_button = Button(u"删除当前IFS")    
    
    view = View(
        HGroup(
            Item("current_name", editor = EnumEditor(name="object.ifs_names")),
            Item("save_button"),                
            Item("unsave_button"),
            show_labels=False
        ),
        Item("plot", editor=ComponentEditor(),show_label=False),
        resizable=True,
        width = 500, 
        height = 500,
        title = u"IFS图形设计器"
    )
    
    def __init__(self):       
        self.data = ArrayPlotData()
        self.set_empty_data()
        self.plot = Plot(self.data, padding=10)
        scatter = self.plot.plot(("x","y", "c"), type="cmap_scatter", 
            marker_size=1, color_mapper=make_color_map(), line_width=0)[0]
        self.plot.x_grid.visible = False
        self.plot.y_grid.visible = False
        self.plot.x_axis.visible = False
        self.plot.y_axis.visible = False
        self.tool = TrianglesTool(self.plot)
        self.plot.overlays.append(self.tool)

        try:
            with file("ifs_chaco.data","rb") as f:
                tmp = pickle.load(f)
                self.ifs_names = [x[0] for x in tmp]                
                self.ifs_points = [np.array(x[1]) for x in tmp]

            if len(self.ifs_names) > 0:
                self.current_name = self.ifs_names[-1]
        except:
            pass 
        
        self.tool.on_trait_change(self.triangle_changed, 'changed')
        self.timer = Timer(10, self.ifs_calculate)       

    def set_empty_data(self):
        self.data["x"] = np.array([])
        self.data["y"] = np.array([])
        self.data["c"] = np.array([])        
        
    def triangle_changed(self):
        count = len(self.tool.points)
        if count % 3 == 0:
            self.set_empty_data()        
            
        if count < 9:
            self.draw = False
            
        if count >= 9 and count % 3  == 0:
            self.clear = True
        
    def ifs_calculate(self):
        if self.clear == True:
            self.clear = False
            self.initpos = [0, 0]
            # 不绘制迭代的初始100个点
            x, y, c = ifs( self.tool.get_areas(), self.tool.get_eqs(), self.initpos, 100)
            self.initpos = [x[-1], y[-1]]
            self.draw = True
        
        if self.draw and len(self.data["x"]) < ITER_COUNT * ITER_TIMES:
            x, y, c = ifs( self.tool.get_areas(), self.tool.get_eqs(), self.initpos, ITER_COUNT)
            ox, oy, oc = self.data["x"], self.data["y"], self.data["c"]
            if np.max(np.abs(x)) < 1000000 and np.max(np.abs(y)) < 1000000:
                self.initpos = [x[-1], y[-1]]
                x, y, z = np.hstack((ox, x)), np.hstack((oy, y)), np.hstack((oc, c))
                self.data["x"], self.data["y"], self.data["c"] = x, y, z
                # 调整绘图范围，保持X-Y轴的比例为1:1
                xmin, xmax = np.min(x), np.max(x)                
                ymin, ymax = np.min(y), np.max(y)
                xptp, yptp = xmax - xmin, ymax-ymin
                xcenter, ycenter =(xmax + xmin) / 2.0 , (ymax + ymin) / 2.0
                w, h = float(self.plot.width), float(self.plot.height)
                scale = max(xptp/w , yptp/h)
                self.plot.index_range.low = xcenter - 0.5*scale*w
                self.plot.index_range.high = xcenter + 0.5*scale*w
                self.plot.value_range.low = ycenter - 0.5*scale*h
                self.plot.value_range.high = ycenter + 0.5*scale

    def _current_name_changed(self):
        index = self.ifs_names.index(self.current_name)
        self.tool.points = list(self.ifs_points[index])
        self.tool.changed = True
        self.clear = True
                
    def _save_button_fired(self):
        """
        保存按钮处理
        """
        ask = AskName(name = self.current_name)
        if ask.configure_traits():
            if ask.name not in self.ifs_names:
                self.ifs_names.append( ask.name )
                self.ifs_points.append( self.tool.points[:] )
            else:
                index = self.ifs_names.index(ask.name)
                self.ifs_names[index] = ask.name
                self.ifs_points[index] = self.tool.points[:]    
            self.save_data()
            self.current_name = ask.name
            
    def _unsave_button_fired(self):
        index = self.ifs_names.index(self.current_name)
        del self.ifs_names[index]
        del self.ifs_points[index]
        if index >= self.ifs_names[index]: index -= 1
        self.current_name = self.ifs_names[index]
        self.save_data()
        
    def save_data(self):               
        with file("IFS_chaco.data", "wb") as f:
            pickle.dump(zip(self.ifs_names, self.ifs_points), f)         
                   
gui = IFSDesigner()
gui.configure_traits()