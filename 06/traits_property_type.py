# -*- coding: utf-8 -*-
"""
自定义Property属性类型
"""

from enthought.traits.api import TraitType, HasTraits, Float

class ScaledValue(TraitType):
    def init(self): 
        self.value = 0
    
    def get(self, object, name): 
        print "get %s.%s" % (object, name)
        return self.value * object.scale 
        
    def set(self, object, name, value):  
        print "set %s.%s = %s" % (object, name , value)
        self.value = value 
        
class A(HasTraits):
    scale = Float(1.0)
    t1 = ScaledValue 
    
if __name__ == "__main__":
    a = A()
    a.t1 = 2
    print a.t1
    a.scale = 3
    print a.t1
