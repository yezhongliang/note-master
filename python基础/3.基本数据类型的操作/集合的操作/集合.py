# -*- coding: utf-8 -*-
"""
@Time    :2022/8/9 15:05
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
集合一般用于数组的去重
集合是无序的，不能通过索引位的方式去删除，也不能通过索引位的方式去查
"""
# set_01=set()
# set_02={}
# print(type(set_01))  #<class 'set'>
# print(type(set_02))  #<class 'dict'>
#
# set_03={'we','dvw','we',34,34,4,65,75,4}
# print(set_03,type(set_03)) #{65, 34, 'we', 4, 75, 'dvw'} <class 'set'>

#集合也可以对列表进行去重,思路：先把列表转换集合，然后再转换成为列表即可
# list1 = [1,2,2,3,3,4,4,5]
# a = set(list1)
# print(a,type(a))
#
# b = list(a)
# print(b,type(b))

#1.add增加元素
# set_04 =set("abcdef")
# set_04.add("z")
# set_04.add('31')
# set_04.add('31')
# print(set_04)

# 2.pop 随机删除
# set_05 =set('hangzhou')
# set_05.pop()
# print(set_05)

