# -*- coding: utf-8 -*-
"""
@Time    :2022/8/23 18:45
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
from time import sleep

"""运行用例的第一种方式：运行所有用例
操作步骤：
1.unittest.main()

执行自动化测试用例的方法：
1.执行一个py文件里面的所有用例：unitest.main的方法来执行
2.执行一个测试类里面的某些用例的方法：addTest(类名('方法名'))的方法或者addTests的方法来执行
3.执行某些测试类的方法：TestLoader的方法
4.执行某些py文件




"""
from selenium import webdriver
import unittest


# class Test_webtest_login(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://127.0.0.1:5000/signin')
#         self.driver.maximize_window()
#         sleep(2)
#
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
# if __name__ == '__main__':
#     #此函数是这个文件执行的入口，如果运行此函数，那么就会执行函数体里面的代码
#     unittest.main()
#     #运行用例的三种方法：
#     #第一种，直接再main下面去右键然后点击运行
#     #第二种，直接运行测试类左边的绿色符号
#     #第三种，点击工具栏的Run，选择你要执行的文件


import unittest
from selenium import  webdriver
class Test_webtest_login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:5000/signin')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_webtest_login_1(self):
        self.driver.find_element('xpath','/html/body/form/p[1]/input').send_keys('15521048080') #输入账号
        self.driver.find_element('xpath','/html/body/form/p[2]/input').send_keys('123456') #输入密码
        sleep(2)
        self.driver.find_element('xpath','/html/body/form/p[3]/button').click() #点击登录
        sleep(5)

    def test_webtest_login_2(self):
        self.driver.find_element('xpath', '/html/body/form/p[1]/input').send_keys('111111111')  # 输入账号
        self.driver.find_element('xpath', '/html/body/form/p[2]/input').send_keys('123456')  # 输入密码
        sleep(2)
        self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()  # 点击登录
        sleep(5)

    def test_webtest_login_3(self):
        self.driver.find_element('xpath', '/html/body/form/p[1]/input').send_keys(' ')  # 输入账号
        self.driver.find_element('xpath', '/html/body/form/p[2]/input').send_keys(' ')  # 输入密码
        sleep(2)
        self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()  # 点击登录
        sleep(5)


if __name__ == '__main__':
    unittest.main() #运行用例的第一种方法，运行当前文件的所有用例，所有的类


