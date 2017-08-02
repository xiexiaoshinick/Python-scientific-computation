# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import pylab as pl

b, a = signal.butter(2, 1.0, analog=1) 

# 低通->带通的频率变换函数
w1 = 1.0 # 低通带频率
w2 = 2.0 # 高通带频率
dw = w2 - w1 # 通带宽度
w0 = np.sqrt(w1*w2) # 通带中心频率

# 产生10**-2到10**2的频率点
w = np.logspace(-2, 2, 1000) 

# 使用频率变换公式计算出转换之后的频率
nw = np.imag(w0/dw*(1j*w/w0 + w0/(1j*w))) 

_, h = signal.freqs(b, a, worN=nw) 
h = 20*np.log10(np.abs(h))

pl.figure(figsize=(8,5))

pl.subplot(221)
pl.semilogx(w, nw) # X轴使用log坐标绘图
pl.xlabel(u"变换前圆频率(弧度/秒)")
pl.ylabel(u"变换后圆频率(弧度/秒)")

pl.subplot(222)
pl.plot(h, nw)
pl.xlabel(u"低通滤波器的频率响应(dB)")

pl.subplot(212)
pl.semilogx(w, h) 
pl.xlabel(u"变换前圆频率(弧度/秒)")
pl.ylabel(u"带通滤波器的频率响应(dB)")

pl.subplots_adjust(wspace=0.3, hspace=0.3, top=0.95, bottom=0.14)

print "center:", w[np.argmin(np.abs(nw))]
pl.show()
