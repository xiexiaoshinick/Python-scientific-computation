# -*- coding: utf-8 -*-
"""
使用容器组件对绘图组件进行排版
"""
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import (HPlotContainer, VPlotContainer, 
        OverlayPlotContainer, ArrayPlotData, Plot)
from enthought.enable.component_editor import ComponentEditor

class ContainerExample(HasTraits):
    plot = Instance(VPlotContainer)
    data = Instance(ArrayPlotData)
    traits_view = View(Item('plot', editor=ComponentEditor(), show_label=False),
                       width=1000, height=600, resizable=True, title="Chaco Plot")
                       
    def __init__(self, **traits):
        super(ContainerExample, self).__init__(**traits)
        x = np.linspace(-14, 14, 100)
        y = np.sin(x) * x**3 / 1000
        data = ArrayPlotData(x=x, y=y)
        
        
        p1 = Plot(data, padding=30)
        p1.plot(("x", "y"), type="scatter", color="blue")
        p1.plot(("x", "y"), type="line", color="blue")
        
        p2 = Plot(data, padding=30)
        p2.plot(("x", "y"), type="line", color="blue")
        p2.set(bounds = [200, 100], position = [70,150],  
        bgcolor = (0.9,0.9,0.9), unified_draw=True, resizable="")
        
        p3 = Plot(data, padding=30)
        p3.plot(("x", "y"), type="line", color="blue", line_width=2.0)
        
        p4 = Plot(data,  padding=30)
        p4.plot(("x", "y"), type="scatter", color="red", marker="circle")
        
        c1 = OverlayPlotContainer(p1, p2) 
        
        c1.fixed_preferred_size = p3.get_preferred_size() 
        c2 = HPlotContainer(c1, p3) 
        c3 = VPlotContainer(p4, c2) 
        
        self.plot = c3
        
        
if __name__ == "__main__":
    p = ContainerExample()
    p.configure_traits()
