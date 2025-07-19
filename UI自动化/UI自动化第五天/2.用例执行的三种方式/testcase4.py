# -*- coding: utf-8 -*-
"""
@Time    :2022/12/29 16:07
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
from zmail邮件发送测试报告.发送邮件带上附件 import send_mail_utils

"""
根据文件的命名来选择运行哪些py文件
步骤：
1.声明一个装测试用例py文件的文件夹路径
2.用discover用来读取
3.HTMLTestRunner
4.runner.run
"""
from selenium import webdriver
import unittest
from HTMLTestRunner3 import  HTMLTestRunner

from python基础.各种包的学习.time模块 import File_time_create_other_function


class TestCase_6(unittest.TestCase):
    def setUp(self) -> None:
        """做初始化操作,所有用例都会执行这个setup的操作"""
        global driver
        driver= webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.maximize_window()
    def tearDown(self) -> None:
        """做资源回收工作，所有的用例都会执行这个teardown的操作"""
        driver.quit()

    def test_1(self):
        print('这里写测试用例test_1的操作')

    def test_2(self):
        print('这里写测试用例test_2的操作')

    def test_3(self):
        print('这例写测试用例test_3的操作')

class TestCase_7(unittest.TestCase):
    def test_11(self):
        print('hello world')

class TestCase_8(unittest.TestCase):
    def test_22(self):
        print('hello python')

if __name__ == '__main__':
    #test_path是装py文件用例的文件夹，翻译过来是测试路径
    test_path = r"D:\TestTool\project_for12\UI自动化\UI自动化第五天\2.用例执行的三种方式"
    discover = unittest.defaultTestLoader.discover(start_dir=test_path, pattern = 'testcase*.py')
    #pattern是用来进行模糊搜索文件名字的表达式

    # discover = unittest.defaultTestLoader.discover(test_path, pattern='testcase1-没有测试报告生成.py')
    with open(file=File_time_create_other_function(),mode='wb') as file:  #wb：二进制的覆盖写
        runner=HTMLTestRunner(stream=file,
                              verbosity=1,
                              title=None,
                              description=None)
        runner.run(discover)



# 今晚作业：
# 1.写两个测试类，一个是登录webtest的测试类，一个是百度搜索的测试类，需要继承TestCase类，一个类里面需要写5条测试用例，需要用导setup和teardown
# 2.运行这两个类，不需要生成测试报告
# 3.运行webtest登录类的第一条测试用例，不生成测试报告报告
# 4.运行百度搜索的第一条测试用例，生成结合time模块的测试报告
# 5.一次性运行两个类，需要生成结合time模块的测试报告
# 6.创建两个py文件，第一个文件命名为：test_webtest_testcase,第二个文件命名为test_webtest_testcase,
# 每个文件里面需要有两个测试类，每个测试类里面需要有2条测试用例，然后根据文件名的方式运行这两个py文件（参考testcase5.py这个文件）

"""unittest执行用例的几种方法：
1.unittest.mian()执行所有的用例，但是生成不了测试报告
2.addtest/addtests的方法，用TestTextRunner，也生成不了测试报告
3.loader方法，收集单个文件类名来执行，结合HTMLTestRunner来生成测试报告
4.discover方法，收集testpath目录里面的所有满足pattern表达式的所有测试文件名，也可以结合HTMLTestRunner
来生成测试报告
"""

