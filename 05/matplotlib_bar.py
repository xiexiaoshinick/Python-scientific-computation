# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("china_population.txt")
width = (data[1,0] - data[0,0])*0.4 
plt.figure(figsize=(8,5))
plt.bar(data[:,0]-width, data[:,1]/1e7, width, color="b", label=u"男") 
plt.bar(data[:,0], data[:,2]/1e7, width, color="r", label=u"女") 
plt.xlim(-width, 100)
plt.xlabel(u"年龄")
plt.ylabel(u"人口（千万）")
plt.legend()


plt.show()