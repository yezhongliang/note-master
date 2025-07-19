# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 23:17
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""多窗口切换
1.获取当前窗口句柄：driver.current_window_handle   current的翻译是当前的意思
2.获取整个driver的所有句柄：driver.window_handles，是有返回值的，这个返回值是一个list
3.切换句柄：driver.switch_to.window(句柄号)  句柄号：handles[-1]也可正向取值
4.返回的所有句柄存在一个列表中，可以用列表的取值拿到最新的窗口handles[-1]
"""
from selenium import  webdriver
from time import  sleep
#
# #实例化一个driver对象用于操作浏览器
#
#
# #窗口最大化
#
#
# #打开百度
#
#
# #通过link text的方式点击hao123
#
#
#
#
# # handle_1 = driver.current_window_handle
# # print('当前的句柄为：',handle_1)
#
# #进行窗口的切换，通过获取所有的句柄号来进行切换
# # handles = driver.window_handles
# # print('所有的句柄为：',handles)
# # print('句柄数量为：',len(handles))
# # print('handles的数据类型为：{}'.format(type(handles)))
# sleep(2)
# #实际进行切换的操作
#  #反向取法
#  #正向取法   ！！！
#
# # print("切换后的句柄为：",driver.current_window_handle)
#
# sleep(2)
#
# #点击地图
#
# #退出整个driver
#
#
#
# # 任务：打开百度，点击hao123，然后在hao123页面点击58同城，然后回到最左边的窗口，
# # 然后在百度输入框输入 疯狂星期四并且点击


#操作：打开百度页面，然后点击hao123网站，然后不进行句柄的切换，然后直接定位hao123网站的元素
# d = webdriver.Chrome()
# d.get('http://www.baidu.com')
# d.maximize_window()
# sleep(1)
# d.find_element('link text','hao123').click()
#
# d.find_element('xpath','//*[@id="govsite-top"]/a[2]').click()
# sleep(5)

#操作：打开百度页面，然后点击hao123网站，然后进行句柄的切换，然后直接定位hao123网站的元素
d = webdriver.Chrome()
d.get('http://www.baidu.com')
d.maximize_window()
sleep(1)
print("当前的句柄号为：{}".format(d.current_window_handle))
d.find_element('link text','hao123').click()
sleep(1)

print("当前的句柄好为：{}".format(d.current_window_handle))

#进行窗口的切换，如果你想要切换窗口，那么先要获取句柄，根据句柄来进行切换
all_handles = d.window_handles
print("所有的句柄有：{}".format(all_handles))
print("返回的句柄的数据类型是：{}".format(type(all_handles)))

#进行句柄的切换，-1永远是最新的窗口
# d.switch_to.window(all_handles[-1]) #反向
# d.switch_to.window(all_handles[len(all_handles)-1]) #正向
d.switch_to.window(all_handles[-1])

#切换后的句柄
print("切换之后的句柄为：{}".format(d.current_window_handle))


# d.find_element('xpath','//*[@id="govsite-top"]/a[2]').click()
d.find_element_by_xpath('//*[@id="govsite-top"]/a[2]').click()
sleep(5)

