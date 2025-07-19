# -*- coding: utf-8 -*-
"""
@Time    :2022/9/5 22:22
@version :Python3.7.4
@Software:pycharm2020.3.2
"""


"""Appium常用元素定位方法：
id定位   根据元素的resoure-id属性值进行定位
name定位  根据元素的text属性值进行定位  appium1.5之后移除了这种方式
class-name定位 根据元素的class属性值进行定位
accessibility-id定位  根据元素的content-desc属性值进行定位Android专用，IOS没有这个
xpath定位  
    uiautomatorview没有xpath路径，inspector有，可以直接复制
    在appium中使用xpath定位需要自己去写xpath路径
    xpath用法：find_element_by_xpath("//标签名[@属性名称='属性值']")
               find_element_by_xpath("//android.widget.TextView[@text='同意']")
               find_element_by_xpath("//*[@text='电子邮件']")

定位工具：
    uiautomator viewer
    inspector
    
属性操作：
    text属性  ele.text 获取元素的文本值
    location属性 ele.location 获取元素的坐标，以字典存储
    size属性 ele.size 获取元素的大小，以字典存储
    tag_name ele.tag_name 获取元素的标签名（元素class的属性值）
"""
from appium import webdriver
from time import  sleep
des = {
    "deviceName":"127.0.0.1:62001",
    "platformName":"Android",
    "appPackage":"com.ss.android.article.lite",
    "appActivity":"com.ss.android.account.v2.view.AccountLoginActivity",
    "platformVersion":"5.1.1"
    # "noReset":"True"  #是否重置测试环境，可要可不要
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=des)
driver.find_element('id','com.ss.android.article.lite:id/ahx').send_keys('12345678999')
sleep(2)






