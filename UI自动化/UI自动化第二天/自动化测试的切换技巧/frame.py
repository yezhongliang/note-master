"""
"""
"""163邮箱登录"""

from selenium import webdriver
from time import  sleep

d = webdriver.Chrome()

d.get('https://mail.163.com/')

d.maximize_window()

sleep(2)
#获取所有的frame框：
all_frame = d.find_elements('tag name','iframe')
print(all_frame)
print(type(all_frame)) #all_frame[0]

#切换进去frame框里面
d.switch_to.frame(all_frame[0])

d.find_element('xpath','//*[@name="email"]').send_keys('1234567')
sleep(2)

d.find_element('name','password').send_keys('11111111')
sleep(5)

