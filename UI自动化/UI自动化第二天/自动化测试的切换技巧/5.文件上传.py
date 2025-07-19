# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 23:38
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""文件路径只能选用绝对路径"""
from selenium import   webdriver
from time import sleep
driver =  webdriver.Chrome()
driver.get('http://127.0.0.1:5000/signin')
driver.maximize_window()
#登录，输入账号和密码
driver.find_element('xpath','/html/body/form/p[1]/input').send_keys('15521048080')
sleep(1)
driver.find_element('xpath','/html/body/form/p[2]/input').send_keys('123456')
sleep(1)
#点击登录
driver.find_element('xpath','/html/body/form/p[3]/button').click()
sleep(1)

#通过xpath的方式定位到上文件按钮
driver.find_element('xpath','//*[@id="testtable"]/tbody/tr[1]/td[2]/input').\
    send_keys(r'D:\TestTool\project_for18\UI自动化\UI自动化第二天\自动化测试的切换技巧\test.txt')
sleep(5)

#点击回家看笔记


