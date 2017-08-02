# -*- coding: utf-8 -*-
"""
输出mymodel.py模块中的x和y，为了显示最新的值，使用reload()强制
重新载入模块。
"""
import mymodel
reload(mymodel)
from mymodel import *

print x, y