# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import pylab as pl

t = np.arange(-1, 1, 0.01)
x = np.sin(np.pi*t+2) + np.random.randn(len(t))*0.05 

[b,a] = signal.butter(3, 0.05)
z = signal.lfilter(b, a, x)
y = signal.filtfilt(b, a, x)

pl.figure(figsize=(8,4))
pl.plot(x, label=u"原始数据")
pl.plot(z, label=u"lfilter滤波")
pl.plot(y, label=u"filtfilt滤波")
pl.legend()
pl.show()