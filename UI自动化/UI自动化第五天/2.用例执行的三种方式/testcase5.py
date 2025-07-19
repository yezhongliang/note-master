# -*- coding: utf-8 -*-
"""
@Time    :2022/12/29 17:33
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""换一个生成测试报告的模板，叫beautiful report
"""
import unittest
from BeautifulReport import BeautifulReport
import os
import time
from python基础.各种包的学习.time模块 import File_time_create_other_function


class Test_HtmlReport(unittest.TestCase):
    def test_1(self):
        '''描述,第一个测试用例'''
        print('test_1错误')
        self.assertNotEqual(1,2)

    def test_2(self):
        '''描述,第二个测试用例'''
        print('test_2正确')
        self.assertEqual(1, 1)

    def test_3(self):
        '''描述,第三个测试用例'''
        print('test_3错误')
        self.assertEqual(2, 3)


if __name__ == '__main__':
    # now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    # localpath = os.getcwd()
    # print('本文件目录位置：' + localpath)
    # filepath = os.path.join(localpath, 'BeautifulReport')
    # print('报告存放路径  ：' + filepath)
    # test_path = r'D:\TestTool\project_for12\UI自动化\UI自动化第五天\2.用例执行的三种方式'
    # discover = unittest.defaultTestLoader.discover(test_path,pattern='testcase5*.py') # 实例化一个测试套件suite
    # # 按文件名加载全部testxxx测试用例
    # filename = now + '.html'
    # # 加载执行用例生成报告
    # result = BeautifulReport(discover)
    # # 定义报告属性
    # result.report(description='webtest自动化测试报告', filename=filename, log_path=filepath)

    #声明测试用例的路径
    test_path = r'D:\TestTool\project_for12\UI自动化\UI自动化第五天\2.用例执行的三种方式'
    #声明测试报告的名字
    filename = File_time_create_other_function()
    #把用例加载导discover里面
    discover = unittest.defaultTestLoader.discover(test_path,pattern='testcase*.py')
    #用BeautifulReport执行discover
    result = BeautifulReport(discover)
    #生成测试报告
    result.report(description='webtest自动化测试报告', filename=filename)