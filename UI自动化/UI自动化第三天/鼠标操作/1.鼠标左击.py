# -*- coding: utf-8 -*-
"""
@Software:pycharm2020.3.2.
@Time    :2022/8/20 22:36
@version :Python3.7.4
"""
import time

"""鼠标左击操作
1.导包
    from selenium.webdriver.common.action_chains import ActionChains as AC
2.实例对象
    action=AC(driver)
3.调用方法
    action.click(ele)
4.统一发送
    action.perform()  #核心，如果不执行perform方法，上面的鼠标操作是不会执行的

实际上在调用 Actionchains 类的方法时，不会立即执行鼠标操作，
而是会将所有的操作按顺序存放在一个队列里，
最终调用 perform() 方法时，队列中的操作会依次进行

消息队列：
    先进先出
    先进后出
"""
# 案例1：对百度的搜索输入hello，点击百度一下按钮(用鼠标的方式点击)
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

driver.maximize_window()

#输入hello
sleep(2)
driver.find_element('id','kw').send_keys('hello')
# driver.find_element('id','su').click()
sleep(2)
#使用action chains的方式去点击百度一下按钮
action=AC(driver)

#实例化完了action之后，就可以去使用整个action去左击，右击，双击，拖拉拽
#百度一下按钮的ele位：driver.find_element('id','su')
on_element = driver.find_element('id','su')
action.click(on_element)

sleep(2)
#把存储在perform的操作一次性释放出去
action.perform()
sleep(5)



















