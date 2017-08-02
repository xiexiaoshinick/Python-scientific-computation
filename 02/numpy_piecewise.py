# -*- coding: utf-8 -*-
"""
使用where, select, piecewise等计算三角波形的分段函数。
"""
import numpy as np


def triangle_wave(x, c, c0, hc):
    x = x - x.astype(np.int) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    return np.where(x>=c, 0, np.where(x<c0, x/c0*hc, (c-x)/(c-c0)*hc))



def triangle_wave2(x, c, c0, hc):
    x = x - x.astype(np.int)
    return np.select([x>=c, x<c0, True], [0, x/c0*hc, (c-x)/(c-c0)*hc])



def triangle_wave3(x, c, c0, hc):
    x = x - x.astype(np.int)
    return np.piecewise(x, 
        [x>=c, x<c0],
        [0,  # x>=c 
        lambda x: x/c0*hc, # x<c0
        lambda x: (c-x)/(c-c0)*hc])  # else


def triangle_wave4(x, c, c0, hc):
    """显示每个分段函数计算的数据点数"""
    def f1(x):
        print "f1:", x.shape
        return x/c0*hc
        
    def f2(x):
        print "f2:", x.shape
        return (c-x)/(c-c0)*hc
        
    x = x - x.astype(np.int)
    return np.piecewise(x, [x>=c, x<c0], [0, f1, f2])

x = np.linspace(0, 2, 1000) 
y = triangle_wave(x, 0.6, 0.4, 1.0)
y2 = triangle_wave2(x, 0.6, 0.4, 1.0)
y3 = triangle_wave3(x, 0.6, 0.4, 1.0)
y4 = triangle_wave4(x, 0.6, 0.4, 1.0)