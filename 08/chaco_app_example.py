# -*- coding: utf-8 -*-
"""
演示如何将Chaco绘图组件嵌入TraitsUI界面中。
"""
import numpy as np
from enthought.traits.api import HasTraits, Instance, Color
from enthought.traits.ui.api import View, Group, Item
from enthought.enable.component_editor import ComponentEditor
from enthought.chaco.api import Plot, ArrayPlotData


from enthought.chaco.api import marker_trait
class ScatterPlotTraits(HasTraits):
    plot = Instance(Plot)
    data = Instance(ArrayPlotData)
    color = Color("blue")   
    marker = marker_trait   

    traits_view = View(
        Group(Item('color', label="Color"),
              Item('marker', label="Marker"),
              Item('object.line.marker_size', label="Size"), 
              Item('plot', editor=ComponentEditor(), show_label=False),
                   orientation = "vertical"),
              width=800, height=600, resizable=True, title="Chaco Plot")

    def __init__(self, **traits):
        super(ScatterPlotTraits, self).__init__(**traits)
        x = np.linspace(-14, 14, 100)
        y = np.sin(x) * x**3
        data = ArrayPlotData(x = x, y = y)
        plot = Plot(data)

        self.line = plot.plot(("x", "y"), type="scatter", color="blue")[0] 
        self.plot = plot
        self.data = data

    def _color_changed(self):
        self.line.color = self.color 

    def _marker_changed(self):
        self.line.marker = self.marker

if __name__ == "__main__":
    p = ScatterPlotTraits()
    p.configure_traits()
