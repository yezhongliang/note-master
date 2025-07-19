# -*- coding: utf-8 -*-
"""
@Time    :2022/8/23 22:52
@version :Python3.7.4
@Software:pycharm2020.3.2
"""


"""运行用例的第三种方式：根据测试类的名称运行单个类的测试用例或者多个类的测试用例
操作步骤：
1.创建一个测试套件suite = unittest.TestSuite()
2.创建一个loader，loader=unittest.loader()然后通过loader的方式把测试类添加到套件suite里面
    suite.addTests(loader.loadTestsFromTestCase(TestCase))#增加了一个测试类，如果有多个，则继续加，如下：
    suite.addTests(loader.loadTestsFromTestCase(其他类名))
3.创建一个执行器 runner = HTMLTestRunner()
4.执行器执行套件:rnner.run(suite)
"""
from selenium import webdriver
import unittest
from HTMLTestRunner3 import  HTMLTestRunner
from time import sleep
from python基础.各种包的学习.time模块 import File_time_create_other_function

class TestCase_0(unittest.TestCase):
    def setUp(self) -> None:
        """做初始化操作,所有用例都会执行这个setup的操作"""
        self.driver= webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
    def tearDown(self) -> None:
        """做资源回收工作，所有的用例都会执行这个teardown的操作"""
        self.driver.quit()

    def test_1(self):
        print('这里写测试用例test_1的操作')
        #点击hao123之前的句柄：
        first = self.driver.current_window_handle
        sleep(2)
        #点击hao123之后的句柄：
        self.driver.find_element('link text','hao123').click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        sleep(2)
        second = self.driver.current_window_handle
        self.assertNotEqual(first=first,second=second)

    def test_2(self):
        print('这里写测试用例test_2的操作')

    def test_3(self):
        print('这例写测试用例test_3的操作')

class TestCase_1(unittest.TestCase):
    def test_11(self):
        print('hello world')

class TestCase_2(unittest.TestCase):
    def test_22(self):
        print('hello python')

class Test_webtest_login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000/signin')
        self.driver.maximize_window()
        sleep(2)
    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_1(self):
        self.driver.find_element('name','username').send_keys('15521058080')
        self.driver.find_element('name','password').send_keys('123456')
        sleep(2)
        self.driver.find_element('xpath','/html/body/form/p[3]/button').click()

    def test_login_2(self):
        self.driver.find_element('name', 'username').send_keys('18888888888')
        self.driver.find_element('name', 'password').send_keys('123456')
        sleep(2)
        self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()

    def test_login_3(self):
        self.driver.find_element('name', 'username').send_keys('16666666666')
        self.driver.find_element('name', 'password').send_keys('123456')
        sleep(2)
        self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()

class Test_webtest_login_copy(unittest.TestCase):
        def setUp(self) -> None:
            self.driver = webdriver.Chrome()
            self.driver.get('http://127.0.0.1:5000/signin')
            self.driver.maximize_window()
            sleep(2)

        def tearDown(self) -> None:
            self.driver.quit()

        def test_login_1(self):
            self.driver.find_element('name', 'username').send_keys('15521058080')
            self.driver.find_element('name', 'password').send_keys('123456')
            sleep(2)
            self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()

        def test_login_2(self):
            self.driver.find_element('name', 'username').send_keys('18888888888')
            self.driver.find_element('name', 'password').send_keys('123456')
            sleep(2)
            self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()

        def test_login_3(self):
            self.driver.find_element('name', 'username').send_keys('16666666666')
            self.driver.find_element('name', 'password').send_keys('123456')
            sleep(2)
            self.driver.find_element('xpath', '/html/body/form/p[3]/button').click()


if __name__=='__main__':
    #执行用例的第三种方法：使用loader
    #第一步：创建一个测试套件
    suite = unittest.TestSuite()
    #第二步：在测试套件中加入用例（按照类和模块加），用loader的方法
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestCase_0))
    suite.addTests(loader.loadTestsFromTestCase(TestCase_1))

    #第三步：创建执行器
    with open(file=File_time_create_other_function(),mode='wb') as file1:
        runner = HTMLTestRunner(stream=file1,
                                verbosity=1,
                                title='恐怖周一',
                                description='描述')

     #第四步：执行器执行测试套件
        runner.run(suite)

    #断言，断言的作用是用来判断一条用例是否执行通过
    # unittest会自带有断言的方法：
    # in ,not in  ,equal ,not equal


