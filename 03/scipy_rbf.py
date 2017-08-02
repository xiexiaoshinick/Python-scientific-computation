# -*- coding: utf-8 -*-
"""
演示径向基函数(radial basis function, 简称RBF)插值算法。
"""
import numpy as np
from scipy import interpolate
import pylab as pl


def func(x,y):
    return (x+y)*np.exp(-5.0*(x**2 + y**2))

# 计算曲面函数上100个随机分布的点
x = np.random.uniform(-1.0, 1.0, size=100)
y = np.random.uniform(-1.0, 1.0, size=100)
fvals = func(x,y) 

# 使用Rbf进行插值运算
newfunc = interpolate.Rbf(x, y, fvals, function='multiquadric') 
ynew, xnew = np.mgrid[-1:1:100j, -1:1:100j] # 插值结果的网格
fnew = newfunc(xnew, ynew) 
truevals = func(xnew, ynew) # 函数的真实值


pl.subplot(121)
pl.imshow(truevals,extent=[-1,1,-1,1], cmap=pl.cm.jet, origin="lower")
pl.subplot(122)
pl.scatter(x,y,20,fvals,cmap=pl.cm.jet)
pl.imshow(fnew,extent=[-1,1,-1,1], cmap=pl.cm.jet, origin="lower")
pl.show()