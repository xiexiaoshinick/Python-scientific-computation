# -*- coding: utf-8 -*-
import numpy as np
from visual import *

def search_line_startswith(f, pattern):
    while True:
        line = f.readline()
        if line == "": return False
        if line.strip().startswith(pattern):
            return True

def read_directx_model(filename, double=False):
    f = open(filename)
    search_line_startswith(f, "Mesh") # 定位Mesh行
            
    point_num = int(f.readline().split(";")[0]) # 读入顶点数
    points = np.zeros((point_num, 3)) # 初始化保存顶点坐标的数组
    # 读入所有顶点坐标
    for i in xrange(point_num):
        points[i, :] = [float(x) for x in f.readline().split(";")[:3]]

    face_num = int(f.readline().split(";")[0]) # 读入面数
    
    # 初始化三角形的顶点坐标数组
    pfaces = zeros( (face_num*3 , 3)) # 正面的顶点下标
           
    # 建造所有的模型面的顶点坐标数组，将面的顶点下标替换为顶点坐标
    cnt = 0
    for i in xrange(face_num):
        p_index = [int(x) for x in f.readline().split(";")[1].split(",")]
        for j in xrange(3):
            pfaces[cnt, :] = points[p_index[j], :]
            cnt += 1
            
    search_line_startswith(f, "MeshMaterialList") # 定位材质
    color_num = int(f.readline().split(";")[0])  # 读入材质数
    face_color_num = int(f.readline().split(";")[0]) # 读出面数
    
    # 读入每个面的材质下标
    face_color_list=[]
    for i in xrange(face_color_num):
        face_color_list.append( int(f.readline().strip(",;\n")) )
    
    colors = np.zeros((color_num, 3)) # 初始化储存材质颜色的数组
    # 读入所有材质的颜色
    for i in xrange(color_num):
        search_line_startswith(f, "Material")
        colors[i,:] = [float(x) for x in f.readline().split(";")[:3]]
   
    # 初始化保存每个顶点颜色的数组
    pcolors = np.zeros( (face_color_num*3, 3), np.float)

    # 建造顶点颜色数组，将面的材质下标替换为顶点的材质颜色
    cnt = 0
    for i in xrange(face_color_num):
        color_idx = face_color_list[i] 
        for j in xrange(3):
            pcolors[cnt, :] = colors[color_idx,:]
            cnt += 1
            
    search_line_startswith(f, "MeshNormals") # 定位法线方向 
    
    # 读入法线方向
    point_num = int(f.readline().split(";")[0])
    npoints = np.zeros((point_num, 3))
    for i in xrange(point_num):
        npoints[i,:] = [float(x) for x in f.readline().split(";")[:3]]
            
    face_num = int(f.readline().split(";")[0]) # 读入面数
    
    # 初始化顶点法线方向数组
    nfaces = np.zeros( (face_num*3 , 3), np.float)
        
    # 建造顶点法线方向数组，将每个面的法线下标替换为实际的法线方向
    cnt = 0
    for i in xrange(face_num):
        p_index = [int(x) for x in f.readline().split(";")[1].split(",")]
        for j in xrange(3):
            nfaces[cnt, :] = npoints[p_index[j],:]
            cnt += 1

    f.close()
    
    if double:
       pfaces = np.vstack((pfaces, pfaces[::-1]))
       nfaces = np.vstack((nfaces, nfaces[::-1]))
       pcolors = np.vstack((pcolors, pcolors[::-1]))
    
    model_frame = frame()
    # 使用 顶点坐标数组，顶点颜色数组和顶点法线方向数组构造模型
    model = faces( pos = pfaces, normal = nfaces, color = pcolors, frame = model_frame )
    return model_frame
    
if __name__ == "__main__":
    import sys
    scene.background = (0.9, 0.9, 0.9)
    scene.title = sys.argv[1]
    read_directx_model(sys.argv[1], True)