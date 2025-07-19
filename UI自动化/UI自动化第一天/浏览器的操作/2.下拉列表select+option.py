# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 12:01
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""


"""select+option--下拉框
操作步骤
1.导包 from selenium.webdriver.support.ui import Select
2.定位Select元素
3.定位option选项：通过调用Select的方法来进行定位选项：
    方式1：select_by_value，
    方式2：select_by_index， 这一种是根据索引位的方式来定位的，索引位从0开始
    方式3：select_by_visible
"""
#导包
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import  sleep

#实例化一个对象
driver = webdriver.Chrome()
#打开网址：http://127.0.0.1:5000/signin
driver.get('http://127.0.0.1:5000/signin')
#窗口最大化
driver.maximize_window()
#输入用户名以及密码 15902127953  123456,通过xpath定位
driver.find_element('name','username').send_keys('15521048080')
sleep(2)
driver.find_element('name','password').send_keys('123456')
sleep(2)
#点击登录
driver.find_element('xpath','/html/body/form/p[3]/button').click()
sleep(3)

#定位select菜单
ele = driver.find_element('id','Selector')
#实例化Select类的对象,select_obj====下拉的所有选项，使用到刚入的哪个Select类
select_obj = Select(ele)
#可以选择option框里面的内容的，可以根据value/index/visible_text
# select_obj.select_by_visible_text('芒果')
# sleep(2)
select_obj.select_by_index(5)  #索引，从0开始,用正向来取
sleep(3)
# select_obj.select_by_visible_text('芒果')
sleep(5)
# driver.quit()

