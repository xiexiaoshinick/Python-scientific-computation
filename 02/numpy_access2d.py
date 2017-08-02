# -*- coding: utf-8 -*-
"""
演示二维数组的下标存取。
"""
import numpy as np

a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print "a[0,3:5]=", a[0,3:5]
print "a[4:,4:]=", a[4:,4:]
print "a[:,2]=", a[:,2]
print "a[2::2,::2]=", a[2::2,::2]

b = a[0,3:5]
b[0] = -b[0]
print "a[0,3:5]=", a[0,3:5]
b[0] = -b[0]

idx = slice(None, None, 2), slice(2,None)
print "idx = ", idx
print "a[idx]=", a[idx] # 和a[::2,2:]相同
print "a[idx][idx]=", a[idx][idx] # 和a[::2,2:][::2,2:]相同

print a[(0,1,2,3,4),(1,2,3,4,5)]
print a[3:, [0,2,5]]
mask = np.array([1,0,1,0,0,1], dtype=np.bool)
print a[mask, 2]
mask = np.array([1,0,1,0,0,1])
print a[mask, 2]