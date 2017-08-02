# -*- coding: utf-8 -*-
"""
使用各种编辑编辑器显示字符串列表。
"""
from enthought.traits.api import HasTraits, List, Str
from enthought.traits.ui.api import View, HSplit, Item, CheckListEditor, SetEditor, HGroup

  
filter_types = [u"低通", u"高通", u"带通", u"带阻"] 
class ListDemo(HasTraits):

    items = List(Str) 
    view = View(
        HSplit(
            Item("items", style="custom", show_label=False), 
            Item("items", style="custom", 
                 editor=CheckListEditor(values=filter_types, cols=4)), 
            Item("items", editor=SetEditor(values=filter_types)), 
            show_labels=False
        ),
        resizable=True,
        width = 600,
        title=u"简单列表编辑器演示"
    )


demo = ListDemo()
demo.items = [u"低通", u"高通"]
demo.edit_traits()


class ListDemo2(HasTraits):
    filter_types = List(Str, value=[u"低通", u"高通", u"带通", u"带阻"]) 
    items = List(Str) 
    view = View(
        HGroup(
            Item("filter_types", label=u"候选"), 
            Item("items", style="custom", 
                editor=CheckListEditor(name="filter_types")), 
            show_labels=False
        ),
        resizable=True,
        width = 300,
        height = 180,
        title=u"动态修改候选值"
    )
    

demo2 = ListDemo2()
demo2.items = [u"低通", u"高通"]
demo2.configure_traits()
