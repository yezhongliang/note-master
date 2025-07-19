# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 20:50
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""显式等待：
对指定元素进行等待的一种方式。通过设置最大等待时间、检查频率对页面的元素进行等待，
一旦找到元素，则停止等待，进入后续步骤。
通俗意思：程序每隔x秒看一眼，如果条件成立了（找到这个元素），则执行下一步操作，否则继续等待，
直到超过设置的最长时间，然后抛出TimeoutException异常。

优点：三种等待方式里面最节约时间的，可以提到脚本执行的效率（提高时间的利用率，减少时间的浪费）
缺点：使用起来有点复杂，每一次强制等待只执行一次，如果有多个元素等待，就需要写多次
"""

"""操作步骤：
1.导包：from selenium.webdriver.support.wait import WebDriverWait
2.对WebDriverWait这个类进行实例对象操作
WebDriverWait(driver,timeout,poll_frequency=0.5,ignore_exceptions=None)
driver:浏览器驱动
timeout：最大等待时间 10,就在这10秒里面等待，如果等不到想要的元素，则会抛出超时异常
poll_frequency：检测的间隔时间，默认0.5，可修改
ignore_exceptions：超时后的异常信息，默认抛出NoSuchElementException

调用方法：wait.until()
          wait.until_not()
显式等待是只对一个元素进行监控（监控的是大元素），不会像隐式等待那样等整个页面的元素加载完成
"""
from selenium.webdriver.support.wait import WebDriverWait
from  selenium import  webdriver
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
# driver.find_element('id','kw').send_keys('test')
# driver.find_element('id','su').click()
#显式等待 until的翻译就是直到什么什么
# WebDriverWait(driver,timeout=20,poll_frequency=0.1).until('里面填的是判断') #__init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
#再进行下一步的操作
#下面这行代码就是对百度输入框的监控，监控它是否显示OK，10秒，检测的频率是0.3秒
WebDriverWait(driver,timeout=10,poll_frequency=0.1).until(EC.presence_of_element_located((By.ID,"kw")))
driver.find_element('id',"kw").send_keys("python")
# driver.find_element('xpath','//*[@id="2./h3/a')


























