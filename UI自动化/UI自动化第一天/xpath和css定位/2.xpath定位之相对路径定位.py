# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 1
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
xpath定位
xpath定位方式：绝对路径、相对路径
"""

from selenium import webdriver
from time import sleep
#实例化一个对象driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
#定位百度输入框---xpath的绝对路径定位
driver.find_element('xpath','//*[@id="kw"]').send_keys('春天到了，万物困了')
sleep(2)
#定位百度一下按钮
driver.find_element('xpath','//*[@id="su"]').click()
sleep(3)
#再去quit浏览器
driver.quit()


# # 面试题：xpath定位中，相对路径和绝对路径哪个更加贴合实际项目的需要？为什么？
# 在实际中，常用的是相对路径，因为相对路径可以忽略很多的前面代码的路径的改变。
# 前端改了代码，大部分相对路径都是不需要修改的，如果你用的绝对路径下某个页面的元素路径改了
#一点点，那么需要重新去复制整个绝对路径
#
# json数据：..表示忽略所有层级
# //input[@id="kw"]  分解：
# // 表示忽略所有层级       /表示下一个节点
#   *  表示匹配所有标签
#   @表示选择某个属性 属性不需要引号，但是属性值是需要引号的
#
# //*[@id="kw"]
# //:表示忽略所有层级，找到这个标签
# *表示所有标签
# @id=‘kw’表示这个属性=属性值
