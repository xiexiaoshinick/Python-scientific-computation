# -*- coding: utf-8 -*-
import numpy as np
from xlwt import *

book = Workbook()
sheet1 = book.add_sheet(u'随机数')
head = ["normal", "power", "gamma", "SUM"]
N = 100
data = np.vstack([
    np.random.normal(size=N),
    np.random.power(a=1.0,size=N),
    np.random.gamma(0.9,size=N)
])
# 创建对齐配置
al = Alignment()
al.horz = Alignment.HORZ_CENTER
al.vert = Alignment.VERT_CENTER
# 创建边框配置
borders = Borders()
borders.bottom = Borders.THICK
# 创建样式
style = XFStyle()
style.alignment = al
style.borders = borders
# 获得第0行
row0 = sheet1.row(0)
# 将标题写入第0行，使用所创建的样式
for i, text in enumerate(head):
    row0.write(i, text, style=style)  
# 写入随机数  
for i, line in enumerate(data):
    for j, value in enumerate(line):
        sheet1.write(j+1, i, value)
# 写求和公式，注意公式中的单元格下标从1开始计数
for i in xrange(N):
    sheet1.row(i+1).set_cell_formula( 
        3, Formula("sum(A%s:C%s)" % (i+2, i+2)), calc_flags=1)
    
# 设置4列的宽度   
for i in xrange(4):
    sheet1.col(i).width = 4000 
# 设置第0行的高度
sheet1.row(0).height_mismatch = 1
sheet1.row(0).height = 1000       
book.save("tmp.xls") 