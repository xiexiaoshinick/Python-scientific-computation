# -*- coding: utf-8 -*-
"""
演示Wing IDE 101的goto define功能。使用Wing IDE 101或Spyder打开本程序之后，
按住Ctrl的同时点击signal, pl, HasTraits等跳转到定义它们的程序。
"""
from scipy import signal
import pylab as pl
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item

signal.lfilter
pl.plot
pl.title