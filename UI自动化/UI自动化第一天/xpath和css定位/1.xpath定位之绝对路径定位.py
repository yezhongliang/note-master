# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 1
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""xpath定位--路径定位
xpath定位方式：绝对路径、相对路径
"""
# 案例1：根据xpath的绝对路径路径定位定位百度的输入框和百度一下的按钮
from selenium import webdriver
from time import sleep
#实例化一个对象driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com/')
#定位百度输入框---xpath的绝对路径定位
sleep(2)
driver.find_element('xpath','/html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[1]/input').send_keys('春天到了，万物困了')
sleep(2)
#定位百度一下按钮
driver.find_element('xpath','/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input').click()
sleep(3)
#再去quit浏览器
driver.quit()


# 面试题：xpath定位中，相对路径和绝对路径哪个更加贴合实际项目的需要？为什么？
#  //*[@id="kw"]  分解：
#  // 表示忽略所有层级       /表示下一个节点
#  *  表示匹配所有标签
#  @表示选择某个属性

