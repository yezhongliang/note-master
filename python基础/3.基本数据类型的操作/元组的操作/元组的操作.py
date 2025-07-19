# -*- coding: utf-8 -*-
"""
@Time    :2022/8/9 14:50
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
'''
1.元组的定义
    元组是一些数据的顺序组合，组合之后不可修改（有序不可变）
    标识符：()和逗号,
    关键字：tuple
    元组中的元素支持字符、数字、字符串、也可以是嵌套的元组，元素之间也是用逗号隔开
    使用的场景：保证数据的安全性
当元组里面只有一个数据的时候，不加逗号那就是字符串，加了逗号就是元组
'''
tuple1 = ('hello',)
tuple2 = ('hello','python')
print("tuple1的数据类型是:",type(tuple1))
print("tuple1的长度是：",len(tuple1))

print("tuple2的数据类型是:",type(tuple2))
print("tuple2的长度是：",len(tuple2))

tuple3 = (1,2,3,6.66,False,[False,True],('haha','五点了'))
#元组的查：
#只能通过索引位 和 切片的方式去查
# 用法：变量名[索引位]   变量名[start_index:end_index:step]
print(tuple3[3]) #6.66
print(tuple3[-1][-1])  #五点了

#面试题：列表和元组的区别是什么？
#列表和元组之间如何进行转换？ 用list方法 或者tuple方法即可
list66 = [123456,654321]
tuple88 = ('haha','123')
tuple66 = tuple(list66)
list88 = list(tuple88)
print(tuple66)
print(list88,type(list88)) #['haha', '123'] <class 'list'>




