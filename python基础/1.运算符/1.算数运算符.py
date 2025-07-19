"""
"""
"""
算术运算符：加 减 乘 除 取余 求幂 向下取整
取余：6 %  4 = 2
求幂：2 ** 3 = 8
向下取整：10 // 4 = 2
"""
# 加法，注意加法都是用数字进行加减的，不能用字符串进行加减 +
num1 =  10
num2 =  20
num3 = 10.1
num4 = 3

print(num1 + num2)
print(num1 + num3)

# 乘法   *
print(num1 * num2)
print(num1 * num3)

# 减法  -
print(num1 - num2)

# 除法 /
print(num2/num1)

#取余 %
print(num1 % num4)

#求幂 **
print(num1 ** num4)

#向下取余 //
print(num1//num4) #无论小数是9还是1，都是取0 ，3.9=3  3.1=3


