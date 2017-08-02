# -*- coding: utf-8 -*-
"""
计算二维函数曲面，并使用Mayavi绘图。
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


y, x = np.ogrid[-2:2:200j, -2:2:200j]
z = x * np.exp( - x**2 - y**2) 

extent = [np.min(x), np.max(x), np.min(y), np.max(y)] 

plt.figure(figsize=(10,3))
plt.subplot(121)
plt.imshow(z, extent=extent, origin="lower") 
plt.colorbar()
plt.subplot(122)
plt.imshow(z, extent=extent, cmap=cm.gray, origin="lower")
plt.colorbar()


plt.show()