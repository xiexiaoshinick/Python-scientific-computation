# -*- coding: utf-8 -*-
from nlms_numpy import nlms
from nlms_common import *

def sim_signal_equalization(nlms_func, x, h0, D, step_size, noise_scale):
    d = x[:-D] 
    x = x[D:]
    y = np.convolve(x, h0)[:len(x)] 
    h = np.zeros(2*len(h0)+2*D, np.float64) 
    y += np.random.standard_normal(len(y)) * noise_scale    
    u = nlms_func(y, d, h, step_size)
    return h


def signal_equalization_test1():    
    import scipy.signal
    h0 = make_path(5, 64)
    D = 128
    length = 20000
    data = np.random.standard_normal(length+D)
    h = sim_signal_equalization(nlms, data, h0, D, 0.5, 0.1)
    pl.figure(figsize=(8,4))
    pl.plot(h0, label=u"未知系统")
    pl.plot(h, label=u"自适应滤波器")
    pl.plot(np.convolve(h0, h), label=u"二者卷积")
    #pl.title(u"信号均衡演示")
    pl.legend()
    w0, H0 = scipy.signal.freqz(h0, worN = 1000)
    w, H = scipy.signal.freqz(h, worN = 1000)
    pl.figure(figsize=(8,4))
    pl.plot(w0, 20*np.log10(np.abs(H0)), w, 20*np.log10(np.abs(H)))
    #pl.title(u"未知系统和自适应滤波器的振幅特性")
    pl.xlabel(u"圆频率")
    pl.ylabel(u"振幅(dB)") 
    
signal_equalization_test1()
pl.show()