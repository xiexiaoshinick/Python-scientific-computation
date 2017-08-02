import numpy as np
cimport cython
cimport numpy as np

def matmul1(A, B, out):
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            s = 0
            for k in range(A.shape[1]):
                s += A[i, k] * B[k, j]
                out[i,j] = s
                
def matmul2(A, B, out):
    cdef int i, j, k
    cdef double s
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            s = 0
            for k in range(A.shape[1]):
                s += A[i, k] * B[k, j]
                out[i,j] = s                
                
def matmul3(np.ndarray[np.float64_t, ndim=2] A, 
            np.ndarray[np.float64_t, ndim=2] B, 
            np.ndarray[np.float64_t, ndim=2] out):
    cdef int i, j, k
    cdef double s
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            s = 0
            for k in range(A.shape[1]):
                s += A[i, k] * B[k, j]
                out[i,j] = s                

@cython.boundscheck(False)
@cython.wraparound(False)                
def matmul4(np.ndarray[np.float64_t, ndim=2] A, 
            np.ndarray[np.float64_t, ndim=2] B, 
            np.ndarray[np.float64_t, ndim=2] out):
    cdef int i, j, k
    cdef double s
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            s = 0
            for k in range(A.shape[1]):
                s += A[i, k] * B[k, j]
                out[i,j] = s           