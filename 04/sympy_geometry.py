# -*- coding: utf-8 -*-
from sympy import *
from sympy.geometry import *
a = symbols("a", positive=True)
A = Point(0,0)
B = Point(5,0)
C = Point(3,2)

t = Triangle(A,B,C)
D = t.incenter

p = Circle(C, D, B)

i = Segment(*p.intersection(Line(A,B)))
j = Segment(*p.intersection(Line(A,C)))

print i.length.evalf(50)
print j.length.evalf(50)