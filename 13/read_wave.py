# -*- coding: utf-8 -*-
import wave
import pylab as pl
import numpy as np

# 读取格式和数据
f = wave.open(r"c:\WINDOWS\Media\ding.wav", "rb") 
nchannels, sampwidth, framerate, nframes = f.getparams()[:4] 
str_data = f.readframes(nframes) 
f.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short) 
wave_data.shape = -1, nchannels 
time = np.arange(0, nframes) * (1.0 / framerate) 

# 绘制波形
pl.subplot(211) 
pl.plot(time, wave_data[:,0])
pl.subplot(212) 
pl.plot(time, wave_data[:,1], c="g")
pl.xlabel("time (seconds)")
pl.show()
