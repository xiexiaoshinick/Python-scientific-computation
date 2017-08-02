# -*- coding: utf-8 -*-
import numpy as np
from spectrum_freq_process import FrequencyProcess

def average_spectrum(data, fft_size):
    "以1/2的覆盖率计算data信号的每个频率的平均能量"
    p = np.zeros(fft_size//2+1)
    start = 0
    n = 0
    while start + fft_size < len(data):
        tmp = np.abs(np.fft.rfft(data[start:start+fft_size]))      
        p += tmp*tmp
        n += 1
        start+=fft_size//2
    p /= n
    return p        
        
class SpectrumSubtract(FrequencyProcess):
    def __init__(self, infile, outfile, fft_size, noise_len, a, b):
        self.noise_len = noise_len
        self.a = a
        self.b = b
        super(SpectrumSubtract, self).__init__(infile, outfile, fft_size)
        
    def process_init(self):
        self.noise = average_spectrum(self.input[:self.noise_len], self.fft_size)
        self.avg_gain = np.zeros(self.fft_size//2+1) 
        # 频率平滑用的卷积窗口
        self.moving_window = np.hanning(9)
        self.moving_window /= np.sum(self.moving_window)
        self.moving_size = len(self.moving_window)//2

    def process_block(self, block):
        block_power = np.abs(block) ** 2 #信号block的能量
        
        # 由谱相减得到的每个频率窗口的gain
        gain = (block_power - self.a*self.noise)/block_power
        np.clip(gain, self.b, 1e20, gain)
        
        # 对gain在频率上进行平滑处理
        gain = np.convolve(gain, self.moving_window)
        gain = gain[self.moving_size:self.moving_size+self.fft_size//2+1]
        
        # 对gain在时间上进行平滑处理
        self.avg_gain *= 0.8
        gain *= 0.2
        self.avg_gain += gain
        
        # 处理块
        block *= self.avg_gain
        return block
        
if __name__ == "__main__":
    SpectrumSubtract("voice.wav", "voice_ss.wav", 2048, 138000, 1.2, 0.05)