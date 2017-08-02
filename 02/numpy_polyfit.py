# -*- coding: utf-8 -*-
"""
使用多项式函数拟合正弦波，并显示拟合误差。
"""
import numpy as np
import pylab as pl
pl.figure(figsize=(8,4))

x = np.linspace(-np.pi/2, np.pi/2, 1000) 
y = np.sin(x) 

for deg in [3,5,7]:
    a = np.polyfit(x, y, deg) 
    error = np.abs(np.polyval(a, x)-y) 
    print "poly %d:" % deg, a
    print "max error of order %d:" % deg , np.max(error)
    
    pl.semilogy(x, error, label=u"%d阶多项式的误差" % deg)
pl.legend(loc=3)
pl.axis('tight')
pl.show()    