# -*- coding: utf-8 -*-
import scipy.signal as signal
import pylab as pl
import numpy as np
from numpy.lib.stride_tricks import as_strided

sampling_rate = 8000.0
fft_size = 1024
step = fft_size/16 
time = 2

t = np.arange(0, time, 1/sampling_rate)
sweep = signal.chirp(t, f0=100, t1 = time, f1=0.8*sampling_rate/2, method="logarithmic")
number = (len(sweep)-fft_size)/step 
data = as_strided(sweep, shape=(number, fft_size), strides=(step*8, 8)) 

window = signal.hann(fft_size) 
data = data * window 

spectrogram = np.abs(np.fft.rfft(data, axis=1)) 
spectrogram /= fft_size/2
np.log10(spectrogram, spectrogram)
spectrogram *= 20.0

pl.figure(figsize=(8,4))
im = pl.imshow(spectrogram.T, origin = "lower", 
    extent=[0, 2, 0, sampling_rate/2], aspect='auto') 
bar = pl.colorbar(im, fraction=0.05)
bar.set_label(u"能量(dB)")
pl.xlabel(u"时间(秒)")
pl.ylabel(u"频率(Hz)")
pl.show()