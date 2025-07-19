# -*- coding: utf-8 -*-
"""
@Time    :2022/8/14 17:21
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""
"""
1.在python的类当中：变量就是属性、方法就是行为
2.在类中的函数就是方法  用def定义的
3.在python中用class 来定义一个类
4.一切类都继承object类
    所以第五点的People类继承了object，object默认是每个类都会继承，定义类的时候可以不写
    object称为超类、基类、父类
5.新式类：class People(object):   经典类：class People：
    新式类可以用于继承其他类，经典类不能继承其他类
6.构造函数就会使用默认的构造函数
7.对象就是一个实例
8.self就是当前类的对象，会自动传把实例化的对象 传进去这个类里面的self
9.定义一个类：
    class + 类名():
        def 方法():
            pass
        def 方法():
            pass
对方法的命名，对类的命名，对文件的命名，对模块的命名，对文件夹的命名，对变量的命名
最好都是遵循驼峰式命名法或者下划线命名法
"""
class People():   #类的命名第一个字母是大写，命名用驼峰命名法
    def __init__(self,name,age,sex,job): #构造方法，当构造方法需要传参的时候，在实例化对象时
                                         #要把参数传进去，用的是位置参数
        self.name = name                #作用：构造方法用于实例的初始化操作
                                        #当实例化一个对象的时候，这个对象就会去调用
                                        #init的函数，是自动调用的
        self.age = age
        self.sex = sex
        self.job = job
    def eat(self):  #实例方法名：eat
        print(self.name+'干饭')
    def drink(self):  #实例方法名：drink
        print(self.name+'喝奶茶')
    def play_lanqiu(self):  #实例方法名：play_lanqiu
        print(self.name+'打篮球')

#实例化一个people1的对象,过程
#实例化对象的意思：用一个变量去使用这个类，称为实例化对象
# a = People('damazi',50,'男','测试')

#对象使用类中的属性
# print(a.name)
# print(a.age)
# print(a.job)
# print(a.sex)

#对象使用类中的方法,用法：对象名.方法名即可
# a.drink()
# a.eat()
# a.play_lanqiu()

class CarLei():
    def __init__(self,name,price,color):
        self.xingming = name
        self.jiage    = price
        self.yanse    = color

    def Speed(self):
        print('这个车可以上300公里每小时')
    def Model(self):
        print('车模靠在车旁边')
    def DouFeng(self):
        print('带车模兜风')
    def BiaoChe(self):
        print('狂飙')

#当实例化对象的时候，是否需要传值，要看有没有init函数，如果init函数里面不需要传值
#那么在初始化对象的时候就不需要传值了
#实例化一个对象BMW
# BMW_GLC = CarLei('BMW',400000,'red')
# # print(BMW_GLC.xingming)
# # print(BMW_GLC.jiage)
# # print(BMW_GLC.yanse)
# # BMW_GLC.BiaoChe()



class Games():

    Game_type = '2D游戏'  #类属性，公有的
    Game_company = '腾讯' #类属性，公有的
    __Game_People = '年轻小伙子/女孩子' #类属性 ，私有的

    def __init__(self):  #构造函数
        self.name = '时间消磨品' #公有实例属性
        self.function = '使得心情愉悦' #公有实例属性
        self.__test = 'test一下私有实例属性'

    def Wangzhe(self):    #此方法称为实例方法，公有的
        print('这是王者荣耀游戏')

    def ChiJi(self):      #此方法称为实例方法，公有的
        print('这是刺激战场')

    def DouDiZhu(self):   #此方法称为实例方法，公有的
        print('这是斗地主游戏')

    def __duhai(self):
        print('毒害小伙子')

    def get_Game_People_attribute(self): #间接调用私有类属性
        return self.__Game_People

    def get_duhai(self):
        self.__duhai()

    def get__test(self):
        # return self.__test
        print(self.__test)

#调用类的时候，需要实例化一个对象，或者实例化多个对象
# 实例化对象的操作：  对象名 = 类名(),在实例化对象的时候，需要看有没有构造函数，如果有
#构造函数，要看构造函数里面是否有形参，如果有则需要传值


#现在这个youxi对象已经被这个类实例化了，如果想调用这个类里面的方法，那么只需要用：
# 对象.方法  即可


#调用公有类属性：类名.属性名
print(Games.Game_company)
print(Games.Game_type)

#调用私有类属性，需要写一个公有实例方法去调用私有类属性，间接调用
Game_People =  Games()
res = Game_People.get_Game_People_attribute()
print(res)

#调用公有实例方法
zhangsan = Games()
zhangsan.Wangzhe()

#调用私有实例方法
lisi = Games()
lisi.get_duhai()

#调用公有实例属性，先要实例化对象，再输出这个对象的属性
wangwu = Games()
print(wangwu.function)
print(wangwu.Game_type)

#调用私有实例属性
niuliu = Games()
niuliu.get__test()


# __init__函数和__new__函数的区别是什么？
# # init是在实例化对象之后才去进行的操作，new是在实例化对象之前就去做的操作
# # init函数是构造方法，new函数是静态方法

