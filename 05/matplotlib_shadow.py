# -*- coding: utf-8 -*-
"""
给曲线添加阴影效果。
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

x = np.arange(0., 2., 0.01)
y = np.sin(2*np.pi*x)

N = 7 # 阴影的条数
for i in xrange(N, 0, -1):
    offset = transforms.ScaledTranslation(i, -i, transforms.IdentityTransform()) 
    shadow_trans = plt.gca().transData + offset 
    plt.plot(x,y,linewidth=4,color="black", 
        transform=shadow_trans,  
        alpha=(N-i)/2.0/N)
    
plt.plot(x,y,linewidth=4,color='black')    
plt.ylim((-1.5, 1.5))
plt.show()