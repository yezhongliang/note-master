# -*- coding: utf-8 -*-
"""
@Time    :2022/8/19 20:19
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""三种等待方式，前提：在网络环境不好下进行UI自动化。
    1.强制等待：time.sleep()
        强制等待并不能一定能把想要定位的元素加载出来，有可能受到网络的影响，
        或者加载的元素太大了，x秒内加载完成不了，导致报错找不到元素，
        使用场景：用于调试脚本和学习---》浪费的时间比较多
    2.隐式等待:implicitly_wait(x)--不需要导包
        在x秒内，整个页面都加载完成，再进行下一步操作；
        如果在x秒内还有一些元素没有加载完成，也会进行下一步操作，所有还是有可能存在有一些元素定位不到；
        隐式等待对于整个driver的周期都起作用，所以只需要设置一次即可。
        而且一般设置在打开浏览器之后
        浪费的时间相对强制等待来说少了一些。
    3.显式等待:略

为什么说强制等待浪费的是时间是最多的？
现在有一个元素，加载需要2秒
1.我们用强制等待，等待3秒，3-2=1s，这里就浪费了一秒
2.我们用隐式等待，implicitly_wait(3)，在3秒内一直检测，只要页面的所有元素都加载成功，
就会执行下面的另外步骤，那这里不浪费时间
3.我们用显式等待，这是最好的方法，也是浪费时间最少的，但是实现较复杂
4.隐式等待和显式等待都称为智能等待
"""

from selenium import  webdriver
from time import  sleep

driver = webdriver.Chrome()

driver.get('https://www.nvidia.cn/')

