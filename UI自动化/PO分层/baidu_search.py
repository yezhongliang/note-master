# -*- coding: utf-8 -*-
"""
@Time    :2022/8/24 23:59
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

import unittest
from selenium import  webdriver

class TestCaseBaiduSearch():
    def test01(self):
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