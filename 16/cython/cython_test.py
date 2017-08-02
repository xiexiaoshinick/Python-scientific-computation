# -*- coding: utf-8 -*-
from timeit import timeit
from math import sin
import mylib as cy

def py_test1(xs):
    s = 0.0
    for x in xs:
        s += sin(x)**2
    return s
    
def py_test2(xs):
    return sum(sin(x)**2 for x in xs)
    
x = [t*0.01 for t in range(10000)]
    
if __name__ == "__main__":
    s = "from __main__ import x, py_test1, py_test2, cy"
    
    for f in ["py_test1", "py_test2", "cy.test1", "cy.test2", "cy.test3"]:
        print f, timeit("%s(x)" % f, s, number=100)
