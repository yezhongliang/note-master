# -*- coding: utf-8 -*-
"""
@Time    :2022/8/20 23:30
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

# HTML,CSS,JS
# Selenium是底层基于JS语言开发。
# JS==Java Script,用来写前端的
# JAVA  =用来写后端的，属于后端语言
# Postman 也是用JS语言开发的
# Selenium的底层通信用的协议是：JSON wire protocol(翻译是协议)

# JS在自动化中最重要的两个应用的面试题：
#     1.可以用js语言把隐藏的元素设置为可见，再去定位。
#     场景：账号密码登录，账号输入框可以定位到，密码框定位不了，是因为密码框的元素被隐藏了。
#     需要设置visibility=visible才可以去定位  visible（可见的）
#     hidden是隐藏的元素
#
#     2.document的滚动条应用（懒加载），用js语言来实现滚动
#
#     面试题：对于一些页面隐藏了的属性，定位不了，你会如何去定位？
#      回答：只需要使用js，把visibitity这个参数这是为visible即可显示。visibility=hidden时隐藏

from selenium import webdriver
from time import  sleep
#
dr=webdriver.Chrome()
dr.get('https://www.nvidia.cn/gtc-global')
dr.maximize_window()

sleep(5)
dr.implicitly_wait(100)
# dr.find_element('xpath','//*[@id="J_footer"]/div[2]/div/div/div[5]/ul/li[1]/a').click()
#想要执行多次那就用for循环或者写多条的js
# dr.execute_script("window.scrollTo(0,500)")#滚动到底部
# sleep(3)
# dr.execute_script("window.scrollTo(500,1000)")#滚动到底部
# sleep(3)
# dr.execute_script("window.scrollTo(1000,10000)")#滚动到底部
# sleep(3)
# sleep(3)
# dr.execute_script("window.scrollTo(10000,20000)")#滚动到底部
# dr.execute_script("document.documentElement.scrollTop=0")#滚动到顶部


# driver = webdriver.Chrome()
# driver.get('https://www.ctrip.com/?')
# driver.maximize_window()
# sleep(10)
# driver.find_element('xpath','//*[@id="platformSeoFoot"]/div/div[1]/div[2]/div[1]/div/div[1]').click()
#
# sleep(10)

dr.find_element('xpath','//*[@id="nv-button-dd3c0cd89d"]/span/span').click()


