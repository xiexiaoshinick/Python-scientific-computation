# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Range, Bool
from enthought.traits.ui.api import View, Item, Group, VGroup

class HoughDemo(HasTraits):
    # Canny 参数
    th1 = Range(0.0, 255.0, 50.0)
    th2 = Range(0.0, 255.0, 200.0)
    show_canny = Bool(False)
    
    # HoughLine 参数
    rho = Range(1.0, 10.0, 1.0)
    theta = Range(0.1, 5.0, 1.0)
    hough_th = Range(1, 100, 40)
    minlen = Range(0, 100, 10)
    maxgap = Range(0, 20, 10)
    
    # HoughtCircle 参数
    dp = Range(1.0, 5.0, 2.0)
    mindist = Range(1.0, 100.0, 50.0)
    param1 = Range(50, 100.0, 50.0)
    param2 = Range(50, 100.0, 100.0)
    
    view = View(
        VGroup(
            Group(
                Item("th1", label=u"阈值1"),
                Item("th2", label=u"阈值2"),
                Item("show_canny", label=u"显示结果"),
                label=u"边缘检测参数"
            ),
            Group(
                Item("rho", label=u"偏移分辨率(像素)"),
                Item("theta", label=u"角度分辨率(角度)"),
                Item("hough_th", label=u"阈值"),
                Item("minlen", label=u"最小长度"),
                Item("maxgap", label=u"最大空隙"),
                label=u"直线检测"
            ),
            Group(
                Item("dp", label=u"分辨率(像素)"),
                Item("mindist", label=u"圆心最小距离(像素)"),
                Item("param1", label=u"参数1"),
                Item("param2", label=u"参数2"),
                
                label=u"圆检测"            
            )
        ),
        title = u"直线和圆检测控制面板"
    )
    
    def __init__(self, *args, **kwargs):
        super(HoughDemo, self).__init__(*args, **kwargs)
        
        self.img = cv.imread("stuff.jpg")
        self.img_gray = cv.Mat()
        cv.cvtColor(self.img, self.img_gray, cv.CV_BGR2GRAY)
        
        self.img_smooth = self.img_gray.clone()
        cv.smooth(self.img_gray, self.img_smooth, cv.CV_GAUSSIAN, 7, 7, 0, 0)
        
        self.redraw()
        
        self.on_trait_change(self.redraw,
            "th1,th2,show_canny,rho,theta,hough_th,minlen,maxgap,dp,mindist,param1,param2")
        
    def redraw(self):
        
        edge_img = cv.Mat()
        # 边缘检测
        cv.Canny(self.img_gray, edge_img, self.th1, self.th2)
        3###
        # 计算结果图
        if self.show_canny: 
            show_img = cv.Mat()
            cv.cvtColor(edge_img, show_img, cv.CV_GRAY2BGR)
        else:
            show_img = self.img.clone()
        4### 
        # 线段检测   
        theta = self.theta / 180.0 * np.pi
        lines = cv.HoughLinesP(edge_img,  
            self.rho, theta, self.hough_th, self.minlen, self.maxgap)
        for line in lines: 
            cv.line(show_img, 
                cv.asPoint(line[:2]),  
                cv.asPoint(line[2:]),
                cv.CV_RGB(255, 0, 0), 2)
        5###
        # 圆形检测
        circles = cv.HoughCircles(self.img_smooth, 3,  
            self.dp, self.mindist, param1=self.param1, param2=self.param2)
            
        for circle in circles: 
            cv.circle(show_img, 
                cv.Point(int(circle[0]), int(circle[1])), int(circle[2]), 
                cv.CV_RGB(0, 255, 0), 2)
        
        cv.imshow("Hough Demo", show_img)
                    
cv.namedWindow("Hough Demo")     
demo = HoughDemo()     
demo.configure_traits()