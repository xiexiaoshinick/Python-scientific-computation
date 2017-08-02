# -*- coding: utf-8 -*-
"""
演示中值滤波。
"""
from scipy import signal
import numpy as np
import pylab as pl

t = np.arange(0, 20, 0.1)
x = np.sin(t)
x[np.random.randint(0, len(t), 20)] += np.random.standard_normal(20)*0.6
x2 = signal.medfilt(x, 5)

pl.plot(t, x)
pl.plot(t,x2+0.5)

x3 = signal.order_filter(x, np.ones(5), 2)
print np.all(x2==x3)
pl.show()