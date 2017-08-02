# -*- coding: utf-8 -*-
import numpy as np
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData, HPlotContainer
from enthought.enable.component_editor import ComponentEditor 

from enthought.chaco.api import LassoOverlay 
from enthought.chaco.tools.api import LassoSelection
from enthought.kiva.agg import points_in_polygon

class LassoDemoPlot(HasTraits):
    plot = Instance(HPlotContainer) 
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False), 
        width=600, height=320, resizable=True, title="Lasso Tool Demo")

    def __init__(self):
        x, y = np.ogrid[-2*np.pi:2*np.pi:256j, -2*np.pi:2*np.pi:256j]
        self.img_data = np.sin(x)*y
        #self.img_mask = np.zeros((len(x), len(y[0]), 4), dtype=np.uint8)
        #self.img_mask[:, :, 3] = 255
        self.img_index = np.array(list((np.broadcast(y, x))))
        
        plotdata = ArrayPlotData(img_data=self.img_data, mask_data=self.img_data) 
        plot1 = Plot(plotdata, padding=10) 
        img_plot = plot1.img_plot("img_data",
            xbounds=(np.min(x), np.max(x)),
            ybounds=(np.min(y), np.max(y)))[0]
       
        self.lasso = LassoSelection(img_plot)
        img_plot.tools.append(self.lasso)
        self.ll = LassoOverlay(img_plot, lasso_selection=self.lasso)
        img_plot.overlays.append(self.ll)
        self.lasso.on_trait_change(self._selection_changed, 'selection_completed')
        
        plot2 = Plot(plotdata, padding=10)
        plot2.img_plot("mask_data")
       
        self.plot = HPlotContainer(plot1, plot2)
        self.plot1 = plot1
        self.plot2 = plot2
        self.plotdata = plotdata
        
    def _selection_changed(self):
        data = np.logical_not(points_in_polygon(self.img_index, self.lasso.dataspace_points, False).astype(np.bool))
        data = data.reshape((256, 256))
        copy = self.img_data.copy()
        copy[data] = 0
        self.plotdata["mask_data"] = copy
        self.plot2.request_redraw()
        # self.img_mask[:, :, :3] = 0
        # gc = GraphicsContext(self.img_mask)
        # gc.set_stroke_color((1,1,1,1))
        # gc.set_fill_color((1,1,1,1))        
        # for selection in self.lasso.disjoint_selections:
            # screen_pts = selection
            # gc.move_to(*screen_pts[0])
            # for i in xrange(1, len(screen_pts)):
                # gc.line_to(*screen_pts[i])
            # gc.fill_path()
        # self.plotdata["mask_data"] = self.img_mask[:, :, 0]
        #self.plot2.request_redraw()

p = LassoDemoPlot()
p.configure_traits()