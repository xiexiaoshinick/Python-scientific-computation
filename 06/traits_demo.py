# -*- coding: utf-8 -*-
"""
演示Trait属性的各种功能： 初始化、验证、代理、监听、界面
"""
from enthought.traits.api import Delegate, HasTraits, Instance, Int, Str

class Parent ( HasTraits ):
    # 初始化: last_name被初始化为'Zhang'
    last_name = Str( 'Zhang' ) 

class Child ( HasTraits ):          
    age = Int

    # 验证: father属性的值必须是Parent类的实例
    father = Instance( Parent ) 

    # 代理： Child的实例的last_name属性代理给其father属性的last_name
    last_name = Delegate( 'father' ) 

    # 监听: 当age属性的值被修改时，下面的函数将被运行
    def _age_changed ( self, old, new ): 
        print 'Age changed from %s to %s ' % ( old, new )

if __name__ == "__main__":        
    p = Parent()
    c = Child()

    c.father = p
    print c.last_name

    c.age = 4
    c.print_traits()
    print c.get()
    c.set(age = 6)
    c.configure_traits()