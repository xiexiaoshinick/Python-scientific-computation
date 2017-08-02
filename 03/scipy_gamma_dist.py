# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import pylab as pl


parameters = [(1,2),(2,2),(3,2),(5,1),(9,0.5)]
x = np.linspace(0, 20, 1000)

for p in parameters:
    y = stats.gamma.pdf(x, p[0], scale=p[1])
    pl.plot(x, y, label="k=%d, theta=%.1f" % (p))
pl.legend()
pl.show()