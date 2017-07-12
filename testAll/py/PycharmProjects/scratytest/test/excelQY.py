#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf-8

import xlrd
import xlwt
from xlutils.copy import copy

wb_rd1 = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\result.xls")
wb_rd2 = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\test8Create.xls")
ws1 = wb_rd1.sheet_by_index(0)
ws2 = wb_rd2.sheet_by_index(0)

wd = copy(wb_rd1)
wsd = wd.get_sheet(0)

for i in range(0, 1816):
    print(i)
    if i % 10 == 0 and i != 0 and i < 1811:
        wd.save(r"C:\Users\Administrator\Desktop\result8.xls")
    elif i > 1810:
        wd.save(r"C:\Users\Administrator\Desktop\result8.xls")
    s_bm2 = ws2.cell(i, 1).value
    flag1 = ws2.cell(i, 12).value

    # if flag1 is not None and flag1 != '' and int(flag1) < 4:
    for j in range(1, 8002):
        s_bm1 = ws1.cell(j, 1).value
        if s_bm2 == s_bm1:
            for m in range(0, 13):
                con = ws2.cell(i, m).value
                wsd.write(j, m, con)
            break

