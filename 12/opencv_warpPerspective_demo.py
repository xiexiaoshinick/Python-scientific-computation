# -*- coding: utf-8 -*-
"""
透视变换
"""
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Array
from enthought.traits.ui.api import View, Item

class PerspectiveDemo(HasTraits):
    src = Array(shape=(4,2), dtype=np.float32)
    dst = Array(shape=(4,2), dtype=np.float32)
    
    View = View(
        Item("dst", label=u"变换后坐标"),
        title = u"Perspective Demo控制面板"
    )
    
    def __init__(self, **traits):
        super(PerspectiveDemo, self).__init__(**traits)
        self.img = cv.imread("lena.jpg")
        w = self.img.size().width
        h = self.img.size().height
        self.src = np.array([[0,0],[w,0],[0,h],[w,h]],dtype=np.float32)
        self.dst = np.array([[0,0],[w,0],[0,h],[w,h]],dtype=np.float32)
        self.on_trait_change(self.redraw, "src,dst")
        self.redraw()
        
    def redraw(self):
        src = cv.asvector_Point2f(self.src)
        dst = cv.asvector_Point2f(self.dst)
        m = cv.getPerspectiveTransform(src, dst)
        print m
        img2 = cv.Mat()
        cv.warpPerspective(self.img, img2, m, self.img.size())
        cv.imshow("Perspective Demo", img2)

cv.namedWindow("Perspective Demo")
demo = PerspectiveDemo()
demo.configure_traits()