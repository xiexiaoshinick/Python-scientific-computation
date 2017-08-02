# -*- coding: utf-8 -*-
"""
使用fsolve()计算非线性方程组的解。
"""
from scipy.optimize import fsolve
from math import sin

def f(x): 
    x0, x1, x2 = x.tolist() 
    return [
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2 - 1.5
    ]

# f计算方程组的误差，[1,1,1]是未知数的初始值
result = fsolve(f, [1,1,1]) 
print result
print f(result)