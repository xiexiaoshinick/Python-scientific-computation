# -*- coding: utf-8 -*-
"""
使用Hit和Miss算法对二值图像进行细线化。
"""
from binary_image_common import *
import scipy.ndimage.morphology as m

def skeletonize(img):
    h1 = np.array([[0, 0, 0],[0, 1, 0],[1, 1, 1]]) 
    m1 = np.array([[1, 1, 1],[0, 0, 0],[0, 0, 0]]) 
    h2 = np.array([[0, 0, 0],[1, 1, 0],[0, 1, 0]]) 
    m2 = np.array([[0, 1, 1],[0, 0, 1],[0, 0, 0]])    
    hit_list = [] 
    miss_list = []
    for k in range(4): 
        hit_list.append(np.rot90(h1, k))
        hit_list.append(np.rot90(h2, k))
        miss_list.append(np.rot90(m1, k))
        miss_list.append(np.rot90(m2, k))    
    img = img.copy()
    while True:
        last = img
        for hit, miss in zip(hit_list, miss_list): 
            hm = m.binary_hit_or_miss(img, hit, miss) 
            # 从图像中删除hit_or_miss所得到的白色点
            img = np.logical_and(img, np.logical_not(hm)) 
        # 如果处理之后的图像和处理前的图像相同，则结束处理
        if np.all(img == last):  
            break
    return img

a = make_text_image(200, 100, 1, 5, 80, 0, "TEST")
b = skeletonize(a)

fig = pl.figure()
ax = fig.add_subplot(121)
ax.imshow(a, cmap=pl.cm.gray)
pl.gca().set_axis_off()    
ax = fig.add_subplot(122)
ax.imshow(b, cmap=pl.cm.gray)
pl.gca().set_axis_off()
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
pl.show()