# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


y, x = np.ogrid[-2:2:200j, -3:3:300j] 
z = x * np.exp( - x**2 - y**2) 

extent = [np.min(x), np.max(x), np.min(y), np.max(y)]

plt.figure(figsize=(10,4))
plt.subplot(121)
cs = plt.contour(z, 10, extent=extent) 
plt.clabel(cs) 
plt.subplot(122)
plt.contourf(x.reshape(-1), y.reshape(-1), z, 20) 
plt.show()