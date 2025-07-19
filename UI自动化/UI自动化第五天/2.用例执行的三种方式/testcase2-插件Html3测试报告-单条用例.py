# -*- coding: utf-8 -*-
"""
@Time    :2022/8/23 18:45
@version :Python3.7.4
@Software:pycharm2020.3.2
"""


"""运行用例的第二种方式：运行指定的一条或者多条用例
操作步骤：
1.创建一个测试套件suite = unittest.TestSuite()
2.通过addTest()添加单条用例或者addTests()添加多条测试用例到测试套件suite，
        添加单条用例：suite.addTest(TestCase('用例的名字'))
        添加多条用例：suite.addTests(case_list),
            case_list=[TestCase('用例1的名字'),TestCase('用例2的名字')]
            case_list是一个列表，以列表的形式存储用例
3.创建一个执行器 runner = unittest.TextTestRunner() 
4.执行器执行套件:rnner.run(suite)
"""

from selenium import webdriver
import unittest
#这个模块是用来生成测试报告，生成的是自动化测试报告
from  HTMLTestRunner3 import HTMLTestRunner #TextTestRunner
from time import sleep
import time
from python基础.各种包的学习.time模块 import File_time_create, File_time_create_other_function


# from python基础.6.各种包的学习.time模块 import file_name_utils


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

if __name__ == '__main__':
    #此函数是这个文件执行的入口，如果运行此函数，那么就会执行函数体里面的代码
    """操作步骤：

    不生成测试报告步骤
    1.新建一个suite用来装用例：suite = unittest.TestSuite()
    2.用addTests这个方法把用例加到suite里面，多条用例的加
    3.创建一个执行器：runner = unittest.TextTestRunner()
    4.执行器执行suite里面的用例：runner.run(sutie)
    
    生成测试报告的步骤：
    1.新建一个suite用来装用例：suite = unittest.TestSuite()
    2.用addTest这个方法把用例加到suite里面
    3.创建一个执行器：runner = HTMLTestRunner()
    4.执行器执行suite里面的用例：runner.run(sutie)
    
    """
if __name__ == '__main__':
    """不生成测试报告"""
    # #第一步：创建一个测试套件suite来放测试用例，实例化一个对象suite
    #  #看源码
    # suite = unittest.TestSuite()
    # #第二步：把想要执行的用例通过addTest()或者addTests()增加到suite里面
    # #方式1：addTest()，增加单条测试用例,测试类名('测试用例')
    # # suite.addTest(Test_webtest_login('test_login_1'))
    # # suite.addTest(Test_webtest_login('test_login_2'))
    # # suite.addTest(Test_webtest_login('test_login_3'))
    # case_list = [Test_webtest_login('test_login_1'),Test_webtest_login('test_login_2')]
    # suite.addTests(case_list)
    # #第三步：创建一个runner执行器，用来执行测试套件
    # runner = unittest.TextTestRunner() #这种方式是生成不了HTML的测试报告的
    # #第四步：执行器执行整个测试套件
    # runner.run(suite)


    """生成测试报告"""
    #第一步：实例化一个suite的套件，用来装用例
    suite = unittest.TestSuite()
    #第二步：通过addTests的方式加入第一条和第二条用例到套件里面去,只能同一个类
    case_list = [Test_webtest_login('test_login_1')]
    suite.addTests(case_list)

    #第三步：创建一个执行器runner
    with open(file=File_time_create_other_function(),mode='wb') as file:
        runner = HTMLTestRunner(stream=file,  #流文件，用来存储数据的，把数据写进去file里面
                                verbosity=1,  #verbosity，测试报告的详细程度，最高是2，越高越详细
                                title='自动化测试报告', #这个参数是用来生成文件的title
                                description='简单的描述一下') #这个参数是用来生成描述的

        runner.run(suite)






