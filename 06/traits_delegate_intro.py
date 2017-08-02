# -*- coding: utf-8 -*-
"""
比较代理类型和原型类型的区别
"""
from enthought.traits.api import HasTraits, Int, Instance, DelegatesTo, PrototypedFrom

class Point(HasTraits):
    x = Int
    y = Int
    
class Circle(HasTraits):
    center = Instance(Point)    
    x = DelegatesTo("center")    
    y = PrototypedFrom("center")    
    r = Int
    
p = Point()
c = Circle()
c.center = p
    
if __name__ == "__main__":
    p.x = 10
    print c.x
    p.y = 100
    print c.y
    c.x = 20
    print p.x
    c.y = 200
    print p.y
    p.y = 300
    print c.y