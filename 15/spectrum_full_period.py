# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl

sampling_rate, fft_size = 8000, 512 
t = np.arange(0, 1.0, 1.0/sampling_rate) 
x = np.sin(2*np.pi*156.25*t)  + 2*np.sin(2*np.pi*234.375*t) 
xs = x[:fft_size]
xf = np.fft.rfft(xs)/fft_size 
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1) 
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100)) 
pl.figure(figsize=(8,4))
pl.subplot(211)
pl.plot(t[:fft_size], xs)
pl.xlabel(u"时间(秒)")
pl.subplot(212)
pl.plot(freqs, xfp)
pl.xlabel(u"频率(Hz)")
pl.subplots_adjust(hspace=0.4)
pl.show()