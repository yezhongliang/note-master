# -*- coding: utf-8 -*-
"""
@Time    :2022/8/22 23:08
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""
from time import  sleep
"""
注册页面的输入 账号 以及 密码
"""
def zhuce_cls(driver,username,password):
    driver.find_element('name', 'accounts').send_keys(username)
    sleep(1)
    driver.find_element('name', 'pwd').send_keys(password)
    sleep(1)