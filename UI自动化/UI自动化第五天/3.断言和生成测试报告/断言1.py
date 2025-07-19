# -*- coding: utf-8 -*-
"""
@Time    :2022/8/23 23:15
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""UI自动化的断言：
1.什么是断言？
断言就是用来判断我们的UI自动化脚本或者接口自动化脚本是否操作成功
断言是用来校验最后用例是否执行成功的操作。
断言的关键字: assert

一条用例是否通过取决的是断言是否通过！！！！

"""
from selenium import webdriver
import unittest
from time import  sleep
import time

from HTMLTestRunner3 import HTMLTestRunner

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        """做初始化操作,所有用例都会执行这个setup的操作"""
        global driver
        driver= webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.maximize_window()
        sleep(2)
    def tearDown(self) -> None:
        """做资源回收工作，所有的用例都会执行这个teardown的操作"""
        driver.quit()

    def test_1(self):
        # print('这里写测试用例test_1的操作')
        # driver.find_element('name','accounts').send_keys('test')
        # sleep(1)
        # driver.find_element('name','password').send_keys('123456')
        # sleep(1)
        # driver.find_element('xpath','/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
        # sleep(5)
        # ele = driver.find_element('xpath','/html/body/div[2]/div/ul[1]/div/div/em[2]')
        # #获取test,欢迎来到
        # neirong = ele.text
        # #用变量url1去接收当前driver的url地址
        # neirong1 = '欢迎来到'
        # self.assertIn(neirong1,neirong)

        #获取当前的url
        url1 = driver.current_url  #百度的url
        sleep(2)
        driver.find_element('link text','hao123').click()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        url2 = driver.current_url  #hao123的url

        url3 = 'https://www.hao123.com/?src=from_pc'
        #如果url1 和url2相等的，那就说明打开hao123网址成功，并且条跳转也是成功的，那最终说明
        #的是hao123这个超链接跳转是可用的
        self.assertEqual(url3,url2,msg='通过的')
        sleep(2)
        #断言的操作assertEqual(a,b)  如果a=b，则断言成功，否则断言失败
        # self.assertNotEqual(url1,url2)
        # self.assertEqual(url1,url2)
        # title = driver.title
        # self.assertIn('百度一下',title)  #title是  百度一下，你就知道
        # url1 = driver.current_url
        # url2 = 'https://pan.baidu.com/disk/main?from=homeFlow#/index?category=all'

        # self.assertEqual(url1,url2) #如果url1=url2，那就说明登录成功；反之失败

    # def test_2(self):
    #     print('这里写测试用例test_2的操作')
    #
    # def test_3(self):
    #     print('这例写测试用例test_3的操作')
if __name__=='__main__':
    # 执行所有用例，这是运行的第一种方法
    # unittest.main()

    # 执行指定的用例，这是运行的第二种方法:
    # 第一步：创建一个套件suite来放测试用例
    suite = unittest.TestSuite()
    # 第二步：把想要执行的用例通过addTest()或者addTests()增加到suite里面
    # 方式1：addTest()
    # suite.addTest(TestCase('test_3')) #把test_3增加进来
    # suite.addTest(TestCase('test_1')) #再把test_1增加进来，此时有两条用例
    # 方式2：addTest()
    case_list = [TestCase('test_1')]  # ,TestCase('test_3')
    suite.addTests(case_list)
    # 第三步：创建执行器，两个方式：
    # 方式1：通过runner = unittest.TextTestRunner(),文本执行器
    # runner = unittest.TextTestRunner()
    # 方式2：通过runner = HTMLTestRunner()，HTML执行器
    file = open('./report.html','wb')#stream=sys.stdout, verbosity=1, title=None, description=None
    runner = HTMLTestRunner(stream=file,  # 流文件
                            verbosity=2,  # 报告的详细程度,2 1 0，2最详细
                            title='222222222222222222',  # 报告的title
                            description='111111111111')  # 报告的描述
        # 第四步：执行器执行测试套件
    runner.run(suite)  # .表示成功，E表示错误
    file.close()




# 题目2：学习如何使用beautiful report这个好看的测试报告


