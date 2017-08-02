# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Array
from enthought.traits.ui.api import View, Item

class AffineDemo(HasTraits):
    m = Array(np.float, (2,3))
    size = Array(np.int, (1,2))
    
    view = View(
        Item("m", label=u"变换矩阵"),
        Item("size", label=u"图像大小"),
        title = u"Affine Demo控制面板"
    )    
    
    def __init__(self, **traits):
        super(AffineDemo, self).__init__(**traits)
        self.img = cv.imread("lena.jpg")
        self.m = np.array([[0.5,-0.3,100],[0.3,0.5,0]])
        size = self.img.size()
        self.on_trait_change(self.redraw, "m,size")
        self.size = np.array([[size.width, size.height]])
       
    def redraw(self):
        M = cv.asMat(self.m, force_single_channel=True)
        size = cv.Size(int(self.size[0,0]), int(self.size[0,1]))
        img2 = cv.Mat()
        if size.width > 0 and size.height > 0:
            cv.warpAffine(self.img, img2, M, size, borderValue=cv.CV_RGB(255,255,255))
            cv.imshow("Affine Demo", img2)

cv.namedWindow("Affine Demo")
demo = AffineDemo()
demo.configure_traits()