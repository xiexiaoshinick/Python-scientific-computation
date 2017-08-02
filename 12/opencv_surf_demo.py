# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
from enthought.traits.api import HasTraits, Array, Range, Bool
from enthought.traits.ui.api import View, Item, HGroup
from scipy.spatial.distance import cdist

class SURFDemo(HasTraits):
    m = Array(np.float, (2,3))
    max_distance = Range(0.1, 1.0, 0.26)
    draw_circle = Bool(True)
    
    hessian_th = Range(100.0, 1000.0, 1000.0)
    octaves = Range(1, 5, 2)
    layers = Range(1, 5, 3)
    view = View(
        Item("m", label=u"变换矩阵"),
        Item("hessian_th", label=u"hessian阈值"),    
        HGroup( 
            Item("octaves", label=u"Octaves"),
            Item("layers", label=u"层数"),
        ),
        Item("max_distance", label=u"距离阈值"),
        Item("draw_circle", label=u"绘制特征点"),
        title = u"SURF Demo控制面板",
        resizable = True,
    )        
    
    def __init__(self, *args, **kwargs):
        super(SURFDemo, self).__init__(*args, **kwargs)
        img = cv.imread("lena_small.jpg")
        self.m = np.array([[0.8,-0.6,60],[0.6,0.7,-20]])
        self.img1 = cv.Mat()
        cv.cvtColor(img, self.img1, cv.CV_BGR2GRAY)       
        self.affine()
        self.on_trait_change(self.redraw, "max_distance,draw_circle")
        self.on_trait_change(self.recalculate, "m,hessian_th,octaves,layers")
        self.recalculate()
        self.redraw()
        
    def get_features(self, img):
        surf = cv.SURF(self.hessian_th, self.octaves, self.layers, True)  
        keypoints = cv.vector_KeyPoint()
        features = surf(img, cv.Mat(), keypoints)  
        return keypoints, np.array(features)
        
    def affine(self):
        self.img2 = cv.Mat()
        M = cv.asMat(self.m, force_single_channel=True)
        cv.warpAffine(self.img1, self.img2, M, self.img1.size(), 
            borderValue=cv.CV_RGB(255,255,255))
                    
    def match_features(self):
        f1 = self.features1.reshape(len(self.keypoints1), -1) 
        f2 = self.features2.reshape(len(self.keypoints2), -1)
        self.f1 = f1
        self.f2 = f2
        distances = cdist(f1, f2) 
        self.mindist = np.min(distances, axis=1)  
        self.idx_mindist = np.argmin(distances, axis=1)
            
    def recalculate(self):
        self.affine()
        self.keypoints1, self.features1 = self.get_features(self.img1)        
        self.keypoints2, self.features2 = self.get_features(self.img2)        
        self.match_features()
        self.redraw()
        
    def draw_keypoints(self, img, keypoints, offset):
        for kp in keypoints:
            center = cv.Point(int(kp.pt.x)+offset, int(kp.pt.y))
            cv.circle(img, center, int(kp.size*0.25), cv.CV_RGB(255,255,0))

    def redraw(self):
        # 同时显示两幅图像
        w = self.img1.size().width
        h = self.img1.size().height
        show_img = cv.Mat(cv.Size(w*2, h), cv.CV_8UC3)
        for i in xrange(3):
            show_img[:,:w,i] = self.img1[:]
            show_img[:,w:,i] = self.img2[:]
        
        # 绘制特征线条
        if self.draw_circle:
            self.draw_keypoints(show_img, self.keypoints1, 0)
            self.draw_keypoints(show_img, self.keypoints2, w)
        
        
        # 绘制直线连接距离小于阈值的两个特征点
        for idx1 in np.where(self.mindist < self.max_distance)[0]:  
            idx2 = self.idx_mindist[idx1]
            pos1 = self.keypoints1[int(idx1)].pt  
            pos2 = self.keypoints2[int(idx2)].pt
            
            p1 = cv.Point(int(pos1.x), int(pos1.y)) 
            p2 = cv.Point(int(pos2.x)+w, int(pos2.y)) 
            cv.line(show_img, p1, p2, cv.CV_RGB(0,255,255), lineType=16)
        
        
        cv.imshow("SURF Demo",show_img)
        
cv.namedWindow("SURF Demo")   
demo = SURFDemo()     
demo.configure_traits()
