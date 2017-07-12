#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf-8

import json
a = [{1:1,"a":"a"}, {2:3,"b":"b"}]
b = json.dumps(a)
c = json.loads(b)
print(b)
print(c)

# ori_str = {"state":"ok","message":"","data":{"baseInfo":{"updatetime":1475510852060,"fromTime":1435507200000,"type":1,"categoryScore":7725,"id":2319314962,"percentileScore":7254,"regNumber":"610131100208823","allCount":{"branchCount":0,"investCount":0,"comAbnoInfo":0,"companyBidCount":0,"copyrightRegCount":6,"investorCount":3,"empCount":2,"staffCount":0,"comChanInfoCount":5,"annuRepYear":1,"ComAbnoInfoCount":0,"patentCount":0,"lawSuitCount":0,"bondCount":0,"tmCount":3},"phoneNumber":"029-89384996","regCapital":"3000 万","regInstitute":"西安市工商行政管理局高新分局","name":"陕西优百信息技术有限公司","regLocation":"西安市高新区科技五路北侧橡树星座1幢2单元22901室","industry":"电信、广播电视和卫星传输服务","approvedTime":1447948800000,"businessScope":"一般经营项目：计算机软件设计、开发、销售；计算机信息技术服务、技术咨询、技术转让；弱电工程、建筑智能化工程的施工；计算机电子产品的销售。（以上经营范围除国家规定的专控及前置许可项目）","estiblishTime":1435507200000,"regStatus":"存续","legalPersonName":"张复生","toTime":4070880000000,"legalPersonId":1923545637,"sourceFlag":"http://qyxy.baic.gov.cn/","actualCapital":"","flag":1,"companyOrgType":"有限责任公司(自然人投资或控股)","updateTimes":1475510851000,"base":"snx","companyType":0,"creditCode":"91610131333792691H","companyId":42780110},"investorList":[{"id":1923545637,"amount":0.0,"name":"张复生","type":2},{"id":2005021142,"amount":0.0,"name":"杨辉","type":2},{"id":2209944738,"amount":0.0,"name":"邵光明","type":2}],"investList":[],"staffList":[],"branchList":[],"tmList":[{"name":"比令数据","url":"http://tm-image.tianyancha.com/tm/f22b7aa0b9f39166123b3b5e84bf1e13.jpg"},{"name":"集狐","url":"http://tm-image.tianyancha.com/tm/b6dd7322fe77e9c905968ee5eed7ecce.jpg"},{"name":"云集采","url":"http://tm-image.tianyancha.com/tm/561c95a2d9cd1fab0f466e77f06b46e4.jpg"}],"lawSuitList":[],"comChanInfoList":[{"changeItem":"住所(营业场所、地址)变更","contentBefore":"西安市高新区唐延南都市之门C座第1幢1单元20层12002-2018-1号","contentAfter":"西安市高新区科技五路北侧橡树星座1幢2单元22901室","changeTime":"2015-11-20"},{"changeItem":"投资人(股权)变更","contentBefore":"姓名: 杨辉; 出资额: 225; 百分比: 7.5姓名: 于谌彬; 出资额: 510; 百分比: 17姓名: 张复生; 出资额: 765; 百分比: 25.5姓名: 邵光明; 出资额: 1500; 百分比: 50","contentAfter":"姓名: 杨辉; 出资额: 225; 百分比: 7.5姓名: 张复生; 出资额: 1275; 百分比: 42.5姓名: 邵光明; 出资额: 1500; 百分比: 50","changeTime":"2015-11-20"},{"changeItem":"投资人(股权)变更","contentBefore":"姓名: 杨辉; 出资额: 225; 百分比: 7.5姓名: 张复生; 出资额: 1125; 百分比: 37.5姓名: 邵光明; 出资额: 1650; 百分比: 55","contentAfter":"姓名: 杨辉; 出资额: 225; 百分比: 7.5姓名: 于谌彬; 出资额: 510; 百分比: 17姓名: 张复生; 出资额: 765; 百分比: 25.5姓名: 邵光明; 出资额: 1500; 百分比: 50","changeTime":"2015-08-24"},{"changeItem":"注册资本(金)变更","contentBefore":"100","contentAfter":"3000","changeTime":"2015-07-15"},{"changeItem":"投资人(股权)变更","contentBefore":"姓名: 杨辉; 出资额: 7.5; 百分比: 7.5姓名: 张复生; 出资额: 37.5; 百分比: 37.5姓名: 邵光明; 出资额: 55; 百分比: 55","contentAfter":"姓名: 杨辉; 出资额: 225; 百分比: 7.5姓名: 张复生; 出资额: 1125; 百分比: 37.5姓名: 邵光明; 出资额: 1650; 百分比: 55","changeTime":"2015-07-15"}],"comAbnoInfoList":[],"annuRepYearList":[{"id":408467263,"phoneNumber":"029-89384996","reportYear":"2015"}],"lawSuitTotal":0}}
# ori_data = ori_str['data']
# ori_info = ori_data['baseInfo']
#
# print(ori_info['name'])
# print(ori_info['regLocation'])
# print(ori_info['creditCode'])



# ori_str_liebiao = {
# 	"state": "ok",
# 	"message": "",
# 	"totalPage": 1,
# 	"humanCount": 0,
# 	"companyCount": 1,
# 	"total": 1,
# 	"data": [{
# 		"id": 239568981
# 	},{
# 		"id": 239568982,
# 		"base": "山东2"
# 	}]
# }
#
#
# ori_data = ori_str_liebiao['data'][0]
#
# if 'id' not in ori_data:
#     print(ori_data['id'] is None)
#
# if 'base' in ori_data:
#     print(ori_data['base'] is None)
#
# print(ori_str_liebiao['state'] is None)
# print(ori_str_liebiao['total'] is None)
