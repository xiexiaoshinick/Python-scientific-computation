# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl

# 某个均衡滤波器的参数
a = np.array([1.0, -1.947463016918843, 0.9555873701383931])
b = np.array([0.9833716591860479, -1.947463016918843, 0.9722157109523452])

impulse = np.zeros(1000)
impulse[0] = 1
h = signal.lfilter(b, a, impulse)
print h[-1]

pl.plot(h)
pl.show()