# -*- coding: utf-8 -*-
import numpy as np
import scipy.weave as weave

def nlms(x, d, h, step):
    code = """
    int i, j, count;
    int nh = Nh[0];
    double s, e, power=0;
    double *px;
    count = Nu[0];
    for(i=0;i<nh;i++)
    {
        power += x(i) * x(i);
        u(i) = 0;
    }
    for(i=nh;i<count;i++)
    {
        s = 0;
        px = &x(i);
        for(j=0;j<nh;j++)
        {
            s += (*px--) * h(j);
        }
        u(i) = s;
        e = d(i) - s;
        
        px = &x(i);
        for(j=0;j<nh;j++)
        {
            h(j) += step * e * (*px--) / power;        
        }
        power -= x(i-nh+1) * x(i-nh+1);
        if(i<count-1)
            power += x(i+1) * x(i+1);
    }
    """
    u = np.zeros(min(len(x), len(d))) 
    weave.inline(  
        code,   
        ['x','d','h','u','step'], 
        type_converters=weave.converters.blitz, 
        compiler="gcc"
    )
    return u   