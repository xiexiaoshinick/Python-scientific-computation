# -*- coding: utf-8 -*-
"""
演示Trait属性，显示一个编辑颜色的界面
"""
from enthought.traits.api import HasTraits, Color
class Circle(HasTraits):
    color = Color

if __name__ == "__main__":    
    c = Circle()
    c.color = "red"
    c.configure_traits()