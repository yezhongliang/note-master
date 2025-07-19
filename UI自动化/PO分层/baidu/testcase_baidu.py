# -*- coding: utf-8 -*-
"""
@Time    :2022/8/25 0:18
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
import unittest
from selenium import  webdriver

class TestCaseBaiduSearch():
    def test01(self):
        """对于实现测试用例的时候，我们关注测试步骤，测试数据，断言
        测试步骤：打开浏览器--打开百度--输入自动化测试--点击百度一下
        不需要关注元素如何去定位，如何去操作，移动背后（PO页面去）"""
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        driver.implicitly_wait(10)
        driver.find_element('id','kw').send_keys('大闸蟹')
        driver.find_element('id','su').click()
        driver.quit()
    def test02(self):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        driver.implicitly_wait(10)
        driver.find_element('id','kw').send_keys('月饼')
        driver.find_element('id','su').click()
        driver.quit()
if __name__ == '__main__':
    unittest.main()