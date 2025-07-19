# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 20:39
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""三种等待方式
    1.强制等待：time.sleep()
        强制等待并不能一定能把想要定位的元素加载出来，有可能受到网络的影响，
        或者加载的元素太大了，2.用例执行的三种方式 3秒内加载完成不了，导致报错找不到元素，
        使用场景：用于调试和学习---》浪费的时间比较多
        例子，sleep(5),实际上元素在0.5秒里面已经加载完成了，那就浪费了4.5秒了
        
    2.隐式等待:implicitly_wait(x)，不用导包
        在x秒内，等到整个页面都加载完成，再进行下一步操作；
        如果在x秒内还有一些元素没有加载完成，也会进行下一步操作，但是还是有可能存在有一些元素没有加载完成；
        隐式等待对于整个driver的周期都起作用，所以只需要设置一次即可。
        浪费的时间相对强制等待来说少了一些。
        例子，
    3.显式等待:
"""

from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://www.nvidia.cn/')

#10秒的意思是，在这10秒里面，希望把当前页面的所有元素都加载完，再去进行其他的操作
#这里的10 是不会一直等待10秒的，只要页面的元素都加载完成后就会立刻执行其他操作了
driver.implicitly_wait(10)

print(driver.current_window_handle)


