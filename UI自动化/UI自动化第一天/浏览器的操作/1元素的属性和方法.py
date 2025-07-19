# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 11:17
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""
"""元素属性和方法
element = driver.find_element('定位的方式',属性值)
获取元素的尺寸：element.size
获取元素坐标：element.location  
获取元素的文本内容：element.text
获取元素的属性值：element.get_attribut(属性)  通过传入不同的属性名来获取对应属性值class,id,name，value等等

获取页面的url：driver.current_url   对url获取再进行判断，是一种常用的判断方式
获取页面的title：driver.title   #title的翻译是标题，窗口名字
"""
from selenium import webdriver
from time import sleep

#实例化一个对象
driver = webdriver.Chrome()

#对象打开网址百度
driver.get('https://www.baidu.com')

#窗口给最大化
driver.maximize_window()
sleep(2)

#element是页面的元素，
element = driver.find_element('id','su') #百度一下的元素
print(element.size)  #{'height': 44, 'width': 108}  高44 宽108
sleep(2)
# #获取百度搜索框的坐标
print(element.location)  #{'x': 994, 'y': 188}
sleep(2)
# #获取百度首页底部的备案信息
element2 = driver.find_element('xpath','//*[@id="bottom_layer"]/div/p[6]/a')
print(element2.text)
# #定位到百度搜索按钮，并获取这个标签的其他属性值,根据属性来获取对应的属性值
element3 = driver.find_element('id','su')
print(element3.get_attribute('class'))  #bg s_btn
# #打开百度的网址，获取当前页面url和title，来判断百度首页是否打开成功
title = driver.title
url = driver.current_url
# my_cookie = '123456'
# cookie = driver.get_cookie(my_cookie)
# print('cookie为：',cookie)
print("title为：{}".format(title)) #format
print('url为：%s'%(url))
if url == 'https://www.baidu.com/':
    print('打开成功')
else:
    print('打开失败')


#获取百度搜索框的坐标
#获取百度首页底部的备案信息
#定位到百度搜索按钮，并获取这个标签的其他属性值
#打开百度的网址，获取当前页面url和title，来判断百度首页是否打开成功
#获取百度一下按钮的文本值

#text属性--》只能是a、div、p、textarea中间的文本值
# ele = driver.find_element('id','su')
# print('百度一下的text值：',ele.get_attribute('value'))
# driver.quit()

# text = driver.find_element('id','su').text
# print(text)

driver.quit()
