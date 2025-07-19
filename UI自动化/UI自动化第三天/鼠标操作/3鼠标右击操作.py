""""""
"""鼠标右击操作
1.导包
    from selenium.webdriver.common.action_chains import ActionChains as AC
2.实例对象
    action=AC(driver)
3.调用方法
    AC(driver).context_click(ele)
4.统一发送
    action.perform()
    
实际上在调用 Actionchains 类的方法时，不会立即执行鼠标操作，
而是会将所有的操作按顺序存放在一个队列里，
最终调用 perform() 方法时，队列中的操作会依次进行
"""
import time

from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC


driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

driver.implicitly_wait(10)

driver.maximize_window()

action = AC(driver)

element = driver.find_element('id','kw')
action.context_click(element)

action.perform()

time.sleep(3)




