# -*- coding: utf-8 -*-
"""
@Time    :2022/8/8 14:44
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""
字符串（有序可变）：用引号来定义 ''  ，"" ,""" """
    有序：可以通过索引位的方式来查找值
    可变：定义好的字符串可以通过某些函数来进行修改,spilt,join,strip,lower,upper
    字符串也是属于可迭代的数据类型
取值：变量名[索引位]
len()函数  ---》length长度的意思，用来统计此字符串的元素个数（长度），空格也算
增：往字符串里面增加内容：join
删：给字符串剔除字符strip
改：replace
查：变量名[索引位] 
    索引分为正向索引和反向索引
        正向索引：从左往右，0开始
        反向索引：从右往左，-1开始
        
"""
#定义一个空的字符串
# str_1 =" "
# print(type(str_1),len(str_1))  #<class 'str'>
# print(type(len(str_1)))
#字符串的索引
# 正向索引：从左往右，0开始数
# 反向索引：从右往左，-1开始
# 用法： 变量名[索引位]
# str1='ABCDEFG'
# print(str1[-1])
# print(str1[6])
# print(str1[len(str1)-1])

#切片，只要有索引位的数据类型，都能够进行切片取值。
# 切片的语法：变量名[start_index:end_index:step]
    #step默认为1,取左不取右
str1='ABCDEFG'
print(str1[0:4]) #ABCD  0 1 2 3
print(str1[0:4:2]) #AC
print(str1[0:6:3])
print(str1[::2])
print(str1[::-1])  #面试常问，如果将一个字符串反转输出 GFEDCBA
print(str1[1:8:3])
print(str1[:])
print(str1[0:])
print(str1[0:-1:1])
print(str1[-3:-6:-1])
# 面试题：如果将一个字符串反转输出。abcd --->dcba

#字符串的改：
# print(str1.replace('A','B'))

#字符串的相加,字符串的拼接
str2 = '123'
str3 = '456'
print(str2+str3) #123，456   123456

#字符串的多次输出
print(str2 * 3)




