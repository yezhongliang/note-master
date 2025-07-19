# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 23:39
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""frame切换
假设网站是一栋房子，那么iframe则是房子中的某一个房间，我现在要从房间里面拿东西，
必须要进入到这个房间里面，才能拿想要拿的东西。拿完东西需要离开房间
iframe框可以从tag标签看到

进入iframe框:switch_to_frame(iframe元素)或者switch_to.frame(iframe元素)-推荐
退出iframe框：switch_to_default_content()

定位不到元素的原因：
1.在一个frame框里面
2.你用的定位方式的是变化的（变化的id）--结合时间戳
3.有可能有弹窗遮挡没有留意到-广告
4.没有切换窗口
5.元素没有加载完成就去定位--网络原因
6.想要定位的元素它是在下面，需要懒加载的方式
7.想要定位的元素是不可见的，需要用js把它设置为可见再去定位
8.人为原因，代码写错了

百度一下：



"""
#以网易邮箱为例，输入账号和密码登录，登录163邮箱 https://mail.163.com
from selenium import  webdriver
from time import  sleep,time

driver = webdriver.Chrome()
driver.get('https://mail.163.com')
driver.maximize_window()

# #复制到的是一个变化的id，注意注意，变化的id定位是不能够使用，会报错，定位不到这个元素
# #根据tag name 定位，多个，根据索引取到第几个,frame-ele是一个列表的数据类型,取值可以根据索引位来取值
# frame_ele = driver.find_elements('tag name','iframe')[0]
# print(type(frame_ele))
# print('iframe框的数量：',frame_ele)
# #核心步骤，就是这个，进入到iframe框里面去
# driver.switch_to.frame(frame_ele)
#
# driver.find_element('name','email').send_keys('gshunxian@163.com')
# sleep(2)
# driver.find_element('name','password').send_keys('822703304Gsx')
# sleep(2)
# driver.find_element('id','dologin').click()
# sleep(10)
# driver.quit()

#实例化一个对象：用来接受登录界面的所有frame框
ele_frame = driver.find_elements('tag name','iframe')
driver.switch_to.frame(ele_frame[0])

#再去输入定位账号输入框和密码输入框再进行send_keys的操作
driver.find_element('name','email').send_keys('账号')
sleep(1)
driver.find_element('name','password').send_keys('密码')
sleep(10)





