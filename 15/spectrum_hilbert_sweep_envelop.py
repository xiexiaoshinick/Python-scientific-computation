# -*- coding: utf-8 -*-
from scipy import signal
from scipy import fftpack
import numpy as np
import pylab as pl

# 某个均衡滤波器的参数
a = np.array([1.0, -1.947463016918843, 0.9555873701383931])
b = np.array([0.9833716591860479, -1.947463016918843, 0.9722157109523452])

# 44.1kHz， 1秒的频率扫描波
t = np.arange(0, 0.5, 1/44100.0)
x= signal.chirp(t, f0=10, t1 = 0.5, f1=1000.0)

# 直接一次计算滤波器的输出
y = signal.lfilter(b, a, x)

hy = fftpack.hilbert(y)
pl.plot( np.sqrt(y**2 + hy**2),"r", linewidth=2) 
pl.plot(y)
pl.show()