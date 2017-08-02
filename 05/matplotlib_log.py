# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


w = np.linspace(0.1, 1000, 1000)
p = np.abs(1/(1+0.1j*w)) # 计算低通滤波器的频率响应

plt.subplot(221)
plt.plot(w, p, linewidth=2)
plt.ylim(0,1.5)

plt.subplot(222)
plt.semilogx(w, p, linewidth=2)
plt.ylim(0,1.5)

plt.subplot(223)
plt.semilogy(w, p, linewidth=2)
plt.ylim(0,1.5)

plt.subplot(224)
plt.loglog(w, p, linewidth=2)
plt.ylim(0,1.5)


plt.show()