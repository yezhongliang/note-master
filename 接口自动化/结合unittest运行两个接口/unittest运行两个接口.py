# -*- coding: utf-8 -*-
"""
@Time    :2022/8/30 0:26
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
import unittest
import requests
from HTMLTestRunner3 import  HTMLTestRunner
from zmail邮件发送测试报告.发送邮件带上附件 import send_mail_utils


class Test_api(unittest.TestCase):
    # 用例：我需要登录到系统里面，请求登录接口，然后再去请求查看数据的接口，请求增加数据的接口，删除数据的接口
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls) -> None:
        pass
     #接口自动化的过程中，难免会请求到一些增加数据的接口，这些增加的数据其实是垃圾数据
    #我们的数据库尽量少的存储这些垃圾数据，这个时候就要用pymysql对数据进行连接，把增加的
    #垃圾数据清除掉
        # pymysql()
        #删除数据用delete操作去删除

    def test_api_login(self):
        url1 = 'https://openapiv5.ketangpai.com//UserApi/login'
        headers1 = {'Content-Type': 'application/json'}
        json_data1 = {'email': "15521048080",
                     'password': "822703304gsx",
                     'remember': "1",
                     'code': "",
                     'mobile': "",
                     'type': "login"}
        res1 = self.session.post(url=url1,headers=headers1,json=json_data1)
        print(res1.json())
        #assertEqual 里面的两个参数相等的话，就断言成功，说明用例成功
        #里面的这两个参数位置可以调换
        #res1 是返回的整个响应体，.json()把请求体里面的json数据提取出来。
        self.assertEqual(res1.json()['message'],'访问成功')  #unittest的断言
        print(res1.json())


    def test_api_search(self):
        url2 = 'https://openapiv5.ketangpai.com//CourseApi/semesterCourseList'
        headers2 = {'Content-Type': 'application/json'}
        json_data2 = {
                'isstudy': "1",
                'search': "",
                'semester': "2021-2022",
                'term': "0",
                'reqtimestamp': 1661786299326
                }
        res2 = self.session.post(url=url2,headers=headers2,json=json_data2).json()
        print(res2)
        self.assertEqual(res2['message'],'访问成功')

    def test_chaxun(self):
        chaxun_url = 'https://openapiv5.ketangpai.com/CourseApi/semesterList'
        data = {
            "isstudy": "1",
            "search": "",
            "reqtimestamp": 1683873811602
                }
        method = 'post'
        res = self.session.request(method=method,json=data,url=chaxun_url).json()
        print(res)


if __name__ == '__main__':
    # unittest.main()
    #创建一个套件
    suite = unittest.TestSuite()
    #把用例加到套件里面,addTest addTests(case_list)
    suite.addTest(Test_api('test_api_login'))
    suite.addTest(Test_api('test_api_search'))
    suite.addTest(Test_api('test_chaxun'))
    #创建一个runner执行器
    file = open('./report18.html', mode='wb')  # stream=sys.stdout, verbosity=1, title=None, description=None
    runner = HTMLTestRunner(stream=file,  # 流文件
                            verbosity=2,  # 报告的详细程度,2 1 0，2最详细
                            title='我是title，请看我',  # 报告的title
                            description='我是描述我是描述——请看我')  # 报告的描述
    runner.run(suite)
    file.close()
    #执行器执行runner
    #最终把生成出来的邮件发送出去
    send_mail_utils()

    #jenkins运行脚本：python +脚本的绝对路径