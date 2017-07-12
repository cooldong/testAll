# encoding: utf-8
# 天眼查  新增excel
from selenium import webdriver
import xlrd
import xlwt
import time
from xlutils.copy import copy

# 初始化浏览器
browser = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 操作excel
work_book = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\remain.xls")

wb = copy(work_book)
ws = wb.get_sheet(0)

sheet = work_book.sheet_by_index(0)

a_count = 0
time1 = time.time()
# for i in range(0, sheet.nrows):
print(sheet.nrows)
for i in range(4694, sheet.nrows+1):
    try:
        print(i)
        if i % 1 == 0 and i != 0:
            wb.save(r"C:\Users\Administrator\Desktop\remainresult4.xls")

        if i % 50 == 0 and i != 0:
            print('sleep 1 mins!!')
            time.sleep(60)
        a_count += 1
        # 源名称
        s_con = sheet.cell(i, 0).value

        browser.get('http://www.tianyancha.com/')
        time.sleep(1)
        input_text = browser.find_element_by_id('live-search')
        search_btn = browser.find_element_by_css_selector('div.search_button')
        input_text.clear()
        input_text.send_keys(s_con)
        search_btn.click()
        time.sleep(2)

        # 地区
        c_base = browser.find_element_by_css_selector("div.search_base")
        cbase_text = c_base.text

        c_link = browser.find_element_by_css_selector("div.search_name>a")
        c_link_href = c_link.get_attribute("href")
        # print('link:'+str(c_link_href))

        browser.get(c_link_href)
        time.sleep(2)

        # 查询出的结果
        c_name = browser.find_element_by_css_selector("div.company_info_text>p")
        # 组织机构
        f_table_zuzhi = browser.find_element_by_xpath("//table[2]/tbody/tr[2]/td[2]/div/span")
        # 统一信用
        f_table_xinyong = browser.find_element_by_xpath("//table[2]/tbody/tr[4]/td[2]/div/span")
        # 地址
        f_table_addr = browser.find_element_by_xpath("//table[2]/tbody/tr[5]/td[1]/div/span")

        if f_table_zuzhi.text == '未公开' and f_table_xinyong.text == '未公开':
            ws.write(i, 6, c_name.text)
            ws.write(i, 8, f_table_zuzhi.text)
            ws.write(i, 7, f_table_xinyong.text)
            ws.write(i, 9, cbase_text)
            ws.write(i, 11, f_table_addr.text)
            ws.write(i, 12, '3')
        else:
            ws.write(i, 9, cbase_text)
            ws.write(i, 11, f_table_addr.text)
            ws.write(i, 8, f_table_zuzhi.text)
            ws.write(i, 7, f_table_xinyong.text)
            if s_con != c_name.text:
                ws.write(i, 6, c_name.text)
                ws.write(i, 12, '2')
            else:
                ws.write(i, 6, c_name.text)
                ws.write(i, 12, '1')

    except Exception as ex:
        s_con = sheet.cell(i, 0).value
        print(s_con)
        ws.write(i, 12, '4')
        print(ex)

browser.quit()
time2 = time.time()
time = time2-time1
print('all_count:'+str(a_count))
print('time collapse:'+str(time))
