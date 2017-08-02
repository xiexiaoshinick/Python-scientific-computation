# -*- coding: utf-8 -*-
import numpy as np
import pyopencv as cv


def mouse_call_back(event, x, y, flags, user_data):
    global seed
    
    # 右键松开时，初始化种子图像
    if event == cv.CV_EVENT_RBUTTONUP: 
        img2[:] = img[:]    
        markers[:] = 0
        seed = 1
        cv.imshow("Watershed Demo", img2)
        
    if seed == len(marks_color): return
    
    # 左键按下时，在种子图像上添加种子
    if flags == cv.CV_EVENT_FLAG_LBUTTON: 
        pt = cv.Point(x, y)
        cv.circle(markers, pt, 5, cv.Scalar(seed,seed,seed,seed), cv.CV_FILLED)
        cv.circle(img2, pt, 5, marks_color[seed], cv.CV_FILLED)
        cv.imshow("Watershed Demo", img2)
        
    # 左键松开时，使用watershed进行图像分割
    if event == cv.CV_EVENT_LBUTTONUP:  
        seed += 1
        tmp_markers = markers.clone() 
        cv.watershed(img, tmp_markers)
        color_map = tmp_markers[:].astype(np.int) 
        
        img3 = img2.clone()
        img4 = cv.asMat( palette[color_map] ) 
        cv.addWeighted(img3, 1.0, img4, mask_opacity, 0, img3) 
        cv.imshow("Watershed Demo", img3)
        

        

        
# 区域的颜色列表
marks_color = [ 
    cv.CV_RGB(0, 0, 0)    ,cv.CV_RGB(255, 0, 0),
    cv.CV_RGB(0, 255, 0)  ,cv.CV_RGB(0, 0, 255),
    cv.CV_RGB(255, 255, 0),cv.CV_RGB(0, 255, 255),
    cv.CV_RGB(255, 0, 255),cv.CV_RGB(255, 255, 255)
]

# 将颜色列表转换为调色板数组，只取前三个通道的值
palette = np.array([c.ndarray[:-1] for c in marks_color], dtype=np.uint8) 

seed = 1 # 从序号1开始设置区域颜色
mask_opacity = 0.5 # 绘制区域颜色的透明度


img = cv.imread("fruits.jpg")
img2 = img.clone() # 绘制初始区域用
markers = cv.Mat(img2.size(), cv.CV_32S) # 储存初始区域的数组
markers[:] = 0

cv.namedWindow("Watershed Demo")
cv.imshow("Watershed Demo", img2)
cv.setMouseCallback("Watershed Demo", mouse_call_back) 
cv.waitKey(0)
