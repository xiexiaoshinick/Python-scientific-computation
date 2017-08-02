# -*- coding: utf-8 -*-
from scipy import signal
import numpy as np
import matplotlib.pyplot as pl

pl.figure(figsize=(6,6))

b, a = signal.butter(6, 1.0, analog=1)
z,p,k = signal.tf2zpk(b, a)
pl.plot(np.real(p), np.imag(p), '^', label=u"6阶")

b, a = signal.butter(7, 1.0, analog=1)
z,p,k = signal.tf2zpk(b, a)
pl.plot(np.real(p), np.imag(p), 's', label=u"7阶")

pl.axis("equal")
pl.legend(loc="center right")
pl.show()

