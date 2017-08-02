# -*- coding: utf-8 -*-
import numpy as np

def hill1d(n, d):
    """
    绘制山脉曲线，2**n+1为曲线在X轴上的长度，d为衰减系数
    """
    a = np.zeros(2**n+1) 
    scale = 1.0
    for i in xrange(n, 0, -1): 
        s = 2**(i-1) 
        s2 = 2*s
        tmp = a[::s2] 
        a[s::s2] += (tmp[:-1] + tmp[1:]) * 0.5 
        a[s::s2] += np.random.normal(size=len(tmp)-1, scale=scale) 
        scale *= d 
    return a

if __name__ == "__main__":        
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,4))    
    for i, d in enumerate([0.4, 0.5, 0.6]):
        np.random.seed(8) 
        a = hill1d(9, d)
        plt.plot(a, label="d=%s" % d, linewidth=3-i)   
    plt.xlim((0,len(a)))    
    plt.legend()
    plt.show()
