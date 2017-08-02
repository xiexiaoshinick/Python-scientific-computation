#coding=utf8
from xlrd import open_workbook
from xlutils.copy import copy
rb = open_workbook('tmp.xls',formatting_info=True)
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(0, 4, u"我添加了一些内容")
wb.save('output.xls')