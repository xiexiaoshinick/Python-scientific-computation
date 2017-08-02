# -*- coding: utf-8 -*-
"""
直方图范围调整演示
"""
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Instance, Bool
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.chaco.tools.api import RangeSelection, RangeSelectionOverlay
from enthought.enable.component_editor import ComponentEditor
from enthought.pyface.timer.api import Timer

class HistDemo(HasTraits):
    plot = Instance(Plot)
    timer = Instance(Timer)
    need_update = Bool(False)
    view = View(
        Item("plot", editor=ComponentEditor(), show_label=False),
        resizable = True, width = 500, height = 250, title="Hist Demo")
    
    def __init__(self, **traits):
        super(HistDemo, self).__init__(**traits)
        img = cv.imread("lena.jpg")
        gray_img = cv.Mat()
        cv.cvtColor(img, gray_img, cv.CV_BGR2GRAY)
        self.img = gray_img
        self.img2 = self.img.clone()
        result = cv.MatND()

        r = cv.vector_float32([0, 256])
        ranges = cv.vector_vector_float32([r, r])        
        
        cv.calcHist(cv.vector_Mat([self.img]),
            channels = cv.vector_int([0, 1]), 
            mask = cv.Mat(), 
            hist = result,
            histSize=cv.vector_int([256]), 
            ranges=ranges
            )
        
        data = ArrayPlotData(x=np.arange(0, len(result[:])), y=result[:])
        self.plot = Plot(data, padding=10)
        line = self.plot.plot(("x", "y"))[0]
        self.select_tool = RangeSelection(line, left_button_selects=True)
        line.tools.append( self.select_tool )
        self.select_tool.on_trait_change(self._selection_changed, "selection")
        line.overlays.append(RangeSelectionOverlay(component=line))
        
        cv.imshow("Hist Demo", self.img)
        
        self.timer = Timer(50, self.on_timer)
        
    def _selection_changed(self):
        if self.select_tool.selection != None:
            self.need_update = True
            
    def on_timer(self):
        if self.need_update:
            x0, x1 = self.select_tool.selection
            self.img2[:] = self.img[:]
            np.clip(self.img2[:], x0, x1, out=self.img2[:])
            self.img2[:]-=x0
            self.img2[:]*=256.0/(x1-x0)            
            cv.imshow("Hist Demo", self.img2)            
            self.need_update = False

cv.namedWindow("Hist Demo", cv.CV_WINDOW_AUTOSIZE)
if __name__ == "__main__":
    p = HistDemo()
    p.configure_traits()