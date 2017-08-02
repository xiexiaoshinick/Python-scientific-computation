# -*- coding: utf-8 -*-

import numpy as np
import scipy.weave as weave
from scipy.weave import converters
from enthought.traits.api import (HasTraits, Instance, Float, Enum, List, Any, 
    Bool, Str, Property, on_trait_change)
from enthought.traits.ui.api import View, Item, EnumEditor, HGroup, VGroup
from enthought.enable.api import ComponentEditor
from enthought.chaco.api import ArrayPlotData, Plot, AbstractController, reverse, Blues, DataRange1D
import enthought.chaco.default_colormaps as cmaps
      
def weave_mandelbrot(cx, cy, d, arr):
    cx = float(cx)
    cy = float(cy)
    d = float(d)
    code = """
    double x, y;
    int h = Narr[0];
    int w = Narr[1];
    double dx = 2*d / (double)w;
    y = cy-d*(double)h/w;    
    for(int i=0;i<h;i++)
    {
        x = cx-d; 
        for(int j=0;j<w;j++)
        {
            int k;
            double zx, zy;
            zx = x; zy = y;
            for(k=1;k<100;k++)
            {
                double tx, ty;
                if(zx*zx + zy*zy > 4) break;
                tx = zx*zx - zy*zy + x;
                ty = 2*zx*zy + y;
                zx = tx;
                zy = ty;
            }
            double absz = sqrt(zx*zx + zy*zy);
            if(absz>2.0) arr(i,j) = k - log(log(absz)/log(2))/log(2);
            else arr(i,j) = k;
            x += dx;
        }
        y += dx;
    }
    """
    weave.inline(code, ["cx", "cy", "d", "arr"], compiler="gcc", 
                 type_converters=converters.blitz)
    
class MandelbrotController(AbstractController):
    application = Instance("MandelbrotDemo")
    event_state = Enum("normal", "moving")
    start_x = Float
    start_y = Float
    
    def normal_left_down(self, evt):
        self.event_state = "moving"
        self.start_x = evt.x
        self.start_y = evt.y

    def moving_mouse_move(self, evt):
        app = self.application
        dx = evt.x - self.start_x
        dy = evt.y - self.start_y
        app.cx -= dx/float(self.component.x2)*2*app.d
        app.cy -= dy/float(self.component.y2)*2*app.d
        self.start_x = evt.x
        self.start_y = evt.y
        app.update_plot()
        
    def moving_left_up(self, evt):
        self.event_state = "normal"
        
    def normal_mouse_wheel(self, evt):
        app = self.application
        x0, x1, y0, y1 = app.cx-app.d, app.cx+app.d, app.cy-app.d, app.cy+app.d
        x = x0 + evt.x/float(self.component.x2)*2*app.d
        y = y0 + evt.y/float(self.component.y2)*2*app.d
        if evt.mouse_wheel < 0:
            d2 = app.d * 1.2
        else:
            d2 = app.d / 1.2
        scale = d2/app.d
        app.cx = (2*x+(x0+x1-2*x)*scale)/2
        app.cy = (2*y+(y0+y1-2*y)*scale)/2
        app.d = d2
        app.update_plot()
    
class MandelbrotDemo(HasTraits):
    plot = Instance(Plot)
    imgplot = Any
    data = Instance(ArrayPlotData)
    cx = Float(0)
    cy = Float(0)
    d = Float(1.5)
    width = Property(depends_on="imgplot.x2")
    height = Property(depends_on="imgplot.y2")
    color_maps = List
    current_map = Str("Blues")
    reverse_map = Bool(True)
    position = Property(depends_on="cx,cy,d")
    
    def _get_width(self):
        return self.imgplot.x2
    
    def _get_height(self):
        return self.imgplot.y2
    
    def _color_maps_default(self):
        return [x.__name__ for x in cmaps.color_map_functions]
    
    def default_traits_view(self):
        view = View(
            VGroup(
                HGroup(
                    Item("current_map", label=u"颜色映射", editor=EnumEditor(name="object.color_maps")),
                    Item("reverse_map", label=u"反转颜色"),
                    Item("position", label=u"位置", style="readonly"),
                ),
                Item("plot", show_label=False, editor=ComponentEditor()),
            ),
            resizable = True,
            width = 550, height = 300,
            title = u"Mandelbrot观察器"
        )
        return view
    
    def _get_position(self):
        return "X:%f Y:%f d:%f" % (self.cx, self.cy, self.d)
    
    @on_trait_change("reverse_map,current_map")
    def change_color_map(self):
        try:
            cmap_func = getattr(cmaps, self.current_map)
            if self.reverse_map:
                cmap_func = reverse(cmap_func)
            self.imgplot.color_mapper = cmap_func(DataRange1D(self.imgplot.value))
            self.plot.request_redraw()
        except:
            print "Cannot set color map:%s" % self.current_map
    
    def __init__(self, **traits):
        super(MandelbrotDemo, self).__init__(**traits)
        self.data = ArrayPlotData(image=np.zeros((1, 1)))
        self.plot = Plot(self.data, padding=0)
        imgplot = self.plot.img_plot("image", colormap=reverse(Blues), interpolation="bilinear")[0]
        imgplot.tools.append( MandelbrotController(imgplot, application=self) )
        self.imgplot = imgplot
        self.plot.x_axis.visible = False
        self.plot.y_axis.visible = False
        
    @on_trait_change("imgplot.bounds")
    def update_plot(self):
        arr = self.data["image"]
        if arr.shape[0] != self.height or arr.shape[1] != self.width:
            arr = np.empty((self.height, self.width))
        weave_mandelbrot(self.cx, self.cy, self.d, arr)
        self.data["image"] = arr
        
demo = MandelbrotDemo()
demo.configure_traits()