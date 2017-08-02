# -*- coding: utf-8 -*-
import demo

print "----- FILE -----"
f = demo.fopen("test.txt","w")
print f
demo.fputs("test file\n", f)
demo.fclose(f)

print "----- ARRAY -----"
a = demo.make_array(10)
demo.set_element(a, 5, 1.2)
print demo.get_element(a, 5)
demo.free_array(a)

print "----- CTYPES ARRAY -----"
a = demo.make_array(10)
print a.__long__()
import ctypes
ca = ctypes.cast(a.__long__(), ctypes.POINTER(ctypes.c_double))
demo.set_element(a, 3, 2.0)
print ca[3]
ca[2] = 100
print demo.get_element(a, 2)
demo.free_array(a)

print "----- GLOBAL -----"
print demo.cvar.global_test
demo.cvar.global_test *= 3
demo.print_global()

print "----- STRUCT -----"
a = demo.Point()
print a.x, a.y
a.x, a.y = 100, 200
print demo._demo.Point_x_get(a)

print "----- CLASS -----"
p = demo.CPoint()
p.x, p.y = 3, 4
print p.power()

print "----- FUNCTION -----"
print demo.add_mult(3,4)
print demo.add(4,5)
print demo.inc(4)

print "----- FUNCTION POINTER -----"
print demo.reciprocal(10)
print demo.reciprocal, demo.cb_reciprocal
print demo.sum_func(demo.cb_reciprocal, 1, 100)

print "----- CALLBACK ------"
class SumReciprocal(demo.Sum):
    def Func(self, x):
        return 1.0/x

print SumReciprocal().Cal(1, 100)  