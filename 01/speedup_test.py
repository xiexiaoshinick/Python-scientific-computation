# -*- coding: utf-8 -*-
"""
载入几个重量级的扩展库。在IPython中使用run命令可以缩短
第二次运行程序启动时间。
"""
import numpy as np
from scipy import signal
import pylab as pl

t = np.linspace(0, 10, 1000)
x = signal.chirp(t, 5, 10, 30)
pl.plot(t, x)
pl.show()