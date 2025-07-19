# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 0:46
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""partial link text定位
partial link text:文本超链接的模糊匹配   partial:模糊
前提：定位的元素是链接标签 即a标签
hao123
h ,a ,o, 1, 2 ,3 ha ao 123,23,hao,hao1,hao12,hao123---OK的
hao13 hao2 hao3 hao13--不OK

"""
# 案例1：打开百度首页，通过partial_link_text（链接文本）定位到hao123按钮，并进
from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.get('https://www.baidu.com')
d.maximize_window()
sleep(1)
d.find_element('partial link text','hao12').click()
sleep(3)
