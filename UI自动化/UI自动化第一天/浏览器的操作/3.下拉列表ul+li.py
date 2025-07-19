# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 20:12
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""ui+li，ul:节点，li:选项 ---禅道-建用例-功能用例-适用阶段
步骤：
    先定位到ul，并且将定位到的值附给变量a,再用变量a去找到li
    a=driver.find_element('xpath','ul的xpath')
    a.find_element_by('xpath','li的xath').click()
"""
from selenium import webdriver
from time import sleep
#实例化对象driver
driver = webdriver.Chrome()
#对象打开禅道
driver.get('http://127.0.0.1/zentao/user-login.html')
sleep(10)
