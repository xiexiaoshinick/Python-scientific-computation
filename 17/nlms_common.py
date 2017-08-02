# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl

# 随机产生FIR滤波器的系数，长度为length， 延时为delay， 指数衰减
def make_path(delay, length):
   plen = length - delay
   h = np.zeros(length, np.float64)
   h[delay:] = np.random.standard_normal(plen) * np.exp( np.linspace(0, -4, plen) )
   h /= np.sqrt(np.sum(h*h))
   return h

def plot_converge(y, u, label=""):
    size = len(u)
    avg_number = 200
    e = np.power(y[:size] - u, 2)
    tmp = e[:int(size/avg_number)*avg_number]
    tmp.shape = -1, avg_number
    avg = np.average( tmp, axis=1 )
    pl.plot(np.linspace(0, size, len(avg)), 10*np.log10(avg), linewidth=2.0, label=label)

def diff_db(h0, h):
   return 10*np.log10(np.sum((h0-h)*(h0-h)) / np.sum(h0*h0))    