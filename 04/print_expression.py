# -*- coding: utf-8 -*-
from sympy import *

def print_expression(e, level=0):
    spaces = "    "*level
    if isinstance(e, (Symbol, Number)):
        print spaces + str(e)
        return
    if len(e.args) > 0:
        print spaces + e.func.__name__
        for arg in e.args:
            print_expression(arg, level+1)
    else:
        print spaces + e.func.__name__

        
if __name__ == "__main__":
    x, y = symbols('x,y')
    e = sqrt(x**2 + y**2)
    print_expression(e)
