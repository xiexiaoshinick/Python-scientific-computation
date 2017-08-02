# -*- coding: utf-8 -*-
"""
使用内存映射数组修改BMP文件。
"""
import numpy as np

# shape = 高，宽，颜色
bmp = np.memmap("tmp.bmp", offset=54, shape=(1000,1000,3)) 

# 产生一组从0到255的渐变值
tmp = np.linspace(0, 255, 1000).astype(np.uint8) 

# 水平蓝色渐变 
bmp[:, :, 0] = tmp  
# 垂直绿色渐变
bmp[:, :, 1] = tmp.reshape(-1,1)  
# 红色成分
bmp[:, :, 2] = 127  

bmp.flush() 