# -*- coding: utf-8 -*-
"""
@Time    :2022/8/29 22:57
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""session--》
会话管理，常用于保持上下文的管理，保持会话状态（保持在同一个连接的操作）
用于解决http协议的无状态无连接特点
请求登录接口后，如果没有使用session会话管理的话，直接去请求其他接口，是请求不通的
所以要保持在同一个会话中进行

token:身份令牌，从登录接口返回，要获取token，首先要进行登录接口的调用,token放在请求头去传,
其他接口请求的时候带上token请求即可。

postman做接口关联：
    首先请求登录接口，然后从登录接口里面提取对应的token/cookie/session的参数出来，再test
    里面设置为环境变量然后再从其他接口的请求头信息里面去调用
    
get请求和post请求的区别：
1.get请求可以被缓存（方便再次get请求，把数据缓存下载，方便读取），post请求对通常不会被缓存
    get请求做不做缓存取决于业务场景，我认为是大多情况下是不应该做缓存的
    post请求增删改，更加不应该做缓存
2.get请求的参数是放在url上面去传的，而post请求的参数是放在body去传的
3.get请求的安全性要比post请求的安全性要低
4.post请求参数的数据体量要比get请求参数的数据体量要大很多（因为get请求的参数是放在url上面的
，url的长度是有限制；post请求的请求参数几乎是没有限制）
url长度限制为：
    不同的浏览器URL可以存储的长度不同：
        1、IE：最大2083个字符
        2、火狐：最大65536个字符
        3、谷歌：最大8182个字符
        但是: url可以存储多长的字符，也和服务有关
post请求参数大小限制为：
        不好定论，取决于发送这个情况的框架，python的requests（2M）和java的HttpURLConnection（8kb）和node.js的axios（2M）的长度也是不同的

怎么用request处理token或者是cookies，用session就可以了
"""


# import jsonpath
import requests
import time
# url2 = 'https://openapiv100.ketangpai.com//UserApi/login' #课堂派登录接口
# headers.yml = {'Content-Type': 'application/json'}
# dict_data = {'email': "15521048080",
#              'password': "822703304gsx",
#              'remember': "1",
#              'code': "",
#              'mobile': "",
#              'type': "login"}
# # res=requests.request(method='post',url=url2,json=dict_data,headers.yml=headers.yml)#Response<200>
# #后面加了.json() 是请求过后得到的json数据，用res变量来接收
# res=requests.request(method='post',url=url2,json=dict_data,headers.yml=headers.yml).json() #Response<200>
# print("json的内容：{}".format(res))
# #获取token  json提取数据的方法：变量名["key"]["key"]
# token = res['data']['token']
# print(token)
#
#
# url3 = 'https://openapiv5.ketangpai.com//CourseApi/semesterCourseList' #查看课程的列表接口
# header = {'Content-Type': 'application/json',
#           "token":token
#           } # 'token': res['data']['token']
# data = {
#     "isstudy": "1",
#     "search": "",
#     "semester": "2023-2024",
#     "term": "0",
#     "reqtimestamp": 1673077065749
# }
# ress = requests.request(method='post',url=url3,headers.yml = header,json = data)
# print(ress.json())

# session = requests.session()
# session.get()
# session.post()
# session.request()

class Test_ketangpai():
    headers = {'Content-Type': 'application/json'}  #共有类属性
    def __init__(self):  #  构造方法，在实例化一个对象后，都会去调用的方法
        #定义一个session，用来做会话管理
        self.session = requests.session()

    def login_api(self): #登录接口
        url1 = 'https://openapiv5.ketangpai.com//UserApi/login'

        data = {'email': "15521048080",
                     'password': "822703304gsx",
                     'remember': "1",
                     'code': "",
                     'mobile': "",
                     'type': "login"}
        res1 = self.session.request(method='post',url=url1,headers=self.headers,json=data)
        print('登录接口的json',res1.json())

    #查询课程的接口
    def chaxun_api(self):
        url2 = 'https://openapiv5.ketangpai.com//CourseApi/semesterCourseList'
        json_data2 = {
                'isstudy': "1",
                'search': "",
                'semester': "2021-2022",
                'term': "0",
                'reqtimestamp': 1661786299326
                }
        res2 = self.session.request(method='post',url=url2,headers=self.headers,json=json_data2)
        print('查询接口的json',res2.json())

    #查看内容的接口
    # def neirong_api(self):
    #     url3='https://openapiv100.ketangpai.com//UserApi/getUserBasinInfo'
    #     headers.yml={'Content-Type': 'application/json'}
    #     json_data ={"reqtimestamp": 1667530115590}
    #     res = self.session.post(url=url3,json=json_data,headers.yml=headers.yml)
    #     print('内容的json数据',res.json())
    #
    # def setting_api(self):
    #     url4 = 'https://openapiv100.ketangpai.com//UserApi/getUserVipSetting'
    #     headers.yml = {'Content-Type': 'application/json'}
    #     json_data = {"reqtimestamp": int(time.time())}
    #     res = self.session.post(url = url4,headers.yml=headers.yml,json = json_data)
    #     print(res.json())

#实例化一个对象zhangsan，然后对象去调用构造方法，构造方法里面有一个session，用于会话管理
# zhangsan = Test_ketangpai()
# #然后用zhangsan这个对象去调用里面的登录接口
# zhangsan.login_api()
# zhangsan.chaxun_api()
# zhangsan.neirong_api()
# zhangsan.setting_api()



# class Ketang_test():
#     def __init__(self):
#         self.session = requests.session()
#
#     def ketangpai_login(self):
#         login_url = 'https://openapiv5.ketangpai.com//UserApi/login'
#         login_data = {
#             "email": "15521048080",
#             "password": "822703304gsx",
#             "remember": "0",
#             "code": "",
#             "mobile": "",
#             "type": "login",
#             "reqtimestamp": 1683873810521
#                      }
#         login_method = 'post'
#         res = self.session.request(method=login_method,url=login_url,json=login_data).json()
#         print(res)
#
#     def chaxun(self):
#         chaxun_url = 'https://openapiv5.ketangpai.com/CourseApi/semesterList'
#         data = {
#             "isstudy": "1",
#             "search": "",
#             "reqtimestamp": 1683873811602
#                 }
#         method = 'post'
#         res = self.session.request(method=method,json=data,url=chaxun_url).json()
#         print(res)
#
# a = Ketang_test()
# a.ketangpai_login()
# a.chaxun()


class Ketang_test_1():
    def ketangpai_login(self):
        login_url = 'https://openapiv5.ketangpai.com//UserApi/login'
        login_data = {
            "email": "15521048080",
            "password": "822703304gsx",
            "remember": "0",
            "code": "",
            "mobile": "",
            "type": "login",
            "reqtimestamp": 1683873810521
                     }
        login_method = 'post'
        res = requests.request(method=login_method,url=login_url,json=login_data).json()
        print(res)
        self.token = res['data']['token']

    def chaxun(self):
        chaxun_url = 'https://openapiv5.ketangpai.com/CourseApi/semesterList'
        data = {
            "isstudy": "1",
            "search": "",
            "reqtimestamp": 1683873811602
                }
        method = 'post'
        headers = {"token":self.token}
        res = requests.request(method=method,json=data,url=chaxun_url,headers=headers).json()
        print(res)

a = Ketang_test_1()
a.ketangpai_login()
a.chaxun()













