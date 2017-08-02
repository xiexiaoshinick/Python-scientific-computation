# -*- coding: utf-8 -*-
"""
使用TraitsUI制作的简单的界面程序。使用Wing IDE 101可以查看
按钮点击事件处理函数_button_fired的调用堆栈。
"""
from enthought.traits.api import HasTraits, Instance, Button, Int
from enthought.traits.ui.api import View, Item

class Demo(HasTraits):
    count = Int(0)
    button = Button("Click Me")
    view = View(Item("button"), Item("count"))
    
    def _button_fired(self):
        self.count += 1
    
demo = Demo()
demo.configure_traits()