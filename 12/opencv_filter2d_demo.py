# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Array, Float
from enthought.traits.ui.api import View, Item

class FilterDemo(HasTraits):
    kernel = Array(shape=(3,3),dtype=np.float)
    scale = Float
    
    view = View(
        Item("kernel", label=u"卷积核"),
        Item("scale", label=u"乘积因子"),
        title = u"Filter Demo控制面板"
    )    
    
    def __init__(self, *args, **kwargs):
        super(FilterDemo, self).__init__(*args, **kwargs)
        self.kernel = np.ones((3,3))
        self.img = cv.imread("lena.jpg")
        self.on_trait_change(self.redraw, "kernel,scale")
        self.scale = 1.0 / 9.0
        
    def redraw(self):
        img2 = cv.Mat()
        kernel = cv.asMat(self.kernel*self.scale, force_single_channel=True)
        cv.filter2D(self.img, img2, -1, kernel)
        cv.imshow("Filter Demo", img2)
        
cv.namedWindow( "Filter Demo", cv.CV_WINDOW_AUTOSIZE )
demo = FilterDemo()
demo.configure_traits()    