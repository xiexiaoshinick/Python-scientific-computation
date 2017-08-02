# -*- coding: utf-8 -*-
"""
自定义一个只能为奇数的Trait类型
"""

from enthought.traits.api import BaseInt

class OddInt( BaseInt ): 

    # 定义缺省值
    default_value = 1 

    # trait类型的描述文字
    info_text = 'an odd integer'

    def validate( self, object, name, value ): 
        "校验值是否为奇数"
        value = super(OddInt, self).validate(object, name, value) 
        if (value % 2) == 1:
            return value

        self.error( object, name, value )

if __name__ == "__main__":
    from enthought.traits.api import HasTraits
    class A(HasTraits):
        v = OddInt
    a = A()
    print a.v
    a.v = 3
    print a.v
    a.v = 2