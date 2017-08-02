# -*- coding: utf-8 -*-
"""
在一个视图对象中显示两个模型对象
"""
from enthought.traits.api import HasTraits, Str, Int
from enthought.traits.ui.api import View, Group, Item

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

comp_view = View(
    Group(
        Group(
            Item('p1.department', label=u"部门"),
            Item('p1.name', label=u"姓名"),
            Item('p1.salary', label=u"工资"),
            Item('p1.bonus', label=u"奖金"),
            show_border=True
        ),
        Group(
            Item('p2.department', label=u"部门"),
            Item('p2.name', label=u"姓名"),
            Item('p2.salary', label=u"工资"),
            Item('p2.bonus', label=u"奖金"),
            show_border=True
        ),
        orientation = 'horizontal'
    ),
    title = u"员工对比"    
)


employee1 = Employee(department = u"开发", name = u"张三", salary = 3000, bonus = 300)
employee2 = Employee(department = u"销售", name = u"李四", salary = 4000, bonus = 400)

if __name__ == "__main__":
    # 方法一：调用configure_traits，通过context关键字指定模型对象
    
    HasTraits().configure_traits(view=comp_view, context={"p1":employee1, "p2":employee2})
    
    # 方法二：调用视图对象的ui方法显示模型，它的参数是一个字典，将作为
    # UI对象的context属性。此方法需要后续的代码启动界面库的消息循环
    #comp_view.ui({"p1":employee1, "p2":employee2})

    ##### 通过GUI启动消息循环
    #from enthought.pyface.api import GUI
    #GUI().start_event_loop() # 开始后台界面库的消息循环

    ##### 直接启动wx库的消息循环
    #import wx
    #wx.PySimpleApp().MainLoop() # 开始wx的消息循环
