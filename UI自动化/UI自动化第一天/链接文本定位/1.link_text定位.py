# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 0:46
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""link text定位与前面4个定位有所不同，它专门用来定位文本超链接  
link:超链接https://www.baidu.com
text:文本
link_text:文本超链接的全匹配   精准匹配  123456
前提：定位的元素是链接标签 即a标签
"""
from selenium import  webdriver
from time import  sleep
# 案例1：打开百度首页，通过link_text（链接文本）定位到hao123按钮，并进行点击
d = webdriver.Chrome()
d.maximize_window()
d.get('http://www.baidu.com')
d.find_element('xpath','//*[@id="s-top-left"]/a[2]').click()
sleep(3)


# 案例2：根据xpath的绝对路径路径定位定位百度的输入框和百度一下的按钮
















