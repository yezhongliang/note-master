# -*- coding: utf-8 -*-
"""
@Time    :2022/8/14 19:20
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
公有实例方法：People里面的eat、drink、play_lanqiu 都是公有实例方法
在类里面和类外面都能被调用

实例方法包含共有实例方法以及私有实例方法
公有实例方法：不以两个下划线开头的，都是公有实例方法
私有实例方法：以两个下划线开头的，都是私有实例方法

类属性（类变量）
    按位置来区分：类属性放在构造方法上面
    公有：不以双下划线开头的
    私有：以双下划线开头的
实例属性（实例变量）
    按位置来区分：实例属性放在构造方法里面
    公有：不以双下划线开头的
    私有：以双下划线开头的
    
公有类属性、私有类属性
公有实例属性、私有实例属性

公有实例方法、私有实例方法

"""

# class People():  #People类，类名首字母大写开头
#     classname = '人的类'  #公有类属性
#     __classage = '几百万年' #私有类属性
#
#     def __init__(self,name,age='60+',sex='男',job='董事长',hobby='唱歌'): #构造方法
#         self.name = name  # 公有实例属性
#         self.age = age    #公有实例属性
#         self.sex = sex    #公有实例属性
#         self.job = job    #公有实例属性
#         self.__aihao = hobby  #私有实例属性
#
#     def eat(self):  #公有实例方法
#         print(self.name+'会干饭')
#
#     def drink(self):  #公有实例方法
#         print(self.name+'会喝奶茶')
#
#     def play_lanqiu(self):  #公有实例方法
#         print(self.name+'会打篮球')
#
#     def __money(self):   #私有实例方法
#         print(self.name + '有1亿')
#
#     def get_classage(self): #公有实例方法
#         return self.__classage #有返回值要用变量接收
#
#     def get_aihao(self): #公有实例方法
#         return self.__aihao
#
#     def get_money(self):
#         return  self.__money()

#实例化一个对象 zeman


#调用公有类属性


#调用私有类属性,不能够直接调用，只能通过公有实例方法间接调用


#调用公有实例属性  对象.公有实例属性


#调用私有实例属性 ,间接调用



#调用公有实例方法  对象.公有实例方法


#调用私有实例方法  对象.私有实例方法-报错,只能间接调用

class People():    #这是类名，People类
    classname = '人的类'   #类属性  共有类属性
    __classage = '几百万年'   #类属性 私有类属性

    def __init__(self,name,age='60+',sex='男',job='董事长',hobby='唱歌'): #构造方法
        self.name = name    #实例属性  公有实例属性
        self.age = age      #实例属性  公有实例属性
        self.sex = sex      #实例属性  公有实例属性
        self.job = job      #实例属性  公有实例属性
        self.__aihao = hobby    #实例属性  私有实例属性

    def eat(self):  #公有实例方法
        print(self.name+'会干饭')

    def drink(self):
        print(self.name+'会喝奶茶')

    def play_lanqiu(self):
        print(self.name+'会打篮球')

    def __money(self):    #私有实例方法
        print(self.name + '有1亿')

    def get_classage(self):  #公有实例方法
        return self.__classage

    def get_aihao(self):    #公有实例方法
        return self.__aihao

    def get_money(self):
        return  self.__money()


