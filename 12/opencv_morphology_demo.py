# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Array, Enum, Int
from enthought.traits.ui.api import View, Item

class MorphologyDemo(HasTraits):
    structing_element = Array(shape=(3,3),dtype=np.uint8)
    process_type = Enum("dilate", "erode", 
        "MORPH_OPEN", "MORPH_CLOSE", "MORPH_GRADIENT", "MORPH_TOPHAT", "MORPH_BLACKHAT")
    iter = Int(1)
    
    view = View(
        Item("structing_element", label=u"结构元素"),
        Item("process_type", label=u"处理类型"),
        Item("iter", label=u"迭代次数"),
        title = u"Morphology Demo控制面板"
    )    
    
    def __init__(self, *args, **kwargs):
        super(MorphologyDemo, self).__init__(*args, **kwargs)
        self.structing_element = np.ones((3,3), dtype=np.uint8)
        self.img = cv.imread("lena.jpg")
        self.on_trait_change(self.redraw, "structing_element,process_type,iter")
        self.redraw()
        
    def redraw(self):
        img2 = cv.Mat()
        element = cv.asMat(self.structing_element, force_single_channel=True)
        if self.process_type.startswith("MORPH_"):
            type = getattr(cv, self.process_type)
            cv.morphologyEx(self.img, img2, type, element, iterations=self.iter)
        else:
            func = getattr(cv, self.process_type)
            func(self.img, img2, element, iterations=self.iter)
            
        cv.imshow("Morphology Demo", img2)
        
cv.namedWindow( "Morphology Demo", cv.CV_WINDOW_AUTOSIZE )
demo = MorphologyDemo()
demo.configure_traits()