# -*- coding: utf-8 -*-
"""
@Time    :2022/8/14 19:20
@version :Python3.7.4
@Software:pycharm2020.3.2
"""


"""讲到Unittest再细讲类方法的作用
类方法以及静态：

@classmethod 和 @staticmethod，这种前面带@符号的，在python里面
成为装饰器。

装饰器的定义以及作用：在不改变原有方法的基础上，给原有方法增加新的功能。这就是装饰器的定义。
装饰器本质上也是一个函数。
装饰器的原理是：闭包。

类中的方法包含：
    实例方法、静态方法、类方法
    实例方法：有self的
    静态方法：需要用staticmethod来装饰，不需要self
    类方法：需要用classmethod来装饰，需要cls、

"""
class Hello():
    @staticmethod
    def func1():
        print('Hello,这是一个静态方法')

    @classmethod
    def func2(cls):
        print('Hello,这是一个类方法')

    def test(self):
        print('1111111111')



