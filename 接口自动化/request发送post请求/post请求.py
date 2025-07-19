# -*- coding: utf-8 -*-
"""
@Time    :2022/8/29 22:13
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""post请求
发送post请求的时候需要注意，参数是放在body上面去传的
url：接口地址
json：请求参数
Headers：请求头信息
发送请求：res = requests.post(url,json,headers.yml)
获取响应对象的内容：
    响应状态码：res.status_code
    响应信息：res.json()   #以json格式查看响应内容
"""
# import  requests
# import json
# #请求cms的登录接口,post请求的请求参数是表单的形式
# url = 'http://192.168.203.168:8080/cms/manage/loginJump.do'
# data = {"userAccount":"admin",
#         'loginPwd':"123456"}
# headers.yml = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
#
# # res = requests.post(url=url,data=data,headers.yml=headers.yml)
# res = requests.request(method='post',url=url,headers.yml=headers.yml,data=data)
#
# print(res)
# print(res.json())

#请求课堂派的登录接口
# ketangpai_login_url ='https://openapiv5.ketangpai.com//UserApi/login'
# data = {
#     "email": "15521048080",
#     "password": "822703304gsx",
#     "remember": "0",
#     "code": "",
#     "mobile": "",
#     "type": "login",
#     "reqtimestamp": 1679278865560
# }
# json_data = json.dumps(data)
# print(type(json_data))  #str类型，json是字符串表示法
#
# headers.yml = {"Content-Type":"application/json"}
# res1 = requests.request(method = 'post',
#                         url=ketangpai_login_url,
#                         headers.yml = headers.yml,
#                         json = json_data)
# #json参数自动帮你把dict类型转换成为json
# print(res1.json())


# import requests
# import unittest
# ketangpai_login_url ='https://openapiv5.ketangpai.com//UserApi/login'
# data = {
#     "email": "15521048080",
#     "password": "822703304gsx",
#     "remember": "0",
#     "code": "",
#     "mobile": "",
#     "type": "login",
#     "reqtimestamp": 1679278865560
# }
#
#
# headers.yml = {"Content-Type":"application/json"}
# res1 = requests.request(method = 'post',
#                         url=ketangpai_login_url,
#                         headers.yml = headers.yml,
#                         json = data)
# #json参数自动帮你把dict类型转换成为json
# print(res1.json())
# print(res1.json()['data']['token'])
#
# #请求查看课程列表接口
# ketangpai_kecheng_url = 'https://openapiv5.ketangpai.com/CourseApi/semesterList'
#
# kecheng_data = {
#     "isstudy": "1",
#     "search": "",
#     "reqtimestamp": 1679278866326
# }
# headers_kecheng = {
#     "Content-Type":"application/json",
#                    "token":"a9f78e386498731e2e8b88b66ba2c4b1b4ccd1236c69e4aea5c38d8485afa445"
#                    }
# res2 = requests.request(method='post',url=ketangpai_kecheng_url,headers.yml=headers_kecheng,json = kecheng_data)
# print(res2.json())

# import requests
# import unittest
# from HTMLTestRunner3 import  HTMLTestRunner
# class Test_ketangpai(unittest.TestCase):
#     headers = {"Content-Type":"application/json"}
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.session = requests.session()
#     # def __init__(self):
#     #     self.session = requests.session()
#
#     def test_login(self):
#         login_url = 'https://openapiv5.ketangpai.com//UserApi/login'
#         login_data =  {
#                         "email": "15521048080",
#                         "password": "822703304gsx",
#                         "remember": "0",
#                         "code": "",
#                         "mobile": "",
#                         "type": "login",
#                         "reqtimestamp": 1679278865560
#         }
#         res = self.session.request(method='post',url=login_url,headers=self.headers,json = login_data)
#         print(res.json())
#
#     def test_chaxunkecheng(self):
#         chaxun_url = 'https://openapiv5.ketangpai.com//CourseApi/semesterCourseList'
#         chaxun_data = {
#                 'isstudy': "1",
#                 'search': "",
#                 'semester': "2021-2022",
#                 'term': "0",
#                 'reqtimestamp': 1661786299326
#                 }
#
#         res = self.session.request(method='post',url=chaxun_url,headers=self.headers,json = chaxun_data)
#         print(res.json())
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(Test_ketangpai('test_login'))
#     file = open('./report.html', 'wb')  # stream=sys.stdout, verbosity=1, title=None, description=None
#     runner = HTMLTestRunner(stream=file,  # 流文件
#                             verbosity=2,  # 报告的详细程度,2 1 0，2最详细
#                             title='我是title，请看我',  # 报告的title
#                             description='我是描述我是描述——请看我')  # 报告的描述
#     runner.run(suite)
#     file.close()


import  requests
import json
"""cms的登录接口使用post请求登录"""
# cms_login_url ='http://192.168.203.180:8080/cms/manage/loginJump.do'
# method = 'post'
# dict_data = {"userAccount":"admin",
#              "loginPwd":"123456"}
#
# res = requests.request(method=method,url=cms_login_url,data = dict_data).json()
# print(res)


"""课堂派登录接口--json参数自动转换，把dict转换为json数据"""
ketangpai_login= 'https://openapiv5.ketangpai.com//UserApi/login'
method = 'post'
#如果以后要传的是json数据，那么直接写字典数据来存就可以了，json参数会
#自动把dict数据转换称为json数据
dict_data ={
    "email": "15521048080",
    "password": "822703304gsx",
    "remember": "0",
    "code": "",
    "mobile": "",
    "type": "login",
    "reqtimestamp": 1683873810521
}
res = requests.request(method=method,url=ketangpai_login,json=dict_data).json()
print(res)

# ketangpai_login= 'https://openapiv5.ketangpai.com//UserApi/login'
# method = 'post'
# #如果以后要传的是json数据，那么直接写字典数据来存就可以了，json参数会
# #自动把dict数据转换称为json数据
# dict_data ={
#     "email": "15521048080",
#     "password": "822703304gsx",
#     "remember": "0",
#     "code": "",
#     "mobile": "",
#     "type": "login",
#     "reqtimestamp": 1683873810521
# }
# #把dict_data转换称为json_data,用的是json模块的dumps
# json_data = json.dumps(dict_data)
# res = requests.request(method=method,url=ketangpai_login,data = json_data).json()
# print(res)
#


