""""""
"""逻辑运算符
与：and ，全真才为真
或：or，有真则真
非：not，反，真的反-->假

"""
a=True
b=False
print(a and b) #False
print(a or b) #True
print(a and  not b) #True

"""运算符之间优先级比较
    比较运算符>逻辑运算符
        逻辑运算符里面的优先级比较：
            not > and > or 
    算术> 比较 > 逻辑
"""

print(not 1>2 and 3>2) #True
# print(not False and True)
# print(True and True)
print(1+1 > 1+2 and 3+2 <3-1 or True and not False) #True
# print(False and False or True and True)
# print(False or True)

