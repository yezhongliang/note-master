# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 22:47
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
chrome无头模式设置 
1.声明一个谷歌配置对象：opts=webdriver.ChromeOptions()  opts = options-翻译的意思是选项的意思
2.设置headless属性值，True表示无头模式，False表示正常模式
driver = webdriver.Chrome(options=opts)

无头模式应用的场景：
网站及应用测试
JavaScript库测试(selenium的底层就是JS来写)  ----html css js
后台运行多个UI自动化测试（多个处理的就是兼容性测试）
优点：稳定，减少电脑的性能开销，运行速度快
缺点：调试不方便
"""
#正常模式
# from selenium import webdriver
# from time import  sleep
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# if driver.title =='百度一下，你就知道':
#     print('OK')
# else:
#     print('不OK')
# sleep(2)
# driver.quit()

#无头模式
#导包
from selenium import webdriver
import time
#时间戳：格林威治 时间1970年1月1号起到现在经过了多少秒
time1 = time.time()
print("当前的时间戳：",time1)
# #声明配置对象opts
opts = webdriver.ChromeOptions()
#配置对象去设置无头模式
opts.headless=True   #headless ==翻译过来就是无头的意思

#添加到实例对象中
driver = webdriver.Chrome(options=opts)

driver.get('http://www.baidu.com')

driver.maximize_window()

time.sleep(2)
driver.find_element('id','kw').send_keys('无头哈哈')
driver.find_element('id','su').click()

driver.get_screenshot_as_file('无头怪兽.png')

time.sleep(2)

driver.quit()

time2 = time.time()
time3 = time2-time1
print('headless持续的时间为：{}'.format(time3)) #8.084246397018433

