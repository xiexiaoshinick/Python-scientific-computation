# -*- coding: utf-8 -*-
"""
使用数值积分计算圆的面积和球的体积。
"""
import numpy as np
from scipy import integrate

def half_circle(x):
    return (1-x**2)**0.5
    
def half_sphere(x, y):
    return (1-x**2-y**2)**0.5    
    
N = 10000
x = np.linspace(-1, 1, N)
dx = 2.0/N
y = half_circle(x)
print u"矩形法求圆的面积:", dx * np.sum(y[:-1] + y[1:]) # 面积的两倍    
print u"trapz求圆的面积:", np.trapz(y, x) * 2

pi_half, err = integrate.quad(half_circle, -1, 1)
print u"integrate求圆的面积:", pi_half*2

v, err = integrate.dblquad(half_sphere, -1, 1, 
        lambda x:-half_circle(x), 
        lambda x:half_circle(x))
        
print u"integrate求球的体积:", 2*v
print u"球的体积的理论值:", np.pi*4/3