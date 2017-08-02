# -*- coding: utf-8 -*-
"""
演示代理类型DelegateTo的用法
"""
from enthought.traits.api import HasTraits, Str, Instance, DelegatesTo

class System(HasTraits):
    name = Str
    
class CPU(HasTraits):
    cpu_type = Str
    
class PC(HasTraits):
    os = Instance(System)
    cpu = Instance(CPU)
    
    cpu_type = DelegatesTo("cpu") 
    os_name = DelegatesTo("os", prefix="name") 
    
    def _os_name_changed(self):
        print "OS changed to", self.os_name
    
if __name__ == "__main__":    
    os = System(name="WindowsXP")
    cpu = CPU(cpu_type="Atom280")
    pc = PC(os=os, cpu=cpu)
    print pc.cpu_type
    print pc.os_name
    os.name = "Windows7"