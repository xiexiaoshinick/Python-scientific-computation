# -*- coding: utf-8 -*-
from scipy import weave
a = 100
weave.inline(r'printf("%d\n", a); ', ["a"], compiler="gcc")
a = 200
weave.inline(r'printf("%d\n", a); ', ["a"], compiler="gcc")
a = 200.0
weave.inline(r'printf("%d\n", a); ', ["a"], compiler="gcc")