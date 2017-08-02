# -*- coding: utf-8 -*-
import numpy as np
import enthought.chaco.shell as cs 

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

cs.plot(x, y, "r-") 
cs.title("First plot")
cs.ytitle("sin(x)")
cs.show()