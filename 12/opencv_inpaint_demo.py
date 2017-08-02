# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import (HasTraits, Float, Instance,
    Enum, List, Range, Bool, Button, Event, on_trait_change)
from enthought.traits.ui.api import View, VGroup, Item, HGroup
from enthought.chaco.api import ArrayPlotData, Plot
from enthought.enable.api import ComponentEditor

from enthought.enable.api import AbstractOverlay

class CirclePainter(AbstractOverlay):
    """用半径为r的圆绘制鼠标轨迹，并调用InPaintDemo的fill_circle()
    在其mask图像上绘制选区。当鼠标松开时，调用InPaintDemo的inpaint()
    进行inpaint图像处理。
    """
    x = Float(-1) # 当前圆心X轴坐标
    y = Float(-1) # 当前圆心Y轴坐标
    r = Range(2.0, 20.0, 10.0)  # 圆形半径(数据坐标系)
    event_state = Enum("normal", "drawing")
    track = List() # 储存鼠标轨迹
    updated = Event()
    
    def clear_track(self):
        self.track = []
        self.request_redraw()
    
    def fill_circle(self, event):
        self.x = event.x
        self.y = event.y    
        plot = self.component
        x = plot.x_mapper.map_data(event.x)
        y = plot.y_mapper.map_data(event.y)
        self.track.append((self.x, self.y, x, y))
        self.request_redraw()
    
    def normal_mouse_move(self, event):
        self.x = event.x
        self.y = event.y
        self.request_redraw()
           
    def normal_left_down(self, event):
        self.event_state = "drawing"
        self.fill_circle(event)
        
    def drawing_mouse_move(self, event):
        self.fill_circle(event)

    def drawing_left_up(self, event):
        self.event_state = "normal"
        self.updated = True
        
    def normal_mouse_leave(self, event):
        self.x, self.y = -1, -1
        self.request_redraw()
        
    def overlay(self, component, gc, view_bounds=None, mode="normal"):
        plot = self.component   
        r = plot.x_mapper.map_screen(self.r)
        
        gc.save_state()
        if self.x > 0 and self.y > 0:
            gc.set_stroke_color((1,1,1))
            gc.arc(self.x, self.y, r, 0.0, 2*np.pi)
            gc.stroke_path()

        gc.set_fill_color((1,1,1))            
        for x, y, _, _ in self.track:
            gc.arc(x, y, r, 0.0, 2*np.pi)
        gc.fill_path()
        gc.restore_state()               

class InPaintDemo(HasTraits):
    plot = Instance(Plot)
    painter = Instance(CirclePainter)
    r = Range(2.0, 20.0, 10.0) # inpaint的半径参数
    method = Enum("INPAINT_NS", "INPAINT_TELEA") # inpaint的算法
    show_mask = Bool(False) # 是否显示选区
    clear_mask = Button(u"清除选区")
    apply = Button(u"保存结果")
    
    view = View(
        VGroup(
            VGroup(
                Item("object.painter.r", label=u"画笔半径"),
                Item("r", label=u"inpaint半径"),
                HGroup(
                    Item("method", label=u"inpaint算法"),
                    Item("show_mask", label=u"显示选区"),
                    Item("clear_mask", show_label=False),
                    Item("apply", show_label=False),                    
                )
            ),
            Item("plot", editor=ComponentEditor(), show_label=False),
        ),
        title = u"inpaint Demo控制面板",
        width = 500, height = 450, resizable = True
    )
    
    def __init__(self, *args, **kwargs):
        super(InPaintDemo, self).__init__(*args, **kwargs)
        self.img = cv.imread("stuff.jpg") # 原始图像
        self.img2 = self.img.clone() # inpaint效果预览图像
        self.mask = cv.Mat(self.img.size(), cv.CV_8UC1) # 储存选区的图像
        self.mask[:] = 0
        self.data = ArrayPlotData(img = self.img[:,:,::-1])
        self.plot = Plot(self.data, padding=10, 
            aspect_ratio=float(self.img.size().width)/self.img.size().height)
        self.plot.x_axis.visible = False
        self.plot.y_axis.visible = False
        imgplot = self.plot.img_plot("img", origin="top left")[0]
        self.painter = CirclePainter(component=imgplot)
        imgplot.overlays.append(self.painter)
     
    @on_trait_change("r,method")
    def inpaint(self):
        cv.inpaint(self.img, self.mask, self.img2, self.r, getattr(cv, self.method))
        self.draw()
        
    @on_trait_change("painter:updated")
    def painter_updated(self):
        for _, _, x, y in self.painter.track:
            # 在储存选区的mask上绘制圆形
            cv.circle(self.mask, cv.Point(int(x), int(y)), int(self.painter.r), 
                cv.Scalar(255,255,255,255), thickness=-1) # 宽度为负表示填充圆形
        self.inpaint()
        self.painter.track = []
        self.painter.request_redraw()
        
    def _clear_mask_fired(self):
        self.mask[:] = 0
        self.inpaint()
        
    def _apply_fired(self):
        """保存inpaint的处理结果，并清除选区"""
        self.img[:] = self.img2[:]
        self._clear_mask_fired()
      
    @on_trait_change("show_mask")
    def draw(self):
        if self.show_mask:
            data = self.img[:,:,::-1].copy()
            data[self.mask[:]>0] = 255
            self.data["img"] = data            
        else:
            self.data["img"] = self.img2[:,:,::-1]
        
demo = InPaintDemo()     
demo.configure_traits()