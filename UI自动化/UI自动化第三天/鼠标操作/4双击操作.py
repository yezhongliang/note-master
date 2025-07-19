# -*- coding: utf-8 -*-
"""
@Time    :2022/8/20 22:36
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""鼠标双击操作
1.导包
    from selenium.webdriver.common.action_chains import ActionChains as AC
2.实例对象
    action=AC(driver)
3.调用方法
    action.dubble_click(ele)
4.统一发送
    action.perform()
    
实际上在调用 Actionchains 类的方法时，不会立即执行鼠标操作，
而是会将所有的操作按顺序存放在一个队列里，
最终调用 perform() 方法时，队列中的操作会依次进行
"""

# 验证方法：双击两次即是选中。


from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
import time


