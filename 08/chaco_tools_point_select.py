# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance, Enum, List
from enthought.traits.ui.api import View, Item, HSplit, VGroup, Heading
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.enable.component_editor import ComponentEditor 


from enthought.chaco.api import ScatterInspectorOverlay
from enthought.chaco.tools.api import ScatterInspector



Colors = {
    "green":(0, 1, 0, 0.5),
    "red":(1, 0, 0, 0.5)
}



class PointSelectionDemo(HasTraits):
    color = Enum(Colors.keys())
    green_selection = List()
    red_selection = List()
    plot = Instance(Plot) 
    data = Instance(ArrayPlotData)
    
    
    traits_view = View(
        HSplit(
            Item('plot',editor=ComponentEditor(), show_label=False), 
            VGroup(
                Item("color", show_label=False, style="custom"),
                Heading(u"绿色选择点"),
                Item("green_selection", show_label=False, style="readonly"),
                Heading(u"红色选择点"),
                Item("red_selection", show_label=False, style="readonly"),
            )
        ),
        width=800, height=400, resizable=True, title=u"数据点选择演示")
        
    def __init__(self, **traits):
        super(PointSelectionDemo, self).__init__(**traits)
        x = np.random.rand(100)
        y = np.random.rand(100)
        data = ArrayPlotData(x=x, y=y)
        
        
        plot = Plot(data, padding=25) 
        self.scatter = scatter = plot.plot(("x", "y"), type="scatter", marker_size=4)[0] 
        
        self.select_tools = {}
        for i, c in enumerate(Colors.keys()):
            hover_name = "hover_%s" % c
            selection_name = "selections_%s" % c
            self.select_tools[c] = ScatterInspector(scatter,  
                hover_metadata_name=hover_name, 
                selection_metadata_name=selection_name)
             
            scatter.overlays.append(ScatterInspectorOverlay(scatter,  
                hover_metadata_name = hover_name,
                selection_metadata_name=selection_name,
                hover_color = "transparent",
                hover_outline_color = c,
                hover_marker_size = 6,
                hover_line_width = 1,
                selection_color = Colors[c],
            ))            
            
        scatter.active_tool = self.select_tools[self.color] 
        scatter.index.on_trait_change(self.selection_changed, 'metadata_changed') 
        self.plot = plot
        self.data = data
        
     
    
    def _color_changed(self):
        self.scatter.active_tool = self.select_tools[self.color]
    
    
    def selection_changed(self):
        x = self.scatter.index.get_data() 
        y = self.scatter.value.get_data() 
        metadata = self.scatter.index.metadata
        selection = metadata.get("selections_green", []) 
        self.green_selection = ["%d, (%f, %f)" % (s, x[s], y[s]) for s in selection]
        selection = metadata.get("selections_red", []) 
        self.red_selection = ["%d, (%f, %f)" % (s, x[s], y[s]) for s in selection]
    
    
if __name__ == "__main__":    
    p = PointSelectionDemo()
    p.configure_traits()