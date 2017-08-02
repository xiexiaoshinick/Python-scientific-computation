# -*- coding: utf-8 -*-
from scipy import weave
import numpy as np

def set_array(arr):
    weave.inline(r"""
    int i, j, k;
    double v = 0.0;
    for(i=0;i<Narr(0);i++)
    for(j=0;j<Narr(1);j++)
    for(k=0;k<Narr(2);k++)
    {
        arr(i,j,k) = v;
        v += 1.0;
    }
    """, ["arr"], compiler="gcc", type_converters=weave.converters.blitz)

a = np.zeros(12).reshape(2,2,3)

set_array(a)
print a