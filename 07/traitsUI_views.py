# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Str, Int
from enthought.traits.ui.api import View, Group, Item 

g1 = [Item('department', label=u"部门", tooltip=u"在哪个部门干活"), 
      Item('name', label=u"姓名")]
g2 = [Item('salary', label=u"工资"),
      Item('bonus', label=u"奖金")]

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

    traits_view = View( 
        Group(*g1, label = u'个人信息', show_border = True),
        Group(*g2, label = u'收入', show_border = True),
        title = u"缺省内部视图")    

    another_view = View( 
        Group(*g1, label = u'个人信息', show_border = True),
        Group(*g2, label = u'收入', show_border = True),
        title = u"另一个内部视图")    
        
global_view = View( 
    Group(*g1, label = u'个人信息', show_border = True),
    Group(*g2, label = u'收入', show_border = True),
    title = u"外部视图")    
    
p = Employee()

# 使用内部视图traits_view 
p.edit_traits() 

# 使用内部视图another_view 
p.edit_traits(view="another_view") 

# 使用外部视图view1
p.configure_traits(view=global_view) 