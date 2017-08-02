# -*- coding: utf-8 -*-
"""
使用fsolve()计算非线性方程组的解。
并且使用计算雅可比行列式的函数。
"""
from scipy.optimize import fsolve
from math import sin,cos
def f(x):
    x0, x1, x2 = x.tolist()
    return [
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2 - 1.5
    ]
    
def j(x): 
    x0, x1, x2 = x.tolist()
    return [
        [0, 5, 0],
        [8*x0, -2*x2*cos(x1*x2), -2*x1*cos(x1*x2)],
        [0, x2, x1]
    ]
 
result = fsolve(f, [1,1,1], fprime=j) 

print result
print f(result)
