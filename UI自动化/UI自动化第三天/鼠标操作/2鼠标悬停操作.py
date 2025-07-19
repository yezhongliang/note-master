# -*- coding: utf-8 -*-
"""
@Time    :2022/8/20 22:36
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""鼠标悬停操作
1.导包
     from selenium.webdriver.common.action_chains import ActionChains as AC
2.实例对象
    AC(driver)
3.调用方法
    action.move_to_element(ele)
4.统一发送
    action.perform()
    
定位鼠标的快捷方式：ctrl +shift +c

实际上在调用 Actionchains 类的方法时，不会立即执行鼠标操作，
而是会将所有的操作按顺序存放在一个队列里，
最终调用 perform() 方法时，队列中的操作会依次进行
"""
from time import  sleep
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC

# 任务：打开百度网址，然后使用鼠标悬停操作，把鼠标放在更多上面，然后进行截图

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

driver.maximize_window()
sleep(2)

action = AC(driver)

element = driver.find_element('link text','更多')
action.move_to_element(element)
action.perform()

driver.get_screenshot_as_file('更多.png')

sleep(2)























