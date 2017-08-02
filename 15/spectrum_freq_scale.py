# -*- coding: utf-8 -*-
import numpy as np
from spectrum_freq_process import FrequencyProcess
from scipy.interpolate import UnivariateSpline

class FrequencyScale(FrequencyProcess):
    def __init__(self, infile, outfile, fft_size, scale):
        self.scale = scale        
        super(FrequencyScale, self).__init__(infile, outfile, fft_size)
        
    def process_init(self):
        self.freqs = np.arange(0, self.fft_size//2+1, 1.0)
        
    def process_block(self, block):
        new_freqs = self.freqs * self.scale
        freqs_re = UnivariateSpline(new_freqs, np.real(block), k=3, s=0) 
        freqs_im = UnivariateSpline(new_freqs, np.imag(block), k=3, s=0)
        
        block = freqs_re(self.freqs) + 1j*freqs_im(self.freqs) 
        block[int(np.max(new_freqs)):] = 0  
        return block
        
if __name__ == "__main__":
    FrequencyScale("voice.wav", "voice_fscale.wav", 1024, 0.8)
