# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal

t = np.arange(0, 100)
x = np.sin(t)

N = 100
t2 = np.arange(0, 100, 1.0/N)
x2 = np.sin(t2)

x3 = np.zeros(len(x)*N)
x3[::N] = x

sinc = np.sinc(np.arange(-10, 10, 1.0/N))
sincw = sinc * signal.hann(len(sinc))

x4 = signal.lfilter(sinc, [1], x3)
x5 = signal.lfilter(sincw, [1], x3)

x4 = x4[len(sinc)/2:]
x5 = x5[len(sinc)/2:]

print np.sum((x2[10*N:90*N] - x4[10*N:90*N])**2)
print np.sum((x2[10*N:90*N] - x5[10*N:90*N])**2)
