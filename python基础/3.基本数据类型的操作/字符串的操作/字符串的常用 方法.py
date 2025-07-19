# -*- coding: utf-8 -*-
"""
@Time    :2022/8/8 15:47
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""
常用方法：
    1.startswith,判断是否以某个字符开头,a abc abcd
    2.endswith，判断是否以某个字符结尾
    3.isdigit,判断是否全部都是数字
    4.upper()  全部转成大写
    5.lower() 全部转成小写
    6.strip 去除字符串前后指定的内容  rstrip =right + strip    lstrip = left +strip
    7.split 切割，切割后的数据是一个列表,如果不填写切割多少次，默认切割全部，如果填了切割1次，则只切割一次
    8.replace 替换，替换字符串中指定的元素，如果不填替换多少次，则全部替换
    9.count 统计某个字符或者字符串出现的次数
    10.join 给字符串中的每个元素加入特定的字符
"""
str1 = 'We Are 18 Ban'
str2 = 'hello_python'
str3 = 'Hello haha Hello'
#1.startswith,判断是否以某个字符开头
# 用法：变量名.方法名
# print(str1.startswith('We '))

#2.endswith，判断是否以某个字符结尾
# print(str1.endswith('1'))

#3.isdigit,判断是否全部都是数字
# print(str1.isdigit())

#istitle此方法用来判断所有英文单词首字母是否大写
# print(str1.istitle())

#判断全部是否小写，，判断全部是否大写


# 4.upper()  全部转成大写
#isupper用来判断所有字符是不是都是大写字母
# print(str1.upper())
# 5.lower() 全部转成小写
# print(str1.lower())

# 6.strip 去除字符串首尾指定的内容
# print(str3.strip('Hello'))


# lstrip =left + strip
# print(str3.lstrip('Hello '))
#思考：print(str3.lstrip('haha '))  ？？？？？？？？？？？？


# 7.split 切割，切割后的数据是一个列表,如果不填写切割多少次，
# 默认切割全部，如果填了切割1次，则只切割一次
#此方法用于str数据类型转换成list数据类型
# print(str3.split(' '))
# print(type(str3.split(' ')))
# print(str3.split(' ',1)) #切1次

# 8.replace 替换，替换字符串中指定的元素，如果不填替换多少次，则全部替换
# print(str3.replace(' ','18'))

# 9.count 统计某个字符或者字符串出现的次数
# print(str3.count('Hello '))


# 10.join 给字符串中的每个元素加入特定的字符
print('888'.join(str3))

#11 字符串也可以进行拼接，也可以进行乘法




# 题目1：去除字符串的所有空格，str1 = we are 15 ban--->weare15ban
# 题目2：把str1全部转换成为大写，把str2全部转换成为小写
# 题目3：根据分号字符串进行分割，分割后形成列表的数据类型即可


"""字符串的增删改查：
增：.join()   
删：strip,lstrip,rstrip      'abcd' --->'ab'
改：replace
查：各种各样的判断方法，切片的方式查，通过索引位的方式去查

字符串如何变成列表：split方法
"""




