# -*- coding: utf-8 -*-
"""
@Time    :2022/8/18 23:56
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""id定位,id属性是唯一的（id对于每一个元素来说，都是唯一的，不可能重复）
根据元素的id属性值来进行元素的定位
前提：一定要有id属性
输入文本：send_keys(''),传字符串进去
点击操作：click()
"""
# 操作：打开百度页面，在百度输入框输入“疯狂星期四”,点击一下百度按钮
# 需要窗口最大化，并且点击完按钮之后，需要进行截图操作
#导包
from selenium import  webdriver
from time import  sleep

#实例化一个对象driver
driver = webdriver.Chrome()

#driver对象打开百度页面
driver.get('http://www.baidu.com')

#窗口最大化
driver.maximize_window()
sleep(5)

#在输入框输入“疯狂星期四”,
# find_element方法需要传值进来，需要传定位的方式以及定位方式对应的属性值
driver.find_element("id",'kw').send_keys('疯狂星期四')
sleep(5)

#点击百度一下按钮
driver.find_element('id','su').click()
sleep(3)

#截图操作
driver.get_screenshot_as_file('KFC.jpg')







