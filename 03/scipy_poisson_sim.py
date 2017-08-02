# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats
import pylab as pl

_lambda = 10
pl.figure(figsize=(10,4))
for i, time in enumerate([1000, 50000]):
    t = np.random.rand(_lambda*time)*time
    count, time_edges = np.histogram(t, bins=time, range=(0,time))
    dist, count_edges = np.histogram(count, bins=20, range=(0,20), normed=True)
    x = count_edges[:-1]
    poisson = stats.poisson.pmf(x, _lambda)
    pl.subplot(121+i)
    pl.plot(x, dist, "-o", lw=2, label=u"统计结果")
    pl.plot(x, poisson, "->", lw=2, label=u"泊松分布", color="red")
    pl.xlabel(u"次数")
    pl.ylabel(u"概率")
    pl.title(u"time = %d" % time)
    pl.legend(loc="lower center")
pl.subplots_adjust(0.1, 0.15, 0.95, 0.90, 0.2, 0.1)    
pl.show()