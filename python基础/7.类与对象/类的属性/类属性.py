# -*- coding: utf-8 -*-
"""
@Time    :2022/8/14 17:22
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""类中的属性
类属性：整个类的属性特征
    定义在类中，不是在函数(构造函数)中的属性；
    公有类属性：
        不以两个下划线开头的
        可以在类里面和类外面去使用，子类也可以使用（继承父类的叫子类）
        调用方法：类名.类属性名
    私有类属性：
        以两个下划线开头的
        只可以自己类里面去用，出了这个类就用不了了
          
实例属性：
    实例对象的属性特征，定义在构造方法中的属性
    公有实例属性：
        不已两个下划线开头的,可以在类里面和类外面去使用，子类也可以使用（继承父类的叫子类）
    私有实例属性：
        以两个下划线开头的,只可以自己类里面去用，出了这个类就用不了了

"""

class People():
    # 这两个是类属性
    type = '人类'    #公有类属性
    num=7000000000       #公有类属性
    __phone = 15521048080  #私有类属性，私有的类属性的调用只能通过间接的方法去调用

    def __init__(self,name,age,sex,job):
        #这四个是实例属性,为什么叫实例属性？因为是在实例化对象的时候给的属性，每一个对象的属性都是不一样的
        self.name = name  #公有实例属性,
        self.age = age    #公有实例属性
        self.sex = sex    #公有实例属性
        self.__job = job    #私有实例属性


    def eat(self):  #实例方法名：eat
        print(self.name+'会干饭')

    def drink(self):  #实例方法名：drink
        print(self.name+'会喝奶茶')

    def play_lanqiu(self):  #实例方法名：play_lanqiu
        print(self.name+'会打篮球')

    def get_phone(self): #get是获取的意思，获取phone的方法
        print(self.__phone)

    def get_job(self):
        print(self.__job)

#打印输出People的所有公有类属性：

#打印输出People类的私有类属性：

#打印某个对象所有的公有实例属性

#打印后个对象所有的私有实例属性






#定义一个朋友类
class Friend():
    def __init__(self,shengao,tizhong,aihao,shouru='100W'): #init方法，初始化方法，也叫构造方法，作用是实例化一个对象
                        #的时候，该对象要先调用此方法，相当于一个最前置的方法,
                        #构造方法需要去传参数的时候，必须要在实例化对象这一步把参数传进去

        self.shengao = shengao
        self.tizhong = tizhong
        self.aihao   = aihao
        self.shouru = shouru
    def boy_friend(self):
        print('男朋友的身高：'+self.shengao)

    def girl_friend(self):
        print('这是女朋友方法')

    def normal_friend(self):
        print('这是普通朋友方法')

#实例化一个对象：xiaopeng
# xiaopeng = Friend('185cm','80kg','nv')

# print(xiaopeng.shouru)
# print(xiaopeng.shengao)
# print(xiaopeng.aihao)
# xiaopeng.boy_friend()

#实例化一个对象：fupo
# fupo = Friend('170cm','55KG','nan',shouru='1000W')
# print(fupo.shengao)
