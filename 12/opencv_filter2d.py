# -*- coding: utf-8 -*-
import pyopencv as cv
import numpy as np
import matplotlib.pyplot as plt

# 读入图片并缩小为1/2
img0 = cv.imread("lena.jpg")
size = img0.size()
w, h = size.width, size.height
img1 = cv.Mat()
cv.resize(img0, img1, cv.Size(w//2, h//2)) 

# 各种卷积核
kernels = [ 
    (u"低通滤波器",np.array([[1,1,1],[1,2,1],[1,1,1]])*0.1),
    (u"高通滤波器",np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])),
    (u"边缘检测",np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]))
]

index = 0
for name, kernel in kernels:
    plt.subplot(131+index)
    # 将卷积核转换为Mat对象
    kmat = cv.asMat(kernel.astype(np.float), force_single_channel=True) 
    img2 = cv.Mat()
    cv.filter2D(img1, img2, -1, kmat) 
    # 由于matplotlib的颜色顺序和OpenCV的顺序相反
    plt.imshow(img2[:,:,::-1]) 
    plt.title(name)
    index += 1
    plt.gca().set_axis_off()
plt.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
plt.show()    


