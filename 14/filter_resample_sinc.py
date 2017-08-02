# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl

t = np.arange(0, 10, 0.01)
x = np.zeros(len(t))

delay = [3,4,5,6]
gain = [1.0, 0.5, 0.3, -0.2]

for d, g in zip(delay, gain):
    tmp = g*np.sinc(t-d)
    pl.plot(t, tmp, "--")
    x += tmp

pl.plot(t, x, "b", linewidth=2)
pl.plot(delay, gain, "o")
pl.vlines(delay, [0], gain, linewidth=2)
pl.show()