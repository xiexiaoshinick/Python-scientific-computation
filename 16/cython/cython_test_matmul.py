# -*- coding: utf-8 -*-
import cython_matmul as cm
import numpy as np
import time

N = 100
a = np.random.rand(N,N)
b = np.random.rand(N,N)
out = np.zeros((N,N))

def matmul0(A, B, out):
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            s = 0
            for k in range(A.shape[1]):
                s += A[i, k] * B[k, j]
                out[i,j] = s

cm.matmul0 = matmul0            
                
start = time.clock()
out = np.dot(a,b)
print "np.dot", time.clock() - start

for funcid in range(5):
    funcname = "matmul"+str(funcid)
    func = getattr(cm, funcname)
    start = time.clock()
    func(a,b,out)
    print funcname, time.clock() - start