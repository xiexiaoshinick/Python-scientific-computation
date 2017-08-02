# -*- coding: utf-8 -*-
"""
使用Chaco的绘图组件绘制多条曲线
"""
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.enable.component_editor import ComponentEditor

class MutiLinePlot(HasTraits):
    plot = Instance(Plot)
    data = Instance(ArrayPlotData)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")
        
    
    def __init__(self, **traits):
        super(MutiLinePlot, self).__init__(**traits)
        x = np.linspace(-14, 14, 100)
        y1 = np.sin(x) * x**3
        y2 = np.cos(x) * x**3
        data = ArrayPlotData(x=x, y1=y1, y2=y2)
        plot = Plot(data)
        plot.plot(("x", "y1"), type="line", color="blue", name="sin(x) * x**3") 
        plot.plot(("x", "y2"), type="line", color="red", name="cos(x) * x**3")
        plot.plot(("x", "y2"), type="scatter", color="red", marker = "circle", 
                  marker_size = 2, name="cos(x) * x**3 points")
        plot.title = "Multiple Curves"
        plot.legend.visible = True 
        self.plot = plot
        self.data = data
        

if __name__ == "__main__":
    p = MutiLinePlot()        
    p.configure_traits()
