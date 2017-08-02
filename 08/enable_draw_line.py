# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Instance, List, Enum, Float, Int, Color, Tuple
from enthought.traits.ui.api import Item, View, HGroup
from enthought.enable.api import ComponentEditor, Component

def convert_color(c):
    if c.__class__.__name__ == "QColor":
        return (c.red()/255.0, c.green()/255.0, c.blue()/255.0)
    else:
        return (c[0]/255.0, c[1]/255.0, c[2]/255.0)

class Line(HasTraits):
    x0 = Float
    y0 = Float
    x1 = Float
    y1 = Float
    width = Int
    color = Tuple
       
class DrawLineComponent(Component):
    line_width = Enum(1,2,3,4,5,6,7)
    line_color = Color((0,0,0))
    lines = List(Line)
    event_state = Enum("normal", "line")
       
    def _draw_overlay(self, gc, view_bounds=None, mode="normal"):
        gc.save_state()
        for line in self.lines:
            gc.set_line_width(line.width)
            gc.set_stroke_color(line.color)            
            gc.move_to(line.x0, line.y0)
            gc.line_to(line.x1, line.y1)
            gc.draw_path()
        gc.restore_state()
        
    def normal_left_down(self, event):
        self.lines.append(
            Line(x0=event.x, y0=event.y, x1=event.x, y1=event.y, 
            width=self.line_width, color=convert_color(self.line_color)))
        self.event_state = "line"
        self.request_redraw()
        
    def line_mouse_move(self, event):
        self.lines[-1].set(x1 = event.x, y1 = event.y)
        self.request_redraw()
        
    def line_left_up(self, event):
        self.event_state = "normal"

class EnableDemo(HasTraits):
    box = Instance(DrawLineComponent)
    
    view = View(
        HGroup(Item("object.box.line_width"),
               Item("object.box.line_color", style="custom")),
        Item("box", editor=ComponentEditor(),show_label=False),
        resizable=True,
        width = 500, 
        height = 500,
        title = "Draw Lines"
    )
    
    def __init__(self, **traits):
        super(EnableDemo, self).__init__(**traits)
        self.box = DrawLineComponent()
 
if __name__ == "__main__": 
    p = EnableDemo()
    p.configure_traits()