# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 23:14
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
import time

"""窗口设置大小
1.窗口最大化 maximize
2.窗口最小化 minimize
3.指定窗口大小：driver.set_window_size(100,200)，100是宽，200是高
4.获取当前窗口的大小get_window_size()
"""
# 操作：打开一个窗口，先窗口最大化，打印当前的窗口的尺寸，然后停止2秒，然后窗口最小化，
# 打印当前窗口的尺寸，然后设置窗口指定的大小,然后quit窗口
from selenium import  webdriver
from time import  sleep

#实例化一个对象driver
driver = webdriver.Chrome()

#窗口最大化
driver.maximize_window()
#打印窗口的尺寸
print("最大化的窗口大小的值位：{}".format(driver.get_window_size()))
sleep(2)

#窗口最小化
driver.minimize_window()
#打印窗口的尺寸
print("最小化的窗口大小的值位：{}".format(driver.get_window_size()))
sleep(2)

#设置窗口的宽度位100，长度为200
driver.set_window_size(2000,2000) #到不了最大化的

sleep(5)
print(driver.get_window_size())
sleep(2)
driver.quit()




