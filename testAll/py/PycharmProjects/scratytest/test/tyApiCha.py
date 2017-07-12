# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import xlrd
from xlutils.copy import copy
import json
import time


# 操作excel
work_book = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\xuzhen_new_copy.xlsx")

wb = copy(work_book)

sheet = work_book.sheet_by_index(0)

ws = wb.get_sheet(0)

url_base = 'http://api.tianyancha.com/services/v3/search/'
url_suff = '?pageNum=1&pageSize=20&base=&estiblishTimeStart=&estiblishTimeEnd=&moneyStart=&moneyEnd=&city=&category='

send_headers = {
        'Host': 'api.tianyancha.com',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'User-Agent': 'NewSkyEyes/2.1.4 (iPhone; iOS 10.0.2; Scale/2.00)',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'version': 'iOS 2.1.4',
        'Authorization': 'ufS+JsBsdvqwjd1HFjiPjibdAJ27XNQQDzEzwgpbkIaOmRECyKOagLxDN6j/v62Mn/HndxP16RhkL3QkNyRInA==',
        'Accept-Encoding': 'gzip, deflate'
    }


for i in range(1, 101):

    # try:
        time.sleep(1)
        if i % 2 == 0 and i != 0:
            wb.save(r"C:\Users\Administrator\Desktop\yyyyyyyyy.xls")

        print(i)
        # 源名称
        s_con = sheet.cell(i, 0).value

        s_con_encode = urllib.parse.quote(str(s_con))

        url = url_base + s_con_encode + url_suff

        time.sleep(1)
        req = urllib.request.Request(url, headers=send_headers)
        res = urllib.request.urlopen(req)

        con = res.read()
        html = con.decode('utf-8')
        html = json.loads(html)

        state_h = html['state']
        print("state:"+state_h)

        if state_h == 'ok':
            totalpage_h = html['totalPage']
            print("totalpage:" + str(totalpage_h))
            index = 0
            data_h = html['data'][index]
            while 'base' not in data_h and index <= totalpage_h:
                index += 1
                data_h = html['data'][index]

            print("index:"+str(index))
            if index <= totalpage_h:
                id_h = data_h['id']
                # 结果数据（省份）
                base_h = data_h['base']
                print("base:"+base_h)
                print("id:"+str(id_h))
                time.sleep(1)
                url_c = 'http://api.tianyancha.com/services/v3/t/details/wapCompany/'+str(id_h)

                req = urllib.request.Request(url_c, headers=send_headers)
                res = urllib.request.urlopen(req)

                con = res.read()
                html_c = con.decode('utf-8')
                html_c = json.loads(html_c)
                # print("con:" + str(html))

                # data_c = html_c['data'][0]
                # data_c = json.dumps(data_c)
                # data_c = json.loads(data_c)
                # print(data_c)
                #
                # info_c = data_c['baseInfo']

                info_c = html_c['data']['BaseInfo']
                print(info_c)

                #结果数据（名称，地址，信用代码，组织机构）
                name_c = ''
                regLocation_c = ''
                creditCode_c = ''
                orgniz_c = ''

                if 'name'in info_c:
                    name_c = info_c['name']
                if 'regLocation'in info_c:
                    regLocation_c = info_c['regLocation']
                if 'creditCode'in info_c:
                    creditCode_c = info_c['creditCode']
                if 'orgNumber'in info_c:
                    orgniz_c = info_c['orgNumber']

                print("name:"+name_c)
                print("reglocal:"+regLocation_c)
                print("credit:"+creditCode_c)
                print("orgniz_c:"+orgniz_c)

                ws.write(i, 6, name_c)
                ws.write(i, 7, creditCode_c)
                ws.write(i, 8, orgniz_c)
                ws.write(i, 9, base_h)
                ws.write(i, 10, '')
                ws.write(i, 11, regLocation_c)
                if creditCode_c == '未公开' and orgniz_c == '未公开':
                    ws.write(i, 12, '3')
                elif s_con != name_c:
                    ws.write(i, 12, '2')
                else:
                    ws.write(i, 12, '1')
            else:
                print(s_con)
                ws.write(i, 12, '4')
        else:
            print(s_con)
            ws.write(i, 12, '4')

    # except Exception as ex:
    #     s_con = sheet.cell(i, 0).value
    #     print(s_con)
    #     print(ex)
    #     ws.write(i, 12, '4')








