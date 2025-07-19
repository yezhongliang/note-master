# -*- coding: utf-8 -*-
"""
@Time    :2022/8/9 14:07
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""
其他数据与列表之间的转换---list()
"""
str1 = 'll'
num1 = 100
boo11 = False
float1 = 10.1

#字符串转列表，可以
# print(list(str1),type(list(str1)))   #['a', 'b', 'c'] <class 'list'>
#
# #整形int转列表
# print(list(num1)) #iterable(可迭代的)   TypeError: 'int' object is not iterable

#浮点型float转列表
# print(list(float1))  #TypeError: 'float' object is not iterable

#布尔值bool转列表
#print(list(boo11))   #TypeError: 'bool' object is not iterable