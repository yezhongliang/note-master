# -*- coding: utf-8 -*-
"""
@Time    :2022/8/23 0:27
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

from selenium import webdriver
from time import  sleep
"""
注册页面的输入 账号 以及 密码
"""
def zhuce(username,password):  #这里传两个值，一个是用户名，一个是密码
    driver= webdriver.Chrome() #实例化一个对象
    driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/reginfo.html') #打开注册页面
    driver.maximize_window()  #窗口最大化
    driver.find_element('name', 'accounts').send_keys(username) #根据name定位，输入username
    sleep(1)
    driver.find_element('name', 'pwd').send_keys(password) #根据name定位，输入password
    sleep(1)
    driver.quit()  #每条用例执行完后会有quit的操作