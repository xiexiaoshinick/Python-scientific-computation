# -*- coding: utf-8 -*-
from scipy import weave
import numpy as np

def build_ext():  
    mod = weave.ext_tools.ext_module('demo_ext') 

    ext_code = r"""
    int i, j;
    for(i=0;i<Narr(0);i++)
    for(j=0;j<Narr(1);j++)
    {
        arr(i,j) *= arr(i,j); 
    }    
    """
    arr = np.zeros((2,2))    
    func = weave.ext_tools.ext_function('square',ext_code,['arr'],  
         type_converters=weave.converters.blitz)
    mod.add_function(func) 

    mod.compile(compiler="gcc")
    
if __name__ == "__main__":
    try:
        import demo_ext
    except ImportError:
        build_ext()
        import demo_ext
    
    a = np.arange(0, 100, 1.0).reshape((10, 10))
    demo_ext.square(a)
    print a
        