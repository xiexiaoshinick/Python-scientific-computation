# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Str, Int
from enthought.traits.ui.api import View, Item 

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int
    
    view = View( 
        Item('department', label=u"部门", tooltip=u"在哪个部门干活"), 
        Item('name', label=u"姓名"),
        Item('salary', label=u"工资"),
        Item('bonus', label=u"奖金"),
        title = u"员工资料", width=250, height=150, resizable=True 
    )
    
if __name__ == "__main__":
    p = Employee()
    p.configure_traits()