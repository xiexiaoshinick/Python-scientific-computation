# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData 
from enthought.enable.component_editor import ComponentEditor 

from enthought.chaco.tools.api import PanTool, ZoomTool, DragZoom

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
        
        
        plot.tools.append(PanTool(plot))
        plot.tools.append(DragZoom(plot, drag_button="right", 
            maintain_aspect_ratio=False))        
        plot.overlays.append(ZoomTool(plot))
        
#        plot.overlays.append(ZoomTool(plot, tool_mode="range", axis = "index", 
#            always_on=True, always_on_modifier="control"))
        self.plot = plot
        self.data = data

if __name__ == "__main__":        
    p = LinePlot()
    p.configure_traits()