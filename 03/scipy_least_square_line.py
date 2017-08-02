# -*- coding: utf-8 -*-
"""
使用最小二乘法对直线数据进行拟合。并使用Mayavi绘制误差平面。
"""

import numpy as np
from scipy.optimize import leastsq

X = np.array([ 8.19,  2.72,  6.39,  8.71,  4.7 ,  2.66,  3.78])
Y = np.array([ 7.01,  2.78,  6.47,  6.71,  4.1 ,  4.23,  4.05])

def residuals(p): 
    "计算以p为参数的直线和原始数据之间的误差"
    k, b = p
    return Y - (k*X + b)

# leastsq使得residuals()的输出数组的平方和最小，参数的初始值为[1,0]
r = leastsq(residuals, [1, 0]) 
k, b = r[0]
print "k =",k, "b =",b


#下面是绘图部分
import pylab as pl
from matplotlib.patches import Rectangle

pl.plot(X, Y, "o")
X0 = np.linspace(2, 10, 3)
Y0 = k*X0 + b
pl.plot(X0, Y0)

for x, y in zip(X, Y):
    y2 = k*x+b
    rect = Rectangle((x,y), abs(y-y2), y2-y, facecolor="red", alpha=0.2)
    pl.gca().add_patch(rect)

pl.gca().set_aspect("equal")
pl.show()

####### 误差曲面 #######
scale_k = 1.0
scale_b = 10.0
scale_error = 1000.0

def S(k, b):
    "计算直线y=k*x+b和原始数据X、Y的误差的平方和"
    error = np.zeros(k.shape)
    for x, y in zip(X, Y):
        error += (y - (k*x + b))**2
    return error

ks, bs = np.mgrid[k-scale_k:k+scale_k:40j, b-scale_b:b+scale_b:40j]

error = S(ks, bs)/scale_error

from enthought.mayavi import mlab
surf = mlab.surf(ks, bs/scale_b, error)
mlab.axes(xlabel="k", ylabel="b", zlabel="error", 
    ranges=[k-scale_k,k+scale_k,
            b-scale_b,b+scale_b,
            np.min(error)*scale_error, np.max(error)*scale_error])
mlab.outline(surf)
mlab.points3d([k],[b/scale_b],[S(k,b)/scale_error],scale_factor=0.1, color=(1,1,1))
mlab.show()
