# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats
import pylab as pl

_lambda = 10
time = 1000
pl.figure(figsize=(10,4))
t = np.random.rand(_lambda*time)*time
t.sort()
for i, k in enumerate([1,2]):
    interval = t[k:] - t[:-k]
    dist, interval_edges = np.histogram(interval, bins=100, normed=True)
    x = (interval_edges[1:] +interval_edges[:-1])/2
    gamma = stats.gamma.pdf(x, k, scale=1.0/_lambda)
    pl.subplot(121+i)
    pl.plot(x, dist,  lw=2, label=u"统计结果")
    pl.plot(x, gamma, lw=2, label=u"伽玛分布", color="red")
    pl.xlabel(u"时间间隔")
    pl.ylabel(u"概率密度")
    pl.title(u"k = %d" % k)
    pl.legend()
pl.subplots_adjust(0.1, 0.15, 0.95, 0.90, 0.2, 0.1)    
pl.show()