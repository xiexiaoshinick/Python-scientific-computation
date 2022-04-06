# -*- coding: utf-8 -*-
"""
演示一维数组的下标存取。
"""
import numpy as np

a = np.arange(10)
print ("a[5]", a[5])
print "a[3:5]", a[3:5]
print "a[:5]", a[:5]
print "a[:-1]", a[:-1]
a[2:4] = 100,101 
print "a", a
print "a[1:-1:2]", a[1:-1:2]
print "a[::-1]", a[::-1]
print "a[5:1:-2]", a[5:1:-2]

b = a[3:7]
print b
b[2] = -10
print b
print a

x = np.arange(10,1,-1)
print x
print "x[[3, 3, 1, 8]]", x[[3, 3, 1, 8]]
b = x[np.array([3,3,-3,8])] 
b[2] = 100
print b
print x
x[[3,5,1]] = -1, -2, -3
print x

x = np.arange(5,0,-1)
print x
print x[np.array([True, False, True, False, False])] 
print x[[True, False, True, False, False]]
print x[np.array([True, False, True, True])]
x[np.array([True, False, True, True])] = -1, -2, -3 
print x

x = np.random.rand(10)
print x
print x>0.5
print x[x>0.5]