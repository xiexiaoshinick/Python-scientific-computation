# -*- coding: utf-8 -*-
from scipy import signal
import pylab as pl
from numpy import *

fs = 8000.0 # 取样频率
fc = 1000.0  # 通带频率

# 频率为2kHz的3阶低通滤波器
b, a = signal.butter(3, 2*pi*fc, analog=1)

w, h = signal.freqs(b,a,worN=10000)
p = 20*log10(abs(h))

# 转换为取样频率为8kHz的数字滤波器
b2, a2 = signal.bilinear(b,a,fs=fs)

# 计算数字滤波器的频率响应
w2, h2 = signal.freqz(b2,a2,worN=10000)

# 计算增益特性
p2 = 20*log10(abs(h2))

# 找到增益为-3dB[精确值为： 10*log10(0.5)]的下标
idx = argmin(abs(p2-10*log10(0.5)))

# 输出增益为-3dB时的频率
print w2[idx]/2/pi*8000

# 输出公式 w = 2/T*arctan(wa*T/2) 计算的频率
print 2*fs*arctan(2*pi*fc/2/fs) /2/pi

#pl.plot(w/2/pi, p)
#pl.plot(w2/2/pi*fs,p2)
#pl.show()