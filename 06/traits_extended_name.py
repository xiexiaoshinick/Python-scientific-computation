# -*- coding: utf-8 -*-
"""
演示与Trait属性匹配的扩展名
"""
from enthought.traits.api import HasTraits, Str, Int, Instance, List, on_trait_change

class HasName(HasTraits):
    name = Str()
    
    def __str__(self):
        return "<%s %s>" % (self.__class__.__name__, self.name)

class Inner(HasName):
    x = Int
    y = Int

class Demo(HasName):
    x = Int
    y = Int
    z = Int(monitor=1) # 有元数据属性monitor的Int
    inner = Instance(Inner)
    alist = List(Int)
    test1 = Str()
    test2 = Str()
    
    def _inner_default(self):
        return Inner(name="inner1")
            
    @on_trait_change("x,y,inner.[x,y],test+,+monitor,alist[]")
    def event(self, obj, name, old, new):
        print obj, name, old, new
        
if __name__ == "__main__":        
    d = Demo(name="demo")
    
    d.x = 10 # 与 x 匹配
    d.y = 20 # 与 y 匹配
    d.inner.x = 1 # 与 inner.[x,y] 匹配
    d.inner.y = 2 # 与 inner.[x,y] 匹配
    d.inner = Inner(name="inner2") # 与 inner.[x,y] 匹配
    d.test1 = "ok" # 与 test+ 匹配
    d.test2 = "hello" # 与 test+ 匹配
    d.z = 30  # 与 +monitor 匹配
    d.alist = [3] # alist[] 匹配
    d.alist.extend([4,5]) # alist[] 匹配
    d.alist[2] = 10 # alist[] 匹配