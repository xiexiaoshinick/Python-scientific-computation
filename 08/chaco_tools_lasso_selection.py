# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData, HPlotContainer
from enthought.enable.component_editor import ComponentEditor 


from enthought.chaco.api import LassoOverlay 
from enthought.chaco.tools.api import LassoSelection

N = 300

class LassoDemoPlot(HasTraits):
    plot = Instance(HPlotContainer) 
    data = Instance(ArrayPlotData)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False), 
        width=600, height=320, resizable=True, title="Lasso Tool Demo")

    def __init__(self, **traits):
        super(LassoDemoPlot, self).__init__(**traits)
        x = np.random.random(N)
        y = np.random.random(N)
        x2 = np.array([])
        y2 = np.array([])
   
        data = ArrayPlotData(x=x, y=y, x2=x2, y2=y2) 
        
        
        plot1 = Plot(data, padding=10) 
        scatter_plot1 = plot1.plot(("x", "y"), type="scatter", marker="circle", color="blue")[0]
       
        self.lasso = LassoSelection(scatter_plot1, incremental_select=True,  
            selection_datasource=scatter_plot1.index)
        self.lasso.on_trait_change(self._selection_changed, 'selection_changed') 
        scatter_plot1.tools.append(self.lasso)
        scatter_plot1.overlays.append(LassoOverlay(scatter_plot1, lasso_selection=self.lasso)) 
        
        plot2 = Plot(data, padding=10)
        plot2.index_range = plot1.index_range
        plot2.value_range = plot1.value_range
        plot2.plot(("x2", "y2"), type="scatter", marker="circle", color="red")
        
        
        self.plot = HPlotContainer(plot1, plot2)
        self.plot2 = plot2
        self.data = data
        
    
    def _selection_changed(self):
        index = np.array(self.lasso.selection_datasource.metadata["selection"], dtype=np.bool)
        self.data["x2"] = self.data["x"][index]
        self.data["y2"] = self.data["y"][index]
    

if __name__ == "__main__":    
    p = LassoDemoPlot()
    p.configure_traits()