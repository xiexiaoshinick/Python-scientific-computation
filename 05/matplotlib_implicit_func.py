# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

y, x = np.ogrid[-1.5:1.5:200j, -1.5:1.5:200j]
f = (x**2 + y**2)**4 - (x**2 - y**2)**2

plt.figure(figsize=(9,4))
plt.subplot(121)
extent = [np.min(x), np.max(x), np.min(y), np.max(y)]
cs = plt.contour(f, extent=extent, levels=[0, 0.1], 
     colors=["b", "r"], linestyles=["solid", "dashed"], linewidths=[2, 2])
     
     
plt.subplot(122)
for c in cs.collections:
    data = c.get_paths()[0].vertices
    plt.plot(data[:,0], data[:,1], 
        color=c.get_color()[0],  linewidth=c.get_linewidth()[0])

plt.show()