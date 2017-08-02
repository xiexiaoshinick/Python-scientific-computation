# -*- coding: utf-8 -*-
"""
可以先定义Trait类型对象，然后用它定义Trait属性
"""

from enthought.traits.api import HasTraits, Range

coefficient = Range(-1.0, 1.0, 0.0)

class Quadratic(HasTraits):
    c2 = coefficient
    c1 = coefficient
    c0 = coefficient

    
class Quadratic2(HasTraits):
    c2 = Range(-1.0, 1.0, 0.0)
    c1 = Range(-1.0, 1.0, 0.0)
    c0 = Range(-1.0, 1.0, 0.0)


if __name__ == "__main__":
    print coefficient
    q1 = Quadratic()
    print q1.trait("c2").trait_type
    print q1.trait("c1").trait_type
    print q1.trait("c0").trait_type
    q2 = Quadratic2()
    print q2.trait("c2").trait_type
    print q2.trait("c1").trait_type
    print q2.trait("c0").trait_type