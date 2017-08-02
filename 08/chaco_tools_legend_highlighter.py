# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData 
from enthought.enable.component_editor import ComponentEditor 
from enthought.chaco.tools.api import LegendHighlighter

class LinePlot(HasTraits):
    plot = Instance(Plot) 
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False), 
        width=500, height=500, resizable=True, title="Chaco Plot")

    def __init__(self):
        x = np.linspace(-14, 14, 100)
        y = np.sin(x) * x**3
        y2 = np.cos(x) * x**3
        plotdata = ArrayPlotData(x=x, y=y, y2=y2) 
        plot = Plot(plotdata) 
        plot.plot(("x", "y"), type="line", color="blue", name="sin")
        plot.plot(("x", "y2"), type="line", color="red", name="cos")
        #line.index.sort_order = "ascending"
        plot.title = "sin(x) * x^3" 
        plot.legend.visible = True
        plot.legend.tools.append(LegendHighlighter(plot.legend))
        
        self.plot = plot
        self.plotdata = plotdata

p = LinePlot()
p.configure_traits()