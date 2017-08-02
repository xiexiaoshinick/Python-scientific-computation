# -*- coding: utf-8 -*-
import numpy as np
from numpy import fft
import pyopencv as cv

from enthought.chaco.tools.api import LassoSelection
from enthought.traits.api import HasTraits, Instance, Array, Bool
from enthought.traits.ui.api import Item, Group, View
from enthought.enable.api import ComponentEditor
from enthought.chaco.api import ArrayPlotData, gray, Plot, LassoOverlay, HPlotContainer 
from enthought.pyface.timer.api import Timer

N = 256

class FFT2Demo(HasTraits):
    plot = Instance(HPlotContainer)
    filtered_img = Array()
    timer = Instance(Timer)
    need_redraw = Bool(True)
    
    traits_view = View(
        Group(
            Item('plot', editor=ComponentEditor(), show_label=False),
            orientation = "vertical"),
        resizable=True, title=u"二维傅立叶变换滤波演示",
        width = 260*3, height = 260,
        )    
        
    def __init__(self):
        #读入图像
        img = cv.imread("lena_full.jpg")
        img2 = cv.Mat()
        cv.cvtColor(img, img2, cv.CV_BGR2GRAY)
        img = cv.Mat()
        cv.resize(img2, img, cv.Size(N, N))
        self.fimg = fft.fft2(img[:]) # 图像的频域信号
        mag_img = np.log10(np.abs(self.fimg))
    
        # 创建计算用图像
        filtered_img = np.zeros((N, N), dtype=np.float)
        self.mask = np.zeros((N, N), dtype=np.float)
        self.mask_img = cv.asMat(self.mask) # 在self.mask上绘制多边形用的图像
        
        # 创建数据源
        self.data = ArrayPlotData(
            mag_img = fft.fftshift(mag_img),
            filtered_img = filtered_img,
            mask_img = self.mask
        )
        
        # 创建三个图像绘制框以及容器
        meg_plot, img = self.make_image_plot("mag_img")
        mask_plot, _ = self.make_image_plot("mask_img")       
        filtered_plot, _ = self.make_image_plot("filtered_img")
        self.plot = HPlotContainer(meg_plot, mask_plot, filtered_plot)     
        
        # 创建套索工具
        lasso_selection = LassoSelection(component=img)
        lasso_overlay = LassoOverlay(lasso_selection = lasso_selection, component=img, selection_alpha=0.3)
        img.tools.append(lasso_selection)
        img.overlays.append(lasso_overlay)
        self.lasso_selection = lasso_selection                 
        
        # 监听套索工具的事件、开启时钟事件
        lasso_selection.on_trait_change(self.lasso_updated, "disjoint_selections")
        self.timer = Timer(50, self.on_timer)
    
    def make_image_plot(self, img_data):
        p = Plot(self.data, aspect_ratio = 1)
        p.x_axis.visible = False
        p.y_axis.visible = False
        p.padding = [1,1,1,1]
        return p, p.img_plot(img_data, colormap=gray, origin="top left")[0]
        
    def lasso_updated(self):
        self.need_redraw = True
               
    def on_timer(self, *args):
        if not self.need_redraw: return
        self.need_redraw = False
        
        self.mask.fill(0)
        length = len(self.lasso_selection.dataspace_points)
        if length == 0: return
        
        def convert_poly(poly):
            tmp = cv.asvector_Point2i(poly)            
            return cv.vector_vector_Point2i([tmp])
        
        # 在遮罩数组上绘制套索多边形
        for poly in self.lasso_selection.disjoint_selections: 
            poly = poly.astype(np.int)
            print poly.shape
            cv.fillPoly(self.mask_img, convert_poly(poly), cv.Scalar(1,1,1,1))
            poly = N - poly # 绘制对称多边形
            cv.fillPoly(self.mask_img, convert_poly(poly), cv.Scalar(1,1,1,1))

        # 更新遮罩图像
        self.data["mask_img"] = self.mask
        
            
        # 更新滤波图像    
        data = self.data["filtered_img"]
        data[:] = fft.ifft2(self.fimg * fft.fftshift(self.mask)).real
        self.data["filtered_img"] = data

demo = FFT2Demo()
demo.configure_traits()