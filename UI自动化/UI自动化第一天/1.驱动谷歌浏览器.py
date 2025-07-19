# -*- coding: utf-8 -*-
"""
@Time    :2022/8/18 22:51
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""需要把谷歌浏览器的驱动chromedriver放到python的根目录下面
"""

#导包：
from selenium import webdriver
from time import  sleep

#实例化一个对象driver，这个driver其实就是浏览器
# driver_chrome= webdriver.Chrome()
driver_FireFox = webdriver.Firefox()
#对象就可以去做事情了，包括打开某个页面
driver_FireFox.get('https://www.jd.com/')
sleep(1)

#窗口个最大化
driver_FireFox.maximize_window()

#刷新一下
driver_FireFox.refresh()

#截屏
driver_FireFox.get_screenshot_as_file('18ban.png')














