# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Trait, Float, Tuple, Instance, Array
from enthought.traits.ui.api import View, VGroup, Item
from enthought.chaco.api import ArrayPlotData, Plot
from enthought.enable.api import ComponentEditor

from enthought.enable.api import AbstractOverlay

class PointPicker(AbstractOverlay):
    application = Instance("FloodFillDemo")
    x = Float(-1)
    y = Float(-1)
    
    def normal_left_down(self, event):
        plot = self.application.imgplot
        x = plot.x_mapper.map_data(event.x)
        y = plot.y_mapper.map_data(event.y)
        self.x = event.x
        self.y = event.y
        self.application.point = x, y
        
    def overlay(self, component, gc, view_bounds=None, mode="normal"):
        if self.x > 0 and self.y > 0:
            gc.save_state()
            gc.set_alpha(0.4)
            gc.set_fill_color((1,1,1))
            gc.set_stroke_color((1,1,1))
            gc.set_line_width(1)
            gc.arc(self.x, self.y, 2, 0.0, 2*np.pi)
            gc.draw_path()
            gc.restore_state()     

            
Options = {
    u"以种子为标准-4联通":cv.FLOODFILL_FIXED_RANGE | 4,
    u"以种子为标准-8联通":cv.FLOODFILL_FIXED_RANGE | 8,
    u"以邻点为标准-4联通":4,
    u"以邻点为标准-8联通":8
}            


class FloodFillDemo(HasTraits):
    lo_diff = Array(np.float, (1,4))
    hi_diff = Array(np.float, (1,4))
    plot = Instance(Plot)
    point = Tuple((0,0))
    option = Trait(u"以邻点为标准-4联通", Options)
    
    view = View(
        VGroup(
            VGroup(
                Item("lo_diff", label=u"负方向范围"),
                Item("hi_diff", label=u"正方向范围"),
                Item("option", label=u"算法标志")
            ),
            Item("plot", editor=ComponentEditor(), show_label=False),
        ),
        title = u"FloodFill Demo控制面板",
        width = 500,
        height = 450,
        resizable = True
    )      
    
    def __init__(self, *args, **kwargs):
        self.lo_diff.fill(5)
        self.hi_diff.fill(5)
        self.img = cv.imread("lena.jpg")
        self.data = ArrayPlotData(img = self.img[:,:,::-1])
        w = self.img.size().width
        h = self.img.size().height
        self.plot = Plot(self.data, padding=10, aspect_ratio=float(w)/h)
        self.plot.x_axis.visible = False
        self.plot.y_axis.visible = False
        self.imgplot = self.plot.img_plot("img", origin="top left")[0]
        self.imgplot.interpolation = "nearest"
        self.imgplot.overlays.append(PointPicker(application=self, component=self.imgplot))
        
        self.on_trait_change(self.redraw, "point,lo_diff,hi_diff,option")
                
    def redraw(self):
        img=self.img.clone()
        cv.floodFill(img, cv.Point(*self.point), cv.Scalar(255, 0, 0, 255),
            loDiff=cv.asScalar(self.lo_diff[0]),
            upDiff=cv.asScalar(self.hi_diff[0]),
            flags = self.option_)
        self.data["img"] = img[:,:,::-1]
        
        
demo = FloodFillDemo()     
demo.configure_traits()
