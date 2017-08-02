# -*- coding: utf-8 -*-
"""
多维数组的下标存取实例。

有一个shape为(I, J, K)的三维数组v和一个shape为(I, J)的二维数组idx，idx的每个值
都是0到K-L的整数。通过下标运算得到一个数组r，对于第0和1轴的每个下标i和j都满足下
面条件：

    r[i,j,:] = v[i,j,idx[i,j]:idx[i,j]+L]
"""
import numpy as np

I, J, K, L = 6, 7, 8, 3
_, _, v = np.mgrid[:I, :J, :K]
idx = np.random.randint(0, K-L, size=(I,J))

idx_k = idx.reshape(I,J,1) + np.arange(3)
idx_i, idx_j, _ = np.ogrid[:I, :J, :K]

r = v[idx_i, idx_j, idx_k]
i, j = 2,3
print r[i,j,:]
print v[i,j,idx[i,j]:idx[i,j]+L]