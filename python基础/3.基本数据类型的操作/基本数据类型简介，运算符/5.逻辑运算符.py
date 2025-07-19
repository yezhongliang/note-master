# -*- coding: utf-8 -*-
"""
@Time    :2022/8/8 11:21
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

#逻辑运算符 and与 or或  not非
# and:全真才真
# or：有真则真\
# not 反

a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)
print(a and not b or b)

"""运算优先级：比较运算符 > 逻辑运算符 
    逻辑运算符内部比较：not > and > or
"""
print(not 1>2 and 3>2 ) #True

# print(not False or False and True)
#    True or False and True
#    True
# print(1+1 > 1+2 and 3+2 <3-1 or True and not False)
#     False and False or True and True
#     False or True
#     True
#
# print(not 1 and not 0 or 4 and 2)
#     False  and  True or 2 and 2
#     False or True
#     True
print(1 and 2)











