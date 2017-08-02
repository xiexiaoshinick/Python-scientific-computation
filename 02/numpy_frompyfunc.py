# -*- coding: utf-8 -*-
"""
使用frompyfunc和vectorize将计算单个数值的函数转换成可以对数组
进行循环计算的函数。

"""
import numpy as np


def triangle_wave(x, c, c0, hc):
    x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    if x >= c: r = 0.0
    elif x < c0: r = x / c0 * hc
    else: r = (c-x) / (c-c0) * hc
    return r
        


x = np.linspace(0, 2, 1000)  
y1 = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])



triangle_ufunc1 = np.frompyfunc(triangle_wave, 4, 1)
y2 = triangle_ufunc1(x, 0.6, 0.4, 1.0)



triangle_ufunc2 = np.vectorize(triangle_wave, otypes=[np.float])
y3 = triangle_ufunc2(x, 0.6, 0.4, 1.0)

