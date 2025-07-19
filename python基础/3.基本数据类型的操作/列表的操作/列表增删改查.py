# -*- coding: utf-8 -*-
"""
@Time    :2022/8/8 16:36
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""
列表的标识符：[] 中括号
列表中的元素支持字符串，数字，也可以嵌套列表，元素与元素之间是有逗号隔开，元素的值可以被修改
len()方法 --》统计数据的长度
列表的操作：增、删、改、查
列表也是有序可变
    有序：可以通过索引去查数据
    可变：里面的元素是可修改
    列表属于一种可迭代的数据类型（可以往这个列表变量里面插入数据）
增加的方法：3种
    1.append (object),默认追加到最后一个元素
    2.insert，按照索引位增加，源码：（index,object），可以插入到任意的地方
    3.extend （可以增加list，也可以增加str，甚至可以增加tuple-元组，dict-字典）

删除的方法：4种
    1.pop，默认删除最后一个元素，也可以根据索引位去删除你想要的元素
    2.del，根据索引位去删除
    3.clear，清空，清空列表里面的所有元素，但是保存列表的定义，变成一个空列表
    4.remove，根据元素的值进行删除
"""
#type()   len()
# 定义一个列表
# list1 = ['','',1,'123','haha']
# print(list1,type(list1),len(list1))

list_1 = [1,2,3,4,5,6,'18ban','明天出去耍',[11,22,33,44,[5,6,7,False]],False,True]

#列表的查：通过索引位的方式去查，可以通过切片的方式去查
#语法：变量名[索引位]
# print(list_1[7])
# print(list_1[0:4])
#嵌套查：
print(list_1)
print(list_1[-3][-1][-2])

#列表的增加数据，增加数据有三种方法：append-追加，insert-插入 ，extend-延申-拼接
#append, 追加元素，这种方法默认追加到最后面去
# 语法：变量名.append('被追加的元素')
# print(list_1.append('damazi')) #不可以的，会返回None
# list_1.append('damazi')
# print(list_1)


# insert方法，插入元素到指定位置，根据索引位去插入，使用此方法的时候需要注意索引位
# 语法：变量名.insert(index,'被插入的元素')
# 查看源码：ctrl + 鼠标左键，可以查看源码，教你去怎么使用这个方法的
# list_1.insert(1,'ermazi')
# print(list_1)

#extend 一次只能增加一个或者多个元素，加的数据必须是可迭代的数据类型
#extend列表
# 语法：变量名.extend(新列表)
# list_2 = [111,222,333]
# list_1.extend(list_2)
# print(list_1)
#extend 字符串,字符串会被拆分称为单个元素再插入到列表去
# str1 = '123'
# tuple1 = (1,2,3)
# list_1.extend(tuple1)
# print(list_1)


#总结：列表的增加的三种方法：append能够增加任何的数据类型，而且是默认放到列表的最后面
# insert 方法，能够根据索引位插入到任何的位置，插入的数据类型是任意的数据类型
# extend 方法，增加的新的数据类型必须是列表，字符串而且默认也是放到最后面，而且增加的数据额类型
# 不能是number


#列表的删除操作，删除有四种分别是remove、pop、clear、del
#remove方法，特点是通过元素的值删除，如果元素的值不存在，则会报错
#用法 变量名.remove(元素的值)
# list_1.remove('18ban')
# print(list_1)

#pop方法，如果不带索引位那就默认删除最后一个，如果带索引位那就删索引位对应的值
# list_1.pop(-1)
# print(list_1)

#clear方法，清空列表的所有元素，但是保留列表的定义
#truncate方法，清空表的所有数据，但是保留表的字段定义（保留DDL）
# 语法：变量名.clear()
# list_1.clear()
# print(len(list_1),type(list_1),list_1)

#del方法，删除列表中的指定的值，通过索引位的方式去删除
#用法： del 变量名[索引位]
# print(list_1)
# del list_1[-1]
# print(list_1)

#列表的改，通过 变量名[索引位] = new_value 去改
# list_1[6] = '18班明天出去耍'
# print(list_1)



















