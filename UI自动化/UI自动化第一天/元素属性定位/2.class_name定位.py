# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 0:12
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""class_name定位，class属性值可能会重复
根据元素的class属性值来进行元素的定位
前提：一定要有class属性
"""
# 操作：打开百度页面，在百度输入框输入“疯狂星期四”,点击一下百度按钮
# 需要窗口最大化，并且点击完按钮之后，需要进行截图操作,需要用class name来定位

#导包
from selenium import  webdriver
from time import  sleep

#实例化一个对象driver
driver = webdriver.Chrome()

#窗口最大化
driver.maximize_window()

#打开网址
driver.get('https://www.baidu.com')

#按照class name对输入框进行定位并且输入，今天天气不咋地
driver.find_element("class name",'s_ipt nobg_s_fm_hover').send_keys('今天天气不咋地')
sleep(1)

#按照class name对按钮进行点击
driver.find_element('class name','btn self-btn bg s_btn').click()
sleep(1)

#截图
driver.get_screenshot_as_file('tianqi.png')

sleep(3)





















