# -*- coding: utf-8 -*-
"""
使用字符串编辑器的例子
"""
from enthought.traits.api import HasTraits, Str
from enthought.traits.ui.api import View, Item


class TestStrEditor(HasTraits):
    test = Str        
    view = View(Item("test"))

    
if __name__ == "__main__":
    t = TestStrEditor()
    ed = t.trait("test").trait_type.create_editor()
    print type(ed)
    print ed.get()
    t.configure_traits()