# -*- coding: utf-8 -*-
import pyopencv as cv

img = cv.imread("lena.jpg")
img2 = cv.Mat(img.size(), cv.CV_8UC4)

w, h = img.size().width, img.size().height

def blend(img, img2): 
    """
    混合两幅图像, 其中img2有4个通道
    """
    #使用alpha通道计算img2的混和值
    b = img2[:,:,3:] / 255.0     
    a = 1 - b # img的混合值

    #混合两幅图像
    img[:,:,:3] *= a  
    img[:,:,:3] += b * img2[:,:,:3]

img2[:] = 0
for i in xrange(0, w, w/10): 
    cv.line(img2, cv.Point(i,0), cv.Point(i, h),  
        cv.Scalar(0, 0, 255, i*255/w), 5)

blend(img, img2) 

img2[:] = 0        
for i in xrange(0, h, h/10):
    cv.line(img2, cv.Point(0,i), cv.Point(w, i), 
        cv.Scalar(0, 255, 0, i*255/h), 5)
        
blend(img, img2)
     
cv.namedWindow("Draw Demo")
cv.imshow("Draw Demo", img)
cv.waitKey(0)