# -*- coding: utf-8 -*-
"""
@Time    :2022/8/9 14:17
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""
字典：
    标识符：{}
    关键字：dict
    特点：无序可变（无序：不能通过索引值来查找数据）
    存储数据的方式：  key:value,键值对的方式存储
    key:不能被修改且唯一，支持的数据类型是int float bool str
    value：可以被修改，不唯一，支持的数据类型是任何的数据类型
类似于json数据

"""
dict1 = {}
# print(type(dict1),len(dict1))  #<class 'dict'>

#需求：学生的信息包含了 姓名 年龄 性别 语数英分数，学校地址
dict2 = {
    '姓名':'15ban',
    '年龄':30,
    '性别':1,
    'score':[100,200,300],
    'addr':('广州市','天河区','棠下')
}

#字典的查：
#语法： 变量名['key'] 就可以查到key对应的value值
# 取单个值：
# print(dict2['score'][-1]) #300
# print(dict2['score'][2])  #300

#取所有的key值
#用法： 变量名.keys()
# print(dict2.keys(),type(dict2.keys())) #dict_keys(['姓名', '年龄', '性别', 'score', 'addr']) <class 'dict_keys'>

#取所有的value值
#用法   变量名.values()
# print(dict2.values(),type(dict2.values())) #ict_values(['15ban', 30, 1, [100, 200, 300], ('广州市', '天河区', '棠下')]) <class 'dict_values'>

#获取所有的键值对：items()
# 用法： 变量名.items()
# print(dict2.items())

#字典的增加操作
# 给字典增加一个元素,如果key值已经存在，则新加入的value值会替换掉前面的value值，而不会新建一个key值
#用法：变量名['new_key']  = value
# dict2['score'] = '准备下课了，今晚晚点走'
# dict2['new_key'] = '准备下课了，今晚晚点走'
# print(dict2)

#字典增加的方法2：update方法去增加
#用法：两个字典的值去拼接在一起,         变量名1.update(变量名2)
# dict3 = {'a':10086,'b':10000,'c':10010}
# dict2.update(dict3)
# print(dict2)

#字典增加的方法3： d = dict(dict1,**dict2),此方法的弊端是key要都是字符串才能使用
#TypeError: keywords must be strings
# dict4 = {'a':123,'b':456}
# dict5 = {'c':789,'d':888}
#
# d = dict(dict4,**dict5)
# print(d)  #{'a': 123, 'b': 456, 'c': 789, 'd': 888}


#删除字典里面的某个元素
    # 1.pop  用法： 变量名.pop('key')  或者 删除整个键值对
    # 2.popitem 用法：  变量名.popitem()
    # 3.del  用法：  del 变量名['key'] 删除整个键值对
    # 4.clear  用法   变量名.clear()

#1 pop
print(dict2)
# dict2.pop('addr')
# print(dict2)

#2 popitem
# dict2.popitem()
# print(dict2)

#3 del
# del dict2['score']
# print(dict2)

#4 clear
# dict2.clear()
# print(dict2)  # {}


#字典的改
#用法： 变量名['old_key'] = new_value
#把字典中嵌套的列表的300修改成为3000
dict2['score'][-1] = 3000
print(dict2)


# dict2['addr'][-1] = '车陂'

