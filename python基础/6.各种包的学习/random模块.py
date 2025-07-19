# -*- coding: utf-8 -*-
"""
@Time    :2023/1/19 11:55
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""random模块，用于生成随机数，用于造测试数据的时候使用，非常基础但确重要的函数
random模块常用的方法：
random()     返回0-1之间的小数，取不到1，取左不取右
randint(x,y) 返回x和y之间的整数
randrange()  返回一个range序列里面的某个整数,取左不取右
choice()     返回一个序列中的某个数据
shuffle(list))    打乱序列的顺序
random.sample(seq,n)  从指定序列中随机获取指定长度的片断。
        sample函数不会修改原有序列。 如果k大于sequence元素个数的话会报错
        打印出来的是不重复的数值
"""
import  random

#random方法
# res = random.random()
# print(res)

#randint方法
# res1 = random.randint(1,10)
# print(res1)

#randrange方法
# res2 = random.randrange(1,10,2)
# print(res2)


#choice方法
list1 = [1,2,3,4,5,6,7,8]
tuple1 = (1,2,3,4,5,6,7,8)
str1 =  '12345678'
dict1 = {'name':'zhangsan','sex':1} #不是序列，会报错
res3 = random.choice(str1)
# print(res3)

#shuffle(list)) ,打乱功能
list2 = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(list2)
# print(list2)

# random.sample(seq,n)
list3 = [1,2,3,4,5,6,7,8,9,0]
res4 = random.sample(range(1,100),99)

# print(res4)


#写一个随机生成手机号码的函数，要求手机号码的开头是168，而且手机号不能重复，生成100个手机号
#分析：手机号长度：11位，168占了3位，剩下8位，这8位不能重复
# str_num1 = '168'
# for i in range(9):
#     num2 = random.choice([0,1,2,3,4,5,6,7,8,9])
#     res = str(num2)

def phone_number():
    for i in range(100):
        str_num1 = '168'
        str_1 = str(random.randint(0,9))
        str_2 = str(random.randint(0,9))
        str_3 = str(random.randint(0,9))
        str_4 = str(random.randint(0,9))
        str_5 = str(random.randint(0,9))
        str_6 = str(random.randint(0,9))
        str_7 = str(random.randint(0,9))
        str_8 = str(random.randint(0,9))
        res = str_num1 + str_2+str_3+str_4+str_5+str_6+str_7+str_8
    return res
a = phone_number()
print(a)








