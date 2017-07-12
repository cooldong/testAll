# encoding: utf-8
# 天眼查  新增excel
from selenium import webdriver
import xlrd
import xlwt
import time

# 初始化浏览器
browser = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 操作excel
work_book = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\999(2).xls")

wb = xlwt.Workbook()
ws = wb.add_sheet(u'sheet1', cell_overwrite_ok=True)

# 单元格样式
styleRed = xlwt.easyxf('pattern: pattern solid, fore_colour red; font: bold on;')
styleBlue = xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on;')
styleGreen = xlwt.easyxf('pattern: pattern solid, fore_colour green; font: bold on;')

sheet = work_book.sheet_by_index(0)

a_count = 0
time1 = time.time()
# for i in range(0, sheet.nrows):
w_index = 0
for i in range(6800, 7801):
    try:
        print(i)
        w_index += 1
        a_count += 1
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
            ws.write(w_index, 5, '3', styleRed)
        else:
            ws.write(w_index, 0, s_bm)
            ws.write(w_index, 3, f_table_zuzhi.text)
            ws.write(w_index, 4, f_table_xinyong.text)
            if s_con != c_name.text:
                ws.write(w_index, 1, s_con, styleBlue)
                ws.write(w_index, 2, c_name.text, styleBlue)
                ws.write(w_index, 5, '2', styleBlue)
            else:
                ws.write(w_index, 1, s_con)
                ws.write(w_index, 2, c_name.text)
                ws.write(w_index, 5, '1')

    except Exception as ex:
        s_con = sheet.cell(i, 0).value
        s_bm = sheet.cell(i, 1).value
        print(s_con)
        ws.write(w_index, 0, s_bm, styleGreen)
        ws.write(w_index, 1, s_con, styleGreen)
        ws.write(w_index, 5, '4', styleGreen)
        print(ex)


column0 = [u'源编码', u'源名称', u'查询出的结果', u'组织代码结构', u'统一信用结果', u'标识(1:完全相同2:名称不同3:未公开4:未查到)']

# 生成第一行
for t in range(0, 6):
    ws.write(0, t, column0[t])

ws.col(0).width = 256 * 20
ws.col(1).width = 256 * 40
ws.col(2).width = 256 * 40
ws.col(3).width = 256 * 20
ws.col(4).width = 256 * 30
ws.col(5).width = 256 * 20

wb.save(r"C:\Users\Administrator\Desktop\test2create.xls")
browser.quit()
time2 = time.time()
time = time2-time1
print('all_count:'+str(a_count))
print('time collapse:'+str(time))
