# -*- coding: utf-8 -*-
"""
@Time    :2022/8/29 21:42
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
postman做接口测试流程：
    获得接口文档/自己抓包/-->在接口中填写请求方式（get/post）-->填写url地址-->填写请求参数    
pip install requests 
requests.request(method)   -->find_element(locator)-->find_element('xpath','locator')
requests.get()             -->find_element_by_id()
requests.post()            -->find_element_by_name()
requests.put()
requests.delete()
requests.options()

类比postman，发送请求的三要素：
1.url地址
2.请求的方法
3.请求体和请求头参数（get请求可能是不带参数的）

操作的步骤：
    1.导包： import requests
    2.写好url地址，写好参数
    3.发送请求：右键执行

"""
# import  requests
# #案例1：对百度发起请求 url=https://www.baidu.com
# url1 = 'https://www.baidu.com'
# #发送请求,通过get发送
# res= requests.get(url=url1)
# #打印出来的是状态码
# print(res)
# #打印res对象的text内容,打印的内容是乱码，一般就和编码格式有关系
# print(res.text)
# print("百度的默认编码格式是：",res.encoding)
# res.encoding='utf-8'
# print("修改编码格式后的内容是：",res.text)
# #打印状态码
# print(res.status_code)
# #打印请求头信息
# print(res.headers.yml)


# # res = requests.get(url=url1)
# res = requests.request('get',url=url1)
#
# #查看响应结果中状态码
# print(res.status_code)  #翻译 status：状态  code：码
#
# #查看响应结果中的响应正文
# # print(res.text)    #text正文，文本的意思
#
# # #查看响应结果中的响应头
# print(res.headers.yml)
# # #查看响应结果中的编码格式
# print(res.encoding) #ISO-8859-1
# # #修改编码格式
# res.encoding='utf-8'
# print(res.text)


#导包
#注意，当用get请求的时候，请求的参数可以放在parmas去传
#也可以放在url上面去传

import  requests
# url = 'http://web.juhe.cn/environment/air/cityair'

url = 'http://web.juhe.cn/environment/air/cityair?key=a51d6ef7c899e2d5c7bb1124906d0d2c&city=广州'
# data = {
#     "key":"a51d6ef7c899e2d5c7bb1124906d0d2c",
#     "city":"广州"
# }
res = requests.get(url = url)
print(res) #<Response [200]>
print(res.status_code) #200
print(res.json()) #{'resultcode': '200', 'reason': 'SUCCESSED!', 'error_code': 0, 'result': [{'citynow': {'city': '广州', 'AQI': '31', 'quality': '优', 'date': '2023-03-20 09:00'}, 'lastTwoWeeks': {'1': {'city': '广州', 'AQI': '54', 'quality': '良', 'date': '2023-02-20'}, '2': {'city': '广州', 'AQI': '66', 'quality': '良', 'date': '2023-02-21'}, '3': {'city': '广州', 'AQI': '69', 'quality': '良', 'date': '2023-02-22'}, '4': {'city': '广州', 'AQI': '85', 'quality': '良', 'date': '2023-02-23'}, '5': {'city': '广州', 'AQI': '73', 'quality': '良', 'date': '2023-02-24'}, '6': {'city': '广州', 'AQI': '27', 'quality': '优', 'date': '2023-02-25'}, '7': {'city': '广州', 'AQI': '52', 'quality': '良', 'date': '2023-02-26'}, '8': {'city': '广州', 'AQI': '76', 'quality': '良', 'date': '2023-02-27'}, '9': {'city': '广州', 'AQI': '69', 'quality': '良', 'date': '2023-02-28'}, '10': {'city': '广州', 'AQI': '90', 'quality': '良', 'date': '2023-03-01'}, '11': {'city': '广州', 'AQI': '74', 'quality': '良', 'date': '2023-03-02'}, '12': {'city': '广州', 'AQI': '97', 'quality': '良', 'date': '2023-03-03'}, '13': {'city': '广州', 'AQI': '74', 'quality': '良', 'date': '2023-03-04'}, '14': {'city': '广州', 'AQI': '68', 'quality': '良', 'date': '2023-03-05'}, '15': {'city': '广州', 'AQI': '68', 'quality': '良', 'date': '2023-03-06'}, '16': {'city': '广州', 'AQI': '60', 'quality': '良', 'date': '2023-03-07'}, '17': {'city': '广州', 'AQI': '65', 'quality': '良', 'date': '2023-03-08'}, '18': {'city': '广州', 'AQI': '67', 'quality': '良', 'date': '2023-03-09'}, '19': {'city': '广州', 'AQI': '55', 'quality': '良', 'date': '2023-03-10'}, '20': {'city': '广州', 'AQI': '61', 'quality': '良', 'date': '2023-03-11'}, '21': {'city': '广州', 'AQI': '58', 'quality': '良', 'date': '2023-03-12'}, '22': {'city': '广州', 'AQI': '90', 'quality': '良', 'date': '2023-03-13'}, '23': {'city': '广州', 'AQI': '75', 'quality': '良', 'date': '2023-03-14'}, '24': {'city': '广州', 'AQI': '69', 'quality': '良', 'date': '2023-03-15'}, '25': {'city': '广州', 'AQI': '57', 'quality': '良', 'date': '2023-03-16'}, '26': {'city': '广州', 'AQI': '59', 'quality': '良', 'date': '2023-03-17'}, '27': {'city': '广州', 'AQI': '67', 'quality': '良', 'date': '2023-03-18'}, '28': {'city': '广州', 'AQI': '45', 'quality': '优', 'date': '2023-03-19'}}, 'lastMoniData': {'1': {'city': '白云嘉禾', 'AQI': '49', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '27', 'PM2.5Day': '27', 'PM10Hour': '27', 'lat': '', 'lon': ''}, '2': {'city': '白云竹料', 'AQI': '52', 'America_AQI': 'null', 'quality': '良', 'PM2.5Hour': '30', 'PM2.5Day': '30', 'PM10Hour': '30', 'lat': '', 'lon': ''}, '3': {'city': '从化街口', 'AQI': '38', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '22', 'PM2.5Day': '22', 'PM10Hour': '22', 'lat': '', 'lon': ''}, '4': {'city': '从化良口', 'AQI': '37', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '25', 'PM2.5Day': '25', 'PM10Hour': '25', 'lat': '', 'lon': ''}, '5': {'city': '番禺大学城', 'AQI': '36', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '16', 'PM2.5Day': '16', 'PM10Hour': '16', 'lat': '', 'lon': ''}, '6': {'city': '番禺中学', 'AQI': '25', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '17', 'PM2.5Day': '17', 'PM10Hour': '17', 'lat': '22.9477', 'lon': '113.352'}, '7': {'city': '广东商学院', 'AQI': '31', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '17', 'PM2.5Day': '17', 'PM10Hour': '17', 'lat': '23.0916', 'lon': '113.348'}, '8': {'city': '广雅中学', 'AQI': '33', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '18', 'PM2.5Day': '18', 'PM10Hour': '18', 'lat': '23.1422', 'lon': '113.235'}, '9': {'city': '花都师范', 'AQI': '47', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '25', 'PM2.5Day': '25', 'PM10Hour': '25', 'lat': '23.3917', 'lon': '113.215'}, '10': {'city': '花都梯面', 'AQI': '46', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '25', 'PM2.5Day': '25', 'PM10Hour': '25', 'lat': '', 'lon': ''}, '11': {'city': '黄埔科学城', 'AQI': '43', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '27', 'PM2.5Day': '27', 'PM10Hour': '27', 'lat': '', 'lon': ''}, '12': {'city': '九龙镇镇龙', 'AQI': '44', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '22', 'PM2.5Day': '22', 'PM10Hour': '22', 'lat': '23.2783', 'lon': '113.568'}, '13': {'city': '麓湖', 'AQI': '26', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '16', 'PM2.5Day': '16', 'PM10Hour': '16', 'lat': '23.1544', 'lon': '113.2765'}, '14': {'city': '帽峰山森林公园', 'AQI': '32', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '15', 'PM2.5Day': '15', 'PM10Hour': '15', 'lat': '23.5538', 'lon': '113.589'}, '15': {'city': '南沙黄阁', 'AQI': '22', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '9', 'PM2.5Day': '9', 'PM10Hour': '9', 'lat': '', 'lon': ''}, '16': {'city': '南沙街', 'AQI': '20', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '8', 'PM2.5Day': '8', 'PM10Hour': '8', 'lat': '', 'lon': ''}, '17': {'city': '市八十六中', 'AQI': '45', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '22', 'PM2.5Day': '22', 'PM10Hour': '22', 'lat': '23.105', 'lon': '113.433'}, '18': {'city': '市监测站', 'AQI': '29', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '16', 'PM2.5Day': '16', 'PM10Hour': '16', 'lat': '23.1331', 'lon': '113.26'}, '19': {'city': '市五中', 'AQI': '30', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '18', 'PM2.5Day': '18', 'PM10Hour': '18', 'lat': '23.105', 'lon': '113.261'}, '20': {'city': '体育西', 'AQI': '34', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '19', 'PM2.5Day': '19', 'PM10Hour': '19', 'lat': '', 'lon': ''}, '21': {'city': '增城荔城', 'AQI': '47', 'America_AQI': 'null', 'quality': '优', 'PM2.5Hour': '31', 'PM2.5Day': '31', 'PM10Hour': '31', 'lat': '', 'lon': ''}}}]}
print(res.headers) #{'Date': 'Mon, 20 Mar 2023 01:41:03 GMT', 'Content-Type': 'text/html;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': 'aliyungf_tc=328be4c6ce40671b804d2195211c66146d2732009338f8e9bde70acf64929eca; Path=/; HttpOnly, JSESSIONID=277805DE9724993B33D900B71E4C2561; Path=/environment; HttpOnly', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip'}














