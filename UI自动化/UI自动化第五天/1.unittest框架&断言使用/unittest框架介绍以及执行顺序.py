# -*- coding: utf-8 -*-
"""
@Time    :2022/8/22 22:28
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
from time import sleep

"""
python中的unittest框架，它是python自带的测试框架，unittest中最核心的四个概念-组件：
1.TestCase：测试用例，所有的测试用例的类，都要继承TestCase这个类
2.TestFixure：测试夹具，用于测试用例环境的搭建准备(driver=webdriver.Chrome())
和销毁(driver.quit())--初始化以及 回收资源
3.TestSuite：测试套件，用来把需要一起执行的测试用例集中放到一起执行，相当于一个篮子一样。
4.TestTextRunner：用来执行测试用例的
    HTMLTestRunner才可以生成html的测试报告

 1的详细解析：TestCase：就是我们的测试用例，unittest中提供了一个基本类TestCase，
可以用来创建新的测试用例，一个TestCase的实例（实例方法）就是一个测试用例；
unittest中测试用例规定要以test开头，否则不被unittest识别，执行顺序是：0->9，A->Z，a->z
用法：unittest.TestCase


2的详细解析：测试夹具，用于测试用例环境的搭建和销毁，即用例测试前准备环境的操作（SetUp前置条件），
测试后环境的还原已经资源的回收（TearDown后置条件）
unittest的测试夹具有两种使用方式，
一种是测试方法维度的setUp()和tearDown()；
    setUp:开始要做的事情
    tearDown：结束要做的事情
    每一条测试用例执行前都会调用setUp，执行后都会调用tearDown
    如果有10条用例，那就执行10次的setup和10次的teardown
    
一种是以测试类维度的setUpClass()和tearDownClass()，类方法
setupclass无论测试类里面有多少条用例，只执行1次
如果有10条测试用例，那么setupclass和teardownclass都只执行1次

面试题：
1.setup和teardown分别是用来做什么？
2.setup和setup class的区别是什么？
3.unittest的四大组件分别是什么？
4.unittest是如何加载用例的，选择执行的用例有哪些方式？
5.unittest是如何生成测试报告的？
6.有没用用过其他的生成测试报告的库？
7.unittest和pytest的区别是什么？



"""



# import unittest
# from selenium import  webdriver

#定义一个测试类，类的命名要以Test开头
# class Test_webtest_login(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://127.0.0.1:5000/signin')
#         self.driver.maximize_window()
#         sleep(2)
#     def tearDown(self) -> None:
#         self.driver.quit()
#
#     def test_login_1(self):
#         self.driver.find_element('name','username').send_keys('15521058080')
#         self.driver.find_element('name','password').send_keys('123456')
#         sleep(2)
#         self.driver.find_element('xpath','/html/body/form/p[3]/button').click()
#
#     def test_login_2(self):
#         self.driver.find_element('name', 'username').send_keys('18888888888')
#         self.driver.find_element('name', 'password').send_keys('123456')
#         sleep(2)
#         self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()
#
#     def test_login_3(self):
#         self.driver.find_element('name', 'username').send_keys('16666666666')
#         self.driver.find_element('name', 'password').send_keys('123456')
#         sleep(2)
#         self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()
#

# 定义一个测试类，类的命名要以Test开头,使用类方法的时候，需要用到@classmethod这个装饰器
# class Test_webtest_login(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         global driver
#         driver = webdriver.Chrome()
#         driver.get('http://127.0.0.1:5000/signin')
#         driver.maximize_window()
#         sleep(2)
#     @classmethod
#     def tearDownClass(cls) -> None:
#         driver.get('http://127.0.0.1:5000/signin')
#
#     def test_login_1(self):
#         self.driver.find_element('name','username').send_keys('15521058080')
#         self.driver.find_element('name','password').send_keys('123456')
#         sleep(2)
#         self.driver.find_element('xpath','/html/body/form/p[3]/button').click()
#
#
#     def test_login_2(self):
#         self.driver.find_element('name', 'username').send_keys('18888888888')
#         self.driver.find_element('name', 'password').send_keys('123456')
#         sleep(2)
#         self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()
#
#     def test_login_3(self):
#         self.driver.find_element('name', 'username').send_keys('16666666666')
#         self.driver.find_element('name', 'password').send_keys('123456')
#         sleep(2)
#         self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()
#
#
import unittest
# class Test_search(unittest.TestCase):
#     def test_A(self):
#         print('AAAAAAA')
#
#     def test_0(self):
#         print('000000000')
#
#     def test_a(self):
#         print('aaaaaaaaaa')
#
#     def haha(self):
#         print('hahahaha')


if __name__ == '__main__': #这个是这个py文件的入口
    unittest.main()  #执行所有的用例















































































