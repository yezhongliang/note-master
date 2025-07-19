# -*- coding: utf-8 -*-
"""
@Time    :2022/8/8 10:53
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""
1.运算符：
    算数运算符  +加法  -减法  *乘法  /除法  %取余  **求幂 //取整
    比较运算符 >   <   !=   ==   >=   <=
    赋值运算符 =  
    成员运算符 in   not in
    逻辑运算符 and or not  

"""
#算数运算符
number1 = 11
number2 = 20
number3 = 3
float1 = 6.66
float2 = 8.88
bool1 = False  #当布尔值被使用成为数值计算的时候，只能表示Fasle0 或者True 1
bool2 = True
print(number1+number2)  #30
print(number1+float1)   #16.66
print(float1+ float2)   # 15.54
print(float1+bool1)     # 6.66
print(bool1+bool2)      # 1
print(float1 * bool2)
print(number2      /       number1)
print(number1 / number3)
print(number1 % number3)
print(number1 ** number1)
print(number1 // number3)
