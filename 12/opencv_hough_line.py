# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl

k = 1.2
b = 3

xn, yn = 4, 3

pl.figure(figsize=(8,3))
xs = np.linspace(0,5,4)
ys = xs*k + b


pl.subplot(121)
for x0,y0 in zip(xs, ys):
    pl.plot(x0, y0, "o")
    
pl.plot(xn, yn, ">")
    
pl.subplot(122)
theta = np.linspace(0, np.pi, 100)
for x0,y0 in zip(xs, ys):
    r = x0*np.cos(theta)+y0*np.sin(theta)
    pl.plot(theta, r)

r = xn*np.cos(theta)+yn*np.sin(theta)
pl.plot(theta, r, "--")
pl.xlim(0, np.max(theta))
pl.show()