# -*- coding: utf-8 -*-
"""
@Time    :2022/8/14 19:20
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""
"""
私有实例方法：People里面的__siyou方法是私有实例方法，
只能在类里面被调用，在类外面不能被调用
私有方法用于安全性的考虑
"""

class People():
    def __init__(self):
        pass

    def eat(self):  # 实例方法名：eat
        print('会干饭')

    def __siyou(self):
        print('这是私有有方法，类外面不能被调用，类里面可以被调用')

    def get_siyou(self):  # 实例方法名：drink
        print('会喝奶茶')
        self.__siyou()

    def play_lanqiu(self):  # 实例方法名：play_lanqiu
        print('会打篮球')

#验证私有实例方法不能在类外面被调用


#验证私有实例方法能在类里面被调用


