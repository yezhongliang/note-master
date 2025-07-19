import requests
import unittest
from python基础.各种包的学习.PYMYSQL操作.基本使用_1 import mysql_connection_utils


class Test_cms(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls) -> None:
        mysql_connection_utils()


    def test_login(self):
        login_url = 'http://192.168.203.182:8080/cms/manage/loginJump.do'
        login_method = 'post'
        login_data = {"userAccount":"admin",
                      "loginPwd":"123456"}

        res = self.session.request(method=login_method,url=login_url,data=login_data).json()
        print(res)
        # self.assertEqual()

    def test_user_build(self):
        add_url = 'http://192.168.203.182:8080/cms/manage/saveSysUser.do'
        method = 'post'
        adduser_params = {"userName": "test_cms_1",
                          "userSex": "1",
                          "userMobile": "18320621608",
                          "userEmail": "924993987@qq.com",
                          "userAccount": "test_cms_1",
                          "loginPwd": "123456",
                          "confirmPwd": "123456"}
        res = self.session.request(method=method, url=add_url, params=adduser_params).json()
        print(res)

if __name__ == '__main__':
    unittest.main()