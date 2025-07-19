# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 1.
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""CSS选择器"""
from selenium import  webdriver
import  time

a = webdriver.Chrome()
a.get('https://www.baidu.com')
a.maximize_window()

a.find_element('css selector','#kw').send_keys('LOL')
time.sleep(2)

a.find_element('css selector','#su').click()
time.sleep(4)

a.quit()




