# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData 
from enthought.enable.component_editor import ComponentEditor 

class LinePlot(HasTraits):
    plot = Instance(Plot) 
    data = Instance(ArrayPlotData)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False), 
        width=500, height=500, resizable=True, title="Chaco Plot")

    def __init__(self, **traits):
        super(LinePlot, self).__init__(**traits)
        x = np.linspace(-14, 14, 100)
        y = np.sin(x) * x**3
        data = ArrayPlotData(x=x, y=y) 
        plot = Plot(data) 
        plot.plot(("x", "y"), type="line", color="blue") 
        plot.title = "sin(x) * x^3" 
        self.plot = plot
        self.data = data

if __name__ == "__main__":        
    p = LinePlot()
    p.configure_traits()