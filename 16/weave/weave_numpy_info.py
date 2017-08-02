# -*- coding: utf-8 -*-
from scipy import weave
import numpy as np

def print_array_info(arr):
    weave.inline(r"""
    int i;
    printf("arr.ndim=%d\n", Darr);
    printf("arr.shape=");
    for(i=0;i<Darr;i++)
    {
        printf("%d ", Narr[i]);
    }
    printf("\n");
    printf("arr.strides=");
    for(i=0;i<Darr;i++)
        printf("%d ", Sarr[i]);
    printf("\n");
    """, ["arr"], compiler="gcc")

a = np.arange(12).reshape(-1, 4)
print_array_info(a)
print_array_info(a[:,::2])
