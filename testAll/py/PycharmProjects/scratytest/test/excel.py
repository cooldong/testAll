#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf-8

import xlrd
import xlwt

wb_rd2 = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\tonglei.xls")
ws2 = wb_rd2.sheet_by_index(0)

for i in range(1, 10):
    con = ws2.cell(i, 5).value
    print(con)

