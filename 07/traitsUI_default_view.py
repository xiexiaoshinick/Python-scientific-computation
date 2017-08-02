# -*- coding: utf-8 -*-
"""
演示TraitsUI自动创建的界面
"""
from enthought.traits.api import HasTraits, Str, Int

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

Employee().configure_traits()