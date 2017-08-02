# -*- coding: utf-8 -*-
"""
演示排序滤波。
"""
from scipy import signal
import numpy as np
import pylab as pl

t = np.arange(0, 20, 0.01)
x = (np.sin(t) + 2)* np.sin(100*t) 

x2 = signal.order_filter(x, np.ones(11), 10)

pl.plot(t, x)
pl.plot(t, x2)
pl.show()