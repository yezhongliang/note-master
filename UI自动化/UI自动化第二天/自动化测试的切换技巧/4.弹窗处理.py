# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 23:38
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""切换操作：
switch_to.alert
switch_to.window
switch_to.frame
"""

"""alert弹窗-确认型弹窗"""
from selenium import  webdriver
from time import  sleep

# driver = webdriver.Chrome()
# driver.get('http://127.0.0.1:5000/signin')  #登录页面
# driver.maximize_window()
# sleep(2)
# #输入账号-手机号
# driver.find_element('xpath','/html/body/form/p[1]/input').send_keys('15521048080')
# sleep(2)
# #输入密码
# driver.find_element('xpath','/html/body/form/p[2]/input').send_keys('123456')
# sleep(2)
# #点击登录按钮,点击sign in
# driver.find_element('xpath','/html/body/form/p[3]/button').click()
# sleep(2)
# #定位alter弹窗的入口-确认弹窗
# driver.find_element('xpath','//*[@id="testtable"]/tbody/tr[2]/td[2]/input').click()
# sleep(2)
# #点击确认，使用switch_to.alter 去点击确认,34行代码就是关闭的操作
# driver.switch_to.alert.accept() #accept的翻译是接受，确定  dismiss是取消
# sleep(2)



"""confirm-两重弹窗"""
# driver =  webdriver.Chrome()
# driver.get('http://127.0.0.1:5000/signin')
# driver.maximize_window()
# #登录，输入账号和密码
# driver.find_element('xpath','/html/body/form/p[1]/input').send_keys('15521048080')
# sleep(1)
# driver.find_element('xpath','/html/body/form/p[2]/input').send_keys('123456')
# sleep(1)
# #点击登录
# driver.find_element('xpath','/html/body/form/p[3]/button').click()
# sleep(1)
# #点击confirm框
# driver.find_element('xpath','//*[@id="testtable"]/tbody/tr[4]/td[2]/input').click()
#
# sleep(3)
# #进行了确认的操作
# driver.switch_to.alert.accept()
# sleep(5)
# #再进行取消的操作,选择用accept和dimiss取决于第二个弹窗是否有两个选项
# driver.switch_to.alert.dismiss()
# sleep(5)

"""prompt-输入型弹窗"""
driver =  webdriver.Chrome()
driver.get('http://127.0.0.1:5000/signin')
driver.maximize_window()
#登录，输入账号和密码
driver.find_element('xpath','/html/body/form/p[1]/input').send_keys('15521048080')
sleep(1)
driver.find_element('xpath','/html/body/form/p[2]/input').send_keys('123456')
sleep(1)
#点击登录
driver.find_element('xpath','/html/body/form/p[3]/button').click()
sleep(1)
driver.find_element('xpath','//*[@id="testtable"]/tbody/tr[3]/td[2]/input').click()
sleep(2)
# #开始promt的操作了
prompt = driver.switch_to.alert

sleep(2)
prompt.send_keys('哈哈测试一下试试')
sleep(2)
#再点击确认
prompt.accept()
sleep(5)
driver.quit()










