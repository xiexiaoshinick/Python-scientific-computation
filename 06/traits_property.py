# -*- coding: utf-8 -*-
"""
使用带缓存和监听功能的Property属性
"""

from enthought.traits.api import HasTraits, Float, Property, cached_property

class Rectangle(HasTraits):
    width = Float(1.0) 
    height = Float(2.0)

    #area是一个属性，当width,height的值变化时，它对应的_get_area函数将被调用
    area = Property(depends_on=['width', 'height'])  

    # 通过cached_property修饰器缓存_get_area()的输出
    @cached_property  
    def _get_area(self): 
        "area的get函数，注意此函数名和对应的Proerty名的关系"
        print 'recalculating'
        return self.width * self.height

if __name__ == "__main__":
    r = Rectangle()
    print r.area
    r.width = 10
    print r.area
    r.edit_traits()
    r.configure_traits()
    