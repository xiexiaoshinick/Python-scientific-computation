# -*- coding: utf-8 -*-
import numpy as np

# 用NumPy实现NLMS算法
# x为参照信号，d为目标信号，h为自适应滤波器的初值
# step_size为更新系数
# 返回自适应滤波器的输出信号
def nlms(x, d, h, step_size=0.5):
    count = min(len(x), len(d)) 
    u = np.zeros(count, dtype=np.float64)
    
    nh = len(h)
    # 计算输入到h中的参照信号的乘方和
    power = np.sum( x[:nh] **2 )  
    
    i = nh 
    while True:
        x_input = x[i:i-nh:-1] 
        u[i] = np.dot(x_input , h)
        e = d[i] - u[i]
        h += step_size * e / power * x_input

        # 减去最早的取样
        power -= x_input[-1] * x_input[-1] 
        i+=1
        if i >= count: return u
        # 增加最新的取样
        power += x[i] * x[i] 
