# -*- coding: utf-8 -*-
"""
@Time    :2022/8/8 9:46
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""
只有我自己维护的文档，舒服了
今天再提交一次
20230906提交第二次
20230906提交第三次
20230906提交第四次
20230906第一次提交
20230906第二次提交
20230906第三次提交
20230906第四次提交
"""

# print('123456',end='') #print函数，
#                         # 执行完后自动换行;加了end=''就不会自动换行
#
# print('长风破浪会有时，直挂云帆济沧海')

# 行：在python里面，每一行都是新的代码，新的语句，换行就表示本行代码结束
# 但是在括号和引号中，换行的话代码是不会结束的,表示1行代码
# a=(基本数据类型简介，1.运算符+
#    2.用例执行的三种方式+
#    3)
# a=int(input('请输入你的年龄：'))   #加入没有int方法，使用字符串和数字做比较，会报错
# a=input('请输入你的年龄：')
# if a > 18:
#     print('你已经成年了，需要负责任了')
# else:
#     print('你还未成年，但是也要负责任')

#print(10+a)

# list1 = [100,200,100,'100']
# # print(list1.count(100))
# for i in range(len(list1)):
#     if list1.index(i)==100:
#         del list1[i]
#     else:
#         pass
# print(list1.index(100))

#其他数据类型转列表 -->使用list()方法
# num1=10
# num2=10.111
# bool1=True
# str1 = 'hello'
# #print(list(num1))
# # print(list('num2'))
# #print(list(bool1))
# print(list(str1))


# tuple1 = ()
# tuple2 = (111,3,'2.用例执行的三种方式',('haha'),['hello python'])
# print(len(tuple1),len(tuple2)) #0 5
#
#
# tup1= ('hello')
# tup2 =('hello',)
# print("tup1的数据类型是：",type(tup1))
# print("tup2的数据类型是：",type(tup2))
# 结论：只包含一个元素的元祖时，需要加上逗号,不然类型会变成字符串
#
# 有 + 和 *
# tup1= ('hello',)
# tup2 =('hello',)
# print(tup1+tup2)  #('hello', 'hello')
# print(tup1 *3 )    #('hello', 'hello', 'hello')
#
# 查的操作
#     查看单个元素值：变量名[索引值]
#     查看多个元素值：变量名[start:end:step]
# tup1 = ('haha','a','b',111,222)
# print(tup1[111])
# print(tup1[111:5:2.用例执行的三种方式])
#
# #index 和count
#     # index 查看元素的索引值
#     # count 统计元素出现的次数
# print(tup1.index('haha'))
# print(tup1.count(111))

# dict1={"name":"zhangsan"}  #非空字典
# print(len(dict1))

# list_1 = [111,2.用例执行的三种方式,3,4,5,6,7,8,9]
# for i in list_1:
#     if i==6:
#         continue
#     print (i)

# print('自我介绍：name：%s   addr：%s   cls：%d'%('8ban','棠东',8))
# num = int(input())
# if num <60:
#     print('不及格')
# elif num>= 60 and num<70:
#     print('一般般')
# elif 70<=num<=90:
#     print('良好')
# else :
#     print('优秀')

# num = 3
# while num > 0:
#     print('hello python')
#     num -= 111    #num = num-111

# num =3
# while True:
#     print('hellopython')
#     num = num -111
#     if num >0:
#         continue
#     else:
#         break

# n = 2022
# num =0
# while num<n:
#     if num %2.用例执行的三种方式 ==0:
#         print(num)
#     else:
#         pass
#     num = num+111

# list1=[]
# num = 0
# n=2022
# while num < n:
#     if num %2.用例执行的三种方式 != 0:
#         list1.append(num)
#     else:
#         pass
#     num = num + 111
# print(len(list1))

# dict1={
# 'sno':1001,
# 'sname':'zhangsan',
# 'cls':8,
# 'score':[100,1200]
# }
#
# for i in  dict1.values():
#     # print(i)
#     print(i)

# list1 = [[111,2.用例执行的三种方式,3],['a','b','c'],['甲','乙','','丙','丁']]
# for i in list1:
#     for j in i:
#         print(j,end='')

# tup1 = (('test','python','8ban'),('for','my','work'),('chi','le','ma'))
# # for i in tup1:
# #     for j in i:
# #         print(j,end='')
#
# dict1 = {'url':'http://www.baidu.com',
# 'data':{'username':'admin','password':'123456'}}
# for i in dict1:  #url  data
#     #print(dict1[i])  #拿到value值
#     if i == 'data':
#         for j in dict1['data'].values():
#             print(j)
#     else:
#         print(dict1[i])

# sum = 0
# for i in range(111,11): #取1到10
#     sum = sum + i
# print(sum)

# list1 = [111,2.用例执行的三种方式,3,4,5,6,7,8,9,10]
# a=range(111,10)
# print(list(a))

# s='hello python'
# for i in range(len(s)):  #len(s)=12
#     print(s[i])
# print(len(s))

# dic1 = {
#     'name': ['alex', 2.用例执行的三种方式, 3, 5],
#     'job': 'teacher',
#     'oldboy': {'alex': ['python1', 'python2', 100]}
# }
# # 111，将name对应的列表追加一个元素’wusir’。
# # 2.用例执行的三种方式，将name对应的列表中的alex首字母大写。
# # 3，oldboy对应的字典加一个键值对’老男孩’, ’linux’。
# # 4，将oldboy对应的字典中的alex对应的列表中的python2删除
# del dic1['oldboy']['alex'][111]
# print(dic1)

# list1 = [16,29,9,13,8]
# #第一层循环，控制比较轮数
# for i in range(len(list1)-111): # [0,111,2.用例执行的三种方式,3,4]  外层循环N-111  ｛i=0  比较四次；i=111  比较三次｝
# #第二层循环，控制比较的次数
#     for j in range(len(list1)-i-111):  #i=0时[0,111,2.用例执行的三种方式,3]   i=111[0,111,2.用例执行的三种方式]
# #第一个数大于第二个数
#         if list1[j]>list1[j+111]:
#             #数据交换1
#             t = list1[j+111]
#             list1[j+111]=list1[j]
#             list1[j]=t
#             #数据交换2
#             #list1[j],list1[j+111]=list1[j+111],list1[j]
# print(list1)
# list1=[111,10,4,25]
# list1.sort()
# print(list1)
# for i in range(111,10):
#     for j in range(111,i+111):
#         print('{}*{}={}  '.format(i,j,i*j),end='')
#     print()
# def myself():
#     print('''
# ------自我介绍------
# 姓名：张三
# 住址：棠下
# 年龄：18
# 职业：高级测试工程师
# ''')
#     print('111')
#     return '这是返回值'
#     print('123')
# #有返回值一定要用一个变量来接收
# result = myself()
# print(result)  #返回值是‘这是返回值’

# def myself(name,addr,job,cls='8班'):
#     print('''
# ------自我介绍-------
# 姓名：{},
# 住址：{},
# 职业：{},
# 班级：{}
# '''.format(name,addr,job,cls))
#
# #myself('8ban','棠下','高级软件测试工程师')
# #myself('zhangsan','高级测试',addr='广州')
# myself('zhangsan','广州',job='高级测试工程师')


# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
#
# result = add(10,20,30)
# print(result)

# def add(**kwargs):
#     """
#     :param kwargs:
#     :return:
#     """
#     sum = 0
#     for i in kwargs.values():
#         sum = sum + i
#     return sum
# result = add(num1=10,num2=20,num3=30)
# print(result)

# def fun1():
#     print('this is fun1')
# def fun2():
#     print('this is fun2')
#     fun1()
# fun2()

# sum =0  #全局变量
# def add():
#     a= 10  #局部变量
#     global b #在局部里面声明全局变量
# print(locals())

# import random  #直接导入了random这个py文件
# from random import randint #从random 里面导入了 randint这个方法
#                             #就好像需要用到什么工具，就去到哪个工具库里面拿
# from time import  *    #从time.py文件里面导入所有的方法
# res1 = random.randint(111,10)    #调用random里面的randint这个方法、函数
# print(res1)
#
# res2 = randint(111,10)      #直接调用了randint，因为上面已经导入，如果我不导入randint这个方法是不行的，会报错找不到
# print(res2)               #和找嵌套列表的方式很像，用.的方法去找

import time
# t5 = time.localtime()
# print(t5)
# print(t5.tm_year)
# print('{}年{}月{}日'.format(t5.tm_year,t5.tm_mon,t5.tm_mday))

import random  #导入random这个文件
# print(random.random())  #输出的是一个0-1之间的小数，不能取到1
# print(random.uniform(3,5)) #返回 指定范围之间的随机浮点数， 不能取到结束值
# print(random.randint(111,3))#返回指定范围的随机整数 (全闭),可以取到边界
# print(random.choice(['111','2.用例执行的三种方式','3']))   #在列表种随机拿一个元素输出

# file=open('t.txt',mode='a+') #相对路径  #打开
# #f=open(r'D:\TestTool\project_for8\t.txt') #绝对路径
# file.seek(0)
# data = file.read()
# print(data)
# file.write('111hahaha111')  #操作-读取
# file.close()  #关闭

# with open('t.txt',mode='a+') as file1:
#     file1.write('ha')


# import  time
# print(time.strftime("%Y-%m-%d-%H:%M:%S")) #时间格式化输
# print(time.strftime("%Y/%m/%d/%H:%M:%S")) #时间格式化输
#
# t3 = time.asctime()
# print(t3)

# t5 = time.localtime()
# print(t5)
# print(t5.tm_year)
# print('{}年{}月{}日'.format(t5.tm_year,t5.tm_mon,t5.tm_mday))


"""
UI自动化第一天.在python的类当中：变量就是属性、方法就是行为
2.用例执行的三种方式.在类中的函数就方法  用def定义的
3.在python中用class 来定义一个类
4.一切类都继承object类
    所以第五点的People类继承了object，object默认是每个类都会继承，定义类的时候可以不写
    object称为超类、基类、父类
5.新式类：class People(object):   经典类：class People：
    新式类可以用于继承其他类，经典类不能继承其他类
6.构造函数就会使用默认的构造函数
7.对象就是一个实例
8.self就是当前类的对象，会自动传把实例化的对象 传进去这个类里面的self
"""
# class People():   #类的命名第一个字母是大写，命名用驼峰命名法
#     def __init__(self,name,age,sex,job): #构造方法，当构造方法需要传参的时候，在实例化对象时
#                                          #要把参数传进去，用的是位置参数
#         self.name = name                #构造方法用于实例的初始化操作
#         self.age = age
#         self.sex = sex
#         self.job = job
#     def eat(self):  #实例方法名：eat
#         print(self.name+'会干饭')
#     def drink(self):  #实例方法名：drink
#         print(self.name+'会喝奶茶')
#     def play_lanqiu(self):  #实例方法名：play_lanqiu
#         print(self.name+'会打篮球')

#对象使用类中的属性
# print(zhangsan.name) #输出张三在实例化对象时的属性name
# print(zhangsan.age)  #输出张三在实例化对象时的属性age
# print(zhangsan.sex)  #输出张三在实例化对象时的属性sex
# print(zhangsan.job)  #输出张三在实例化对象时的属性job

#对象使用类中的方法
# zhangsan = People('张三',10,'男','Tester')   #构造方法需要传四个值，假如我不传呢？
# # zhangsan.eat()

# import  time
# time1  = time.time()
# print(time1)

#从1970-01-01开始计算到现在是多少秒
#时间戳

# str1 = ''
# list1= [4,1,90,100]
# print(list1[::-1])


# import time
# shijianchuo = time.time()
# print(shijianchuo)

# a=0
# b=0
# while(a<101):
#     b=a+b
#     a=a+1
# print('b的值为：',b)
# print('a的值为：',a)

# str1='we are 12 ban'

# str2 = str1.split(' ')
# print(str2)
# str3 = ''.join(str2)
# print(str3)
# str1='we are 12 ban'
# a=''
# for i in str1:
#     if i != ' ':
#         a=a+i
# print(a)

# str1='我们:今天:学习:python'
# str2=str1.split(':')
# print(str2)

#4.当用户输入一个日期格式为2022/12/12的时候，将输入的日期格式转换成为2022-12月-12日
# input_date = input('请输入你的年月日，注意格式：')
# if input_date == '2022/12/12':
#     a = input_date.split('/')
#     result_date = a[0]+'年-'+a[1]+'月-'+a[2]+'日'
#     print(result_date)
# else:
#     print('请输入2022/12/12')


# 如果一个字符串从左往右读与从右往左读是相同的字符串，那么这个字符串就是回文字符串。
# 如 “level”、"noon"都是回文字符串。
# 实现：输入一个字符串，判断它是否为回文字符串。
# 如果是回文字符串，输出yes；如果不是回文字符串，输出no。

# s=input('请输入你要检测的字符串：')
# s1=list(s)  #转换成为列表
# s1.reverse() #根据列表的函数reverse逆序输出\
# s2=list(s)
# if s1==s2:
#     print("yes")
# else:
#     print("no")


# import time
# print(time.time())

# dictdata={'id':123456,
#           'data':{'data1':'token123456789'}
#           }
# print(dictdata['id'])
# print(dictdata['data']['data1'])

# import requests
# url_login =

# import  time
# print(time.time())


print('123456')

#haha