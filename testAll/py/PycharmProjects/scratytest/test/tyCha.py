# encoding: utf-8
# 天眼查  修改excel
from selenium import webdriver
from xlutils.copy import copy
import xlrd
import xlwt
import time

# 初始化浏览器
browser = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

work_book = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\xuzhen.xlsx")
work_book1 = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\test1.xls")
wb = copy(work_book1)
ws = wb.get_sheet(0)
# 单元格样式
styleRed = xlwt.easyxf('pattern: pattern solid, fore_colour red; font: bold on;')
styleBlue = xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on;')


sheet = work_book.sheet_by_index(0)
# for i in range(0, sheet.nrows):
w_index = 0
for i in range(80, 85):
    try:
        print(i)
        w_index += 1
        # 源名称
        s_con = sheet.cell(i, 0).value
        # 源编码
        s_bm = sheet.cell(i, 1).value

        browser.get('http://www.tianyancha.com/')
        time.sleep(1)
        input_text = browser.find_element_by_id('live-search')
        search_btn = browser.find_element_by_css_selector('div.search_button')
        input_text.clear()
        input_text.send_keys(s_con)
        search_btn.click()
        time.sleep(1)

        c_link = browser.find_element_by_css_selector("div.search_name>a")
        c_link_href = c_link.get_attribute("href")

        browser.get(c_link_href)
        time.sleep(1)

        # 查询出的结果
        c_name = browser.find_element_by_css_selector("div.company_info_text>p")
        # 组织机构
        f_table_zuzhi = browser.find_element_by_xpath("//table[2]/tbody/tr[2]/td[2]/div/span")
        # 统一信用
        f_table_xinyong = browser.find_element_by_xpath("//table[2]/tbody/tr[4]/td[2]/div/span")

        if f_table_zuzhi.text == '未公开' and f_table_xinyong.text == '未公开':
            ws.write(w_index, 1, s_con, styleRed)
            ws.write(w_index, 2, c_name.text, styleRed)
            ws.write(w_index, 0, s_bm, styleRed)
            ws.write(w_index, 3, f_table_zuzhi.text, styleRed)
            ws.write(w_index, 4, f_table_xinyong.text, styleRed)
        else:
            ws.write(w_index, 0, s_bm)
            ws.write(w_index, 3, f_table_zuzhi.text)
            ws.write(w_index, 4, f_table_xinyong.text)
            if s_con != c_name.text:
                ws.write(w_index, 1, s_con, styleBlue)
                ws.write(w_index, 2, c_name.text, styleBlue)
            else:
                ws.write(w_index, 1, s_con)
                ws.write(w_index, 2, c_name.text)

    except Exception as ex:
        print(ex)

ws.col(0).width = 256 * 20
ws.col(1).width = 256 * 40
ws.col(2).width = 256 * 40
ws.col(3).width = 256 * 20
ws.col(4).width = 256 * 30

wb.save(r"C:\Users\Administrator\Desktop\test1.xls")
browser.quit()
