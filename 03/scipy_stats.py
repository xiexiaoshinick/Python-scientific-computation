# -*- coding: utf-8 -*-
"""
演示stats模块的概率密度函数、直方图统计和累积分布函数。
"""
from scipy import stats
import numpy as np
import pylab as pl

print stats.norm.stats()
X = stats.norm(1.0, 2.0)
print X.stats()

x = X.rvs(size=10000)
print np.mean(x), np.var(x)

t = np.arange(-10, 10, 0.1)

pl.figure(figsize=(8, 3))
pl.subplot(121)
pl.plot(t, X.pdf(t))
p, t2 = np.histogram(x, bins=100, normed=True)
t2 = (t2[:-1] + t2[1:])/2
pl.plot(t2, p)

pl.subplot(122)
pl.plot(t, X.cdf(t))
pl.plot(t2, np.add.accumulate(p)*(t2[1]-t2[0]))
pl.show()
