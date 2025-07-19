# -*- coding: utf-8 -*-
"""
@Time    :2022/10/29 14:22
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
import  unittest
from HTMLTestRunner3 import HTMLTestRunner #这一个库是用来生成测试报告的

class Test_Class(unittest.TestCase):
    def setUp(self) -> None:
        print('这是setup的操作')
    def tearDown(self) -> None:
        print('这是teardown的操作')

    def test1(self):
        print(11111111111)
    def test2(self):
        print(222222222222)
    def aa_test(self):
        print('这一条不是测试用例')
    def test3(self):
        print(333333333333333)
if __name__ == '__main__':
    unittest.main()
    # #1.创建一个测试套件
    # suite = unittest.TestSuite()
    #
    # #2.往测试套件里面增加用例
    # case_list = [Test_Class('test1'),Test_Class('test2')]
    # suite.addTests(case_list)
    #
    # #3.创建一个执行器，用的是HTMLTextRunner
    # file = open('./report.html',mode='wb')
    # runner = HTMLTestRunner(stream=file,
    #                         verbosity=2,
    #                         title='这个是title1111111111111111111',
    #                         description='这个是描述11111111111111111111')
    #
    # #4.执行器执行套件里面的用例
    # runner.run(suite)








