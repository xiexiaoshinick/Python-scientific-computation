# -*- coding: utf-8 -*-
"""
使用NumPy快速读取CSV文件。
"""
import numpy as np

# 采用字符串数组读取文件
tmp = np.loadtxt("test.csv", dtype=np.str, delimiter=",")

# 将部分数组的值进行转换
data = tmp[1:,1:].astype(np.float)
print data

# 定义结构数组元素的类型
persontype = np.dtype({
    'names':['name', 'age', 'weight', 'height'],
    'formats':['S32','i', 'f', 'f']})
    
f = file("test.csv")
f.readline() # 跳过第一行
data = np.loadtxt(f, dtype=persontype, delimiter=",")
f.close()
print data