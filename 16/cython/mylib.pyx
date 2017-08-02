from math import sin as pysin
cdef extern from "math.h":
    double sin(double x)
  
def test1(xs):
    s = 0.0
    for x in xs:
        s += pysin(x)**2
    return s

def test2(xs):
    s = 0.0
    for x in xs:
        s += sin(x)**2
    return s
    
def test3(xs):
    cdef double s = 0.0
    for x in xs:
        s += sin(x)**2
    return s    