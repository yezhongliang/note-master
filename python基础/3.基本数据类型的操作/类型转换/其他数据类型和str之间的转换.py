# -*- coding: utf-8 -*-
"""
@Time    :2022/8/8 14:08
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
其他数据类型转str，需要用到str的方法去转
"""
number1 = 1
number2 = 8.88
number3 = False

# str1 = str(number1)
# print(str1,type(str1))

# input函数：默认传的是字符串
# data = float(input('请输入一个数字：'))
# if data == 100:
#     print('恭喜你，100hun')
# else :
#     print('没有100hun')

#列表转str
# list1 = [100,200,300]
# a = str(list1)
# print(a,type(a))

# str转列表？
# str2 = 'admin 123456'
# b = list(str2)
# print(b,type(b),len(b))
#
# c = str2.split(' ')
# print(c,type(c))

#tuple转str，用到也是str函数
tuple1 = (1,2,3,4,666,777)
str2 = str(tuple1)
print(str2,type(str2),len(str2))   #(1, 2, 3, 4, (666, 777)) <class 'str'> 24
print(str2[2])
















