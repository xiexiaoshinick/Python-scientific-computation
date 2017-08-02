# -*- coding: utf-8 -*-
"""
演示NumPy数组的一些基本功能。
"""
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
print b
print c

print a.shape
print c.shape

c.shape = 4,3
print c

c.shape = 2, -1
print c

d = a.reshape((2,2))
print d

a[1] = 100
print d

print c.dtype

e = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7], 
    [7, 8, 9, 10]], dtype=np.float)
    
print e

f = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7], 
    [7, 8, 9, 10]], dtype=np.complex)
    
print f

print np.typeDict["d"]
print np.typeDict["double"]
print np.typeDict["float64"]
print set(np.typeDict.values())

print np.arange(0, 1, 0.1)
print np.linspace(0, 1, 12)
print np.logspace(0, 2, 20)

s = "abcdefgh"
print np.fromstring(s, dtype=np.int16)
print np.fromstring(s, dtype=np.float)

def func(i):
    return i%4 + 1
    
print np.fromfunction(func, (10,))

def func2(i,j):
    return (i+1)*(j+1)
    
print np.fromfunction(func2, (9,9))