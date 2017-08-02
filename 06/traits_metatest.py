# -*- coding: utf-8 -*-
"""
查看Trait属性的元数据
"""

from enthought.traits.api import HasTraits, Int, Str, Array, List
   
class MetadataTest(HasTraits):
    i = Int(99, myinfo="test my info") 
    s = Str("test", label=u"字符串") 
    # NumPy的数组
    a = Array 
    # 元素为Int的列表
    list = List(Int)  

test = MetadataTest()

print test.traits()
print test.trait("i")
print test.trait("s").desc
print test.trait("a").array
print test.trait("i").default
print test.trait("i").default_kind
print test.trait("i").trait_type
print test.trait("list").inner_traits
print test.trait("list").inner_traits[0].trait_type
print test.trait("i").type
print test.trait("i").myinfo