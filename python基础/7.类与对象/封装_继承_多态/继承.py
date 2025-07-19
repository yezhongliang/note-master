# -*- coding: utf-8 -*-
"""
@Time    :2022/8/14 19:53
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""


"""继承
可以继承多个类:class Son(Father,Grandfater)
可以继承某个类里面的方法：class Son(Father.smoking)
假如需要继承其他库的类，则需要先把库给导进来，import xx
"""
# from 7.类与对象.封装_继承_多态.hahatest import GrandFather

class GrandFather():
    hobby_one = '下象棋'
    hobby_two = '抽烟'
    __age = '99'

    def eat(self):
        print('爷爷爱吃肉')

    def drink(self):
        print('爷爷爱喝酒')

    def __kanmeinv(self):
        print('看美女')

class Mother():
    aihao1 = 'shopping'
    aihao2 = '做菜'
    __aihao3 = '化妆'

    def gym(self):
        print('妈妈喜欢运动')

    def __zhuiju(self):
        print('妈妈喜欢追剧')

class Father(GrandFather):
    aihao11 = '抽烟-抽好烟'
    aihao2 = '打广东麻将'
    __aihao3 = '洗脚'

    def Smoking(self):
        print('爱好抽烟')

    def monkey(self):
        print('贼赚钱')

    def __shuadouyin(self):
        print('喜欢看抖音刷美女视频')

class Son(Father,Mother):
    age = 18
    sex = '1'
    def lanqiu(self):
        print('打篮球是爱好')

    def chang(self):
        print('喜欢唱歌')

    def __rapper(self):
        print('rap了两年半')

    def get_rapper(self):
        self.__rapper()

#实例化一个father类
father = Father()

#father对象去调用Father类里面的公有实例方法
father.drink()


#实例化一个son对象
son = Son()
#son对象去调用Grandfather类里面的公有实例方法
son.eat()
#son类去调用Grandfather类里面的公有类属性
print(son.hobby_one)

#son对象调用Son类里面的私有实例方法
son.get_rapper()











