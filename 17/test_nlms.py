import numpy as np
from nlms_numpy import nlms as numpy_nlms
from nlms_swig import nlms as swig_nlms
from nlms_weave import nlms as weave_nlms
x = np.random.random(100)
d = np.random.random(100)
h = np.zeros(10)
u1 = numpy_nlms(x, d, h, 0.1)
h = np.zeros(10)
u2 = swig_nlms(x, d, h, 0.1)
h = np.zeros(10)
u3 = weave_nlms(x, d, h, 0.1)

print np.sum((u1-u2)**2)
print np.sum((u1-u3)**2)