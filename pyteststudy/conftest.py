# -*- coding: utf-8 -*-
"""
@Time    :2022/10/28 18:17
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""conftest.py 配置里可以实现数据共享，比如py跨文件共享前置  conftest.py配置脚本名称是固定的，不能改名称
不需要import导入 conftest.py，pytest用例会自动查找

背景：
fixture为session级别是可以跨.py模块调用的，也就是当我们有多个.py文件的用例的时候，如果多个用例 只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里。

conftest.py文件名称时固定的，pytest会自动识别该文件。
放到项目的根目录下就可以全局调用了，如果放到某个package下，那就在改package内有效。

通常在conftest里面写工厂函数，这里的工厂函数指的是fixture

pytest运行的先后顺序：
如果有conftest会先执行conftest里面的代码（数据共享、操作共享）,再去其他模块执行其他代码
"""

import pytest
from selenium import  webdriver

# @pytest.fixture(scope='function')
# def function_fixtrue():
#     print('方法级别的fixture,也是默认级别')
#     print('=======================')
#
#
# @pytest.fixture(scope='class')
# def class_fixtrue():
#     print('类级别的fixture')
#     print('========================')
#
# @pytest.fixture(scope='module')
# def module_fixtrue():
#     print('模块级别的fixture')
#
#
# #作为前置来使用
# @pytest.fixture()
# def Kaishi():
#     print('开始了，进行环境初始化')
#
# #作为后置来使用
# @pytest.fixture(scope='function')
# def Jieshu():
#     print('结束了，进行资源的回收')
#
#

@pytest.fixture(scope='module',autouse=True)
def Kaishi():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.maximize_window()

@pytest.fixture(scope='function')
def Jieshu():
    print('环境回收')
