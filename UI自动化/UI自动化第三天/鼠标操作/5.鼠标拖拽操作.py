"""
"""
"""拖拽操作,拖拽到某个元素然后松开
用到的方法：action.drag_and_drop(ele_locator1, ele_locator2).perform()
步骤：
1.导包
    from selenium.webdriver.common.action_chains import ActionChains as AC
2.实例对象
    action=AC(driver)
3.调用方法
    action.drag_and_drop(ele_locator1, ele_locator2)
4.统一发送
    action.perform()

"""

from selenium.webdriver import ActionChains as AC
from selenium import webdriver
from time import sleep

#实例化一个对象driver
driver = webdriver.Chrome()

#driver打开wetest
driver.get('http://127.0.0.1:5000/')

#driver点击登录按钮，跳转到登录页面
driver.find_element('xpath','/html/body/a').click()

#点击练习鼠标拖拽
driver.find_element('xpath','/html/body/div/div[1]/a').click()

#实例化一个对象action
action = AC(driver)

#action对象去调用拖拽方法
source = driver.find_element('xpath','//*[@id="dragger"]')
target = driver.find_element('xpath','/html/body/div[2]')
action.drag_and_drop(source=source,target=target)


#把集聚操作统一请求出去
action.perform()

#睡眠 2秒
sleep(2)


# 任务：把webtest的拖拽，全部操作完，把四个空格都填满，然后进行截图操作





