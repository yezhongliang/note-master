# -*- coding: utf-8 -*-
"""
@Time    :2022/8/29 21:43
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
用python做接口自动化，用到的库是requests库，是一个第三方库
pip install requests
get带参数，
需要注意get的参数是放在url上面传递的,
同时parmas也可以用来传递参数
参数与参数之间都是用的&符号来拼接起来

requests.request(method)   -->find_element(locator)-->find_element('xpath','locator')
requests.get()             -->find_element_by_id()
requests.post()            -->find_element_by_name()
requests.put()
requests.delete()
requests.options()
"""
#请求一下cms登录接口
import requests
# method = 'get'
# cms_login_url = 'http://192.168.203.180:8080/cms/manage/loginJump.do'
# #参数是字典的数据类型，是键值对
# cms_login_params ={"userAccount":"admin",
#                    "loginPwd":"123456"}

# response = requests.get(url=cms_login_url,params=cms_login_params).json()
# print(response)


# method = 'get'
# cms_login_url = 'http://192.168.203.180:8080/cms/manage/loginJump.do?userAccount=admin&loginPwd=123456'
# #参数是字典的数据类型，是键值对
# response = requests.get(url=cms_login_url).json()
# print(response)



method = 'get'
cms_login_url = 'http://192.168.203.180:8080/cms/manage/loginJump.do?userAccount=admin&loginPwd=123456'
#参数是字典的数据类型，是键值对
cms_login_params ={"userAccount":"admin",
                   "loginPwd":"123456"}


res = requests.request(method=method,url=cms_login_url).json()
print(res)

