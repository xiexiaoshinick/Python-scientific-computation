# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl

def stoz(s):
    """
    将s复平面映射到z复平面
    为了方便起见，假设取样周期T=1
    """
    return (2+s)/(2-s)
    
def make_vline(x):
    return x + 1j*np.linspace(-100.0,100.0,20000)
    
fig = pl.figure(figsize=(7,3))    
axs = pl.subplot(121)
axz = pl.subplot(122)
for x in np.arange(-3, 4, 1):
    s = make_vline(x)
    z = stoz(s)
    axs.plot(np.real(s), np.imag(s))
    axz.plot(np.real(z), np.imag(z))

axs.set_xlim(-4,4)
axz.axis("equal")
axz.set_ylim(-3,3)

pl.show()