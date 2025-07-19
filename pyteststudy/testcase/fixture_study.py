# -*- coding: utf-8 -*-
"""
@Time    :2022/10/29 14:54
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""fixture称为pytest的夹具
它的作用是类似setup以及teardown，都是作为测试环境的初始化以及测试环境资源的回收来使用的，
而且fixture的使用是配合conftest.py来使用的
源码：fixture(scope="function", params=None, autouse=False, ids=None, name=None)
    scope：被标记方法的作用域
        =function (default)：作用于每个测试方法，每个test都运行一次
        =class：作用于整个类，每个class的所有test只运行一次
        =module：作用于整个模块，每个module的所有test只运行一次
        =session：作用于整个session(慎用)，每个session只运行一次
    params：(list类型)提供参数数据，供调用标记方法的函数使用
    autouse：是否自动运行,默认为False不运行，设置为True自动运行
        自动运行：不用调用，自动运行
        也可以跨文件调用


之前我们学习的：使用一个模块py文件之前，要导包，但是所有定义在conftest.py文件里面的所有函数或者类
都不需要导包，直接继承或者调用即可
"""
import pytest
from selenium import  webdriver
from time import  sleep

def test_1(Kaishi,driver):
    driver.find_element('id','kw').send_keys('666')
    sleep(1)
    driver.find_element('id','su').click()


if __name__ == '__main__':
    pytest.main()
