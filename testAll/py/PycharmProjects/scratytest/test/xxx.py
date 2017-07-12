# -*- coding: utf-8 -*-

import urllib.request
import json

url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.29.tcvhY7&id=533631191501&ns=1&abbucket=18'
headers = {
        'authority':'item.taobao.com',
        'method':'GET',
        'path':'/item.htm?spm=a230r.1.14.29.tcvhY7&id=533631191501&ns=1&abbucket=18',
        'scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        # 'accept-encoding':'gzip, deflate, sdch, br',
        'accept-language':'zh-CN,zh;q=0.8',
        'cache-control':'max-age=0',
        'cookie':'thw=cn; cna=QP1PEAe4cCECASQtrifVRczH; v=0; t=d3caba308f1c26da322f03bb86fc3b71; cookie2=1cd51bc0309bdcc3c1540537c695ad96; _tb_token_=eb56e3a3333fb; mt=ci%3D-1_0; l=AiQklo/34zzA3rUZQSq3oGQ4dCgXGUgY; isg=AiYmjf-QTU5qWhno0A7Wr88Xd5wkQ2rBhYkxOhDOtskbk8eteJVN0X8hnTjl; uc1=cookie14=UoWwIqzqs%2FyEtg%3D%3D',
        'referer':'https://s.taobao.com/search?q=shouji&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20161013',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)

for i in range(0, 1000):
    try:
        res = urllib.request.urlopen(req)

        con = res.read()
        html = con.decode('gbk')
        # jsont = json.loads(html)
        # print(i)
        print(i)
        print(html)
    except Exception as ex:
        print(i)
        print(ex)
        break


