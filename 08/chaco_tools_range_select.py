# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData, VPlotContainer
from enthought.enable.component_editor import ComponentEditor 


from enthought.chaco.tools.api import RangeSelection, RangeSelectionOverlay


class SelectionDemo(HasTraits):
    plot = Instance(VPlotContainer)
    data = Instance(ArrayPlotData)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False), 
        width=500, height=500, resizable=True, title=u"范围选择演示")

    def __init__(self, **traits):
        super(SelectionDemo, self).__init__(**traits)
        x = np.linspace(-140, 140, 1000)
        y = np.sin(x) * x**3 
        y /= np.max(y)
        data = ArrayPlotData(x=x, y=y) 
    
            
        self.plot1 = plot1 = Plot(data, padding=25) 
        self.line1 = line1 = plot1.plot(("x", "y"), type="line")[0]  
               
        self.select_tool = select_tool = RangeSelection(line1) 
        line1.tools.append( select_tool )
        select_tool.on_trait_change(self._selection_changed, "selection") 
        
        line1.overlays.append(RangeSelectionOverlay(component=line1)) 
        
        self.plot2 = plot2 = Plot(data, padding=25)
        plot2.plot(("x", "y"), type="line")[0]
            
        self.plot = VPlotContainer(plot2, plot1)
        

        self.data = data
    
    
    def _selection_changed(self):
        selection = self.select_tool.selection
        if selection != None:
            self.plot2.index_range.set_bounds(*selection) 
        else:
            self.plot2.index_range.reset()
    
    
if __name__ == "__main__":
    p = SelectionDemo()
    p.configure_traits()