# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance, Float
from enthought.traits.ui.api import View, Item, Handler
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.enable.component_editor import ComponentEditor


from enthought.pyface.timer.api import Timer



class AnimationHandler(Handler): 
    def init(self, info):
        super(AnimationHandler, self).init(info)
        info.object.timer = Timer(10, info.object.on_timer) 
    
    def closed(self, info, is_ok):
        super(AnimationHandler, self).closed(info, is_ok)
        info.object.timer.Stop() 
        
class AnimationPlot(HasTraits):
    plot = Instance(Plot)
    data = Instance(ArrayPlotData)
    phase = Float(0)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Plot Animation",
        handler = AnimationHandler()) 

    def __init__(self, **traits):
        super(AnimationPlot, self).__init__(**traits)
        data = ArrayPlotData(x=[0], y=[0])
        plot = Plot(data)
        plot.plot(("x", "y"), type="line", color="blue")
        plot.title = "sin(x)"
        self.plot = plot
        self.data = data
        
    def on_timer(self): 
        x = np.linspace(self.phase, self.phase+np.pi*4, 100)
        y = np.sin(x)
        self.phase += 0.02        
        self.data["x"] = x 
        self.data["y"] = y

if __name__ == "__main__":        
    p = AnimationPlot()
    p.configure_traits()