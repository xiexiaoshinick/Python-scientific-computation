# -*- coding: utf-8 -*-
import pyopencv as cv
from enthought.traits.api import HasTraits, Range, Button
from enthought.traits.ui.api import View, Item

class MeanShiftDemo(HasTraits):
    spatial_radius = Range(1, 40, 20)
    color_radius = Range(1, 100, 40)
    max_level = Range(1, 4, 2)
    do_button = Button(u"计算")
    
    view = View(
        Item("spatial_radius", label=u"空间半径"),
        Item("color_radius", label=u"颜色半径"),
        Item("max_level", label=u"最大层数"),
        Item("do_button", show_label=False),
        title = u"Mean Shift Demo控制面板"
    )    
    
    def __init__(self, *args, **kwargs):
        super(MeanShiftDemo, self).__init__(*args, **kwargs)
        self.img = cv.imread("fruits.jpg")
        self.img2 = self.img.clone()
        self.on_trait_change(self.redraw, "do_button")
        self.redraw()
        
    def redraw(self):
        cv.pyrMeanShiftFiltering(self.img, self.img2, 
            self.spatial_radius, self.color_radius, self.max_level)
        cv.imshow("Mean Shift Demo", self.img2)

cv.namedWindow("Mean Shift Demo")     
demo = MeanShiftDemo()     
demo.configure_traits() 