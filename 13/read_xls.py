# -*- coding: utf-8 -*-
import numpy as np
from xlrd import *

book = open_workbook("tmp.xls")
print book.nsheets
print book.sheet_names()[0]
sheet = book.sheets()[0]
print sheet.cell(0, 0)
print sheet.row(0)
print sum(x.value for x in sheet.col(1, start_rowx=1))
print sum(sheet.col_values(1, start_rowx=1))
print sheet.cell(1,3)
