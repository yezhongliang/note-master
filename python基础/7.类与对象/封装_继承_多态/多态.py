# -*- coding: utf-8 -*-
"""
@Time    :2022/8/14 19:53
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""多态
多态是以继承和重写父类方法为前提，对所有子类实例化产生的对象调用相同的方法，执行产生不同的执行结果
一个对象的属性和行为不是由他所继承的父类决定的，而是由其本身包含的属性和方法决定的
重写：父类的方法不满足实际需要的，需要重新写。
重写的位置是子类里面
"""
import unittest
class Father():
    def A(self):
        print('AAAAAA')
    def B(self):
        print('BBBBBB')

class Son(Father):
    def C(self):
        print('CCCCCCC')

    def A(self):  #这个操作就叫重写
        print('AAAAAAAAAAAAAAAAAAAAAAAAA')

son = Son()
son.A()

fa = Father()
fa.A()


# # 面试题：
# # python：
# 1.重载和重写的区别？
# 2.init和new的区别？
# 3.is 和 == 的区别？
# 4.深拷贝与浅拷贝的区别？
# 5.迭代器和生成器的区别？
# 6.装饰器的原理
# 7.python的基本数据类型有哪些？
# 8.list和dict的区别？
# 9.list和tuple 的区别？
# 10.基本数据类型的增删改查

