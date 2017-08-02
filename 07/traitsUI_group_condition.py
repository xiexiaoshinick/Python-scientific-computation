# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Int, Bool, Enum, Property
from enthought.traits.ui.api import View, HGroup, VGroup, Item

class Shape(HasTraits):
    shape_type = Enum("rectangle", "circle")
    editable = Bool
    x, y, w, h, r = [Int]*5
    
    view = View(
        VGroup(
            HGroup(Item("shape_type"), Item("editable")),
            VGroup(Item("x"), Item("y"), Item("w"), Item("h"), 
                visible_when="shape_type=='rectangle'", enabled_when="editable"),
            VGroup(Item("x"), Item("y"), Item("r"), 
                visible_when="shape_type=='circle'",  enabled_when="editable"),
        ), resizable = True)
    
if __name__ == "__main__":
    shape = Shape()
    shape.configure_traits()