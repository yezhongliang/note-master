# -*- coding: utf-8 -*-
"""
@Time    :2022/8/20 21:47
@version :Python3.7.4
@Software:pycharm2020.3.2
"""


"""键盘操作--Keys 
1.导包
    from selenium.webdriver.common.keys import Keys
2.调用
    send_keys(Keys.Back_SPACE)   删除键（BackSpace）
    send_keys(Keys.SPACE)       空格键
    send_keys(Keys.ENTER)        回车键
    send_keys(Keys.CONTROL,'a')  全选
    send_keys(Keys.CONTROL,'c')  复制
    send_keys(Keys.CONTROL,'v')  粘贴
    send_keys(Keys.F1)  键盘F1
    send_keys(Keys.F5)  键盘F5
"""

from selenium.webdriver.common.keys import Keys
from selenium import  webdriver
from time import sleep

"""键盘操作--Keys 
1.导包
    from selenium.webdriver.common.keys import Keys
2.调用
    send_keys(Keys.Back_SPACE)   删除键（BackSpace）
    send_keys(Keys.SPACE)       空格键
    send_keys(Keys.ENTER)        回车键
    send_keys(Keys.CONTROL,'a')  全选
    send_keys(Keys.CONTROL,'c')  复制
    send_keys(Keys.CONTROL,'v')  粘贴
    send_keys(Keys.F1)  键盘F1
    send_keys(Keys.F5)  键盘F5
"""

# 案例1：打开百度-》输入Seleniumm-》按删除键Backspace删除一个m  Selenium
# -》再输入空格+‘厉害’-》ctrl+a全选所有文本-》然后剪切---》剪切完再粘贴下来，再点击搜索，回车
# 点击第一个搜索出来的，并且在新页面的输入框搜索‘18班冲冲冲’

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element('id','kw').send_keys('Seleniumm')
sleep(2)
driver.find_element('id','kw').send_keys(Keys.BACKSPACE)
sleep(2)
driver.find_element('id','kw').send_keys(Keys.SPACE+'厉害')
sleep(10)















#打开浏览器，打开百度，然后输入selenium，然后删掉m
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.set_window_size(888,888)
# driver.find_element('id','kw').send_keys('selenium')
# sleep(2)
# driver.find_element('id','kw').send_keys(Keys.BACK_SPACE)
# sleep(4)






