# -*- coding: utf-8 -*-
"""
@Time    :2023/1/11 11:36
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
import  requests
import  time
import random



class ZaoShuJu():

    def __init__(self):
        self.session = requests.session()
        self.userAccount = int(time.time())
        self.username = 'zhangsan' + str(random.randrange(1,10000000))

    def login(self):
        login_url = 'http://192.168.203.170:8080/cms/manage/loginJump.do'
        params = {"userAccount":"admin",
                  "loginPwd":123456}
        res = self.session.request(method='post',url=login_url,data=params).json()
        print(res)

    def create_user(self):
        create_url = 'http://192.168.203.170:8080/cms/manage/saveSysUser.do'
        params = {"id":'',
                  'userName':self.username,
                  'userMobile':'15521048080',
                  'userEmail':'82270@qq.com',
                  'userAccount':self.userAccount,
                  'loginPwd':123456,
                  'confirmPwd':123456,
                  'userSex':1
                  }
        res = self.session.request(method='post',url=create_url,data=params).json()
        print(res)
while 1:
    a = ZaoShuJu()
    a.login()
    a.create_user()