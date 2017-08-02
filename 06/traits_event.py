# -*- coding: utf-8 -*-
"""
演示Event类型
"""
from enthought.traits.api import HasTraits, Float, Event, on_trait_change

class Point(HasTraits): 
    x = Float(0.0)
    y = Float(0.0)
    updated = Event
            
    @on_trait_change( "x,y" )
    def pos_changed(self): 
        self.updated = True

    def _updated_fired(self): 
        self.redraw()
    
    def redraw(self): 
        print "redraw at %s, %s" % (self.x, self.y)
    
if __name__ == "__main__":
    p = Point()
    p.x = 1
    p.y = 1
    p.x = 1
    p.updated = True