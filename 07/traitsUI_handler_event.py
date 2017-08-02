# -*- coding: utf-8 -*-
"""
在控制器对象中对模型对象的Trait属性进行监听
"""
from enthought.traits.api import HasTraits, Bool
from enthought.traits.ui.api import View, Handler

class MyHandler(Handler):
    def setattr(self, info, object, name, value): 
        Handler.setattr(self, info, object, name, value)
        info.object.updated = True 
        print "setattr", name
        
    def object_updated_changed(self, info): 
        print "updated changed", "initialized=%s" % info.initialized
        if info.initialized:
            info.ui.title += "*"

class TestClass(HasTraits):
    b1 = Bool
    b2 = Bool
    b3 = Bool
    updated = Bool(False)

view1 = View('b1', 'b2', 'b3',
             handler=MyHandler(),
             title = "Test",
             buttons = ['OK', 'Cancel'])

tc = TestClass()
tc.configure_traits(view=view1)