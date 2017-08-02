# -*- coding: utf-8 -*-
"""
播放水波动画
"""
import pyopencv as cv

def show_video(fileorid):
    cv.namedWindow(str(fileorid), cv.CV_WINDOW_AUTOSIZE)
    video = cv.VideoCapture(fileorid) 
    img = cv.Mat() 
    img2 = cv.Mat()    
    while video.grab():     
        video.retrieve(img, 0) 
        #cv.cvtColor(img, img2, cv.CV_GBR2RGB)
        cv.imshow(str(fileorid), img)
        cv.waitKey(5)

if __name__ == "__main__":    
    import sys    
    try:
        fileorid = sys.argv[1]
        if fileorid.isalnum():
            fileorid = int(fileorid)
    except:
        fileorid = "waterwave.avi"
    show_video(fileorid)