# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats
import pylab as pl

_lambda = 10.0
x = np.arange(20)
pl.figure(figsize=(10,4))
for i, n in enumerate([100, 1000]):
    pl.subplot(121+i)
    y1 = stats.binom.pmf(x, n, _lambda/n)
    y2 = stats.poisson.pmf(x, _lambda)
    pl.plot(x, y1, label=u"binom", lw=2)
    pl.plot(x, y2, label=u"poisson", lw=2, color="red")
    pl.xlabel(u"次数")
    pl.ylabel(u"概率")
    pl.title("n=%d" % n)
    pl.legend()

pl.subplots_adjust(0.1, 0.15, 0.95, 0.90, 0.2, 0.1)
pl.show()