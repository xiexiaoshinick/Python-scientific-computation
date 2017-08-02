# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Range, Bool, Str, List
from enthought.traits.ui.api import View, Item, EnumEditor


def make_surf_map(func, r, w, h, d0):
    """计算曲面函数func在[-r:r]范围之上的值，并进行透视投影。
    视点高度为曲面高度的d0倍+1"""
    y, x = np.ogrid[-r:r:h*1j, -r:r:w*1j]
    z = func(x,y) 
    d = d0*np.ptp(z) + 1.0 
    map1 = x*(d-z)/d 
    map2 = y*(d-z)/d
    return (map1 / (2*r) + 0.5) * w, (map2 / (2*r) + 0.5) * h 
             
class RemapDemo(HasTraits):
    surf_func = Str()
    func_list = List([
        "np.sqrt(8- x**2 - y**2)",
        "np.sin(6*np.sqrt(x**2+y**2))",
        "np.sin(6*x)",
        "np.sin(6*y)",
        "np.sin(np.sqrt(x**2+y**2))/np.sqrt(x**2+y**2)",
        ])
    range = Range(1.0, 100.0)
    view_height = Range(1.0, 50.0, 10.0)
    grid = Bool(True)
    
    view = View(
        Item("surf_func", label=u"曲面函数", 
            editor=EnumEditor(name="func_list", auto_set=False, evaluate=lambda x:x)),
        Item("range", label=u"曲面范围"),
        Item("view_height" ,label=u"视点高度"),
        Item("grid", label=u"显示网格"),
        title = u"Remap Demo控制面板"
    )
    
    def __init__(self, *args, **kwargs):
        super(RemapDemo, self).__init__(*args, **kwargs)
        self.img = cv.imread("lena.jpg")
        self.size = self.img.size()
        self.w, self.h = self.size.width, self.size.height
        self.dstimg = cv.Mat()
        self.map1 = cv.Mat(self.size, cv.CV_32FC1)
        self.map2 = cv.Mat(self.size, cv.CV_32FC1)
        self.gridimg = self.make_grid_img()
        self.on_trait_change(self.redraw, "surf_func,range,view_height,grid")
    
    def redraw(self):
        def func(x, y):
            return eval(self.surf_func, globals(), locals())        
        
        try:
            self.map1[:], self.map2[:] = make_surf_map(
                    func, self.range, self.w, self.h, self.view_height)
        except SyntaxError:
            return
        if self.grid:
            img = self.gridimg
        else:
            img = self.img
        cv.remap(img, self.dstimg, self.map1, self.map2, cv.INTER_LINEAR)
        cv.imshow("Remap Demo", self.dstimg)
            
    def make_grid_img(self):
        img = self.img.clone()
        for i in xrange(0, self.w, 30):
            cv.line(img, cv.Point(i, 0), cv.Point(i, self.h), 
                cv.CV_RGB(0,0,0), 1)
        for i in xrange(0, self.h, 30):
            cv.line(img, cv.Point(0, i), cv.Point(self.w, i),
                cv.CV_RGB(0,0,0), 1)
        return img

cv.namedWindow( "Remap Demo", cv.CV_WINDOW_AUTOSIZE )
demo = RemapDemo()
demo.configure_traits()