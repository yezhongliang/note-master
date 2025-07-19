# -*- coding: utf-8 -*-
"""
@Time    :2023/2/24 11:11
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
    因为number包含int  float  bool  复数(包含实部和虚部)
    float和bool转int的类型，用int()方法
    float和int转bool的类型，用bool()方法
    bool和int转float的类型，用float()方法
    type函数，用来输出数据是数据什么数据类型的函数
"""
bool1 =False
float1=10.9
int1 = 100
bool2 = True
float2 = -0.1


#float和bool转成int数据类型,转成int就需要用int的函数，或者说用int的方法来转
#float 转int
print(int(float1))
print(type(int(float1))) #<class 'int'>

print(int(bool1)) #当bool值为False的时候被转换成为int或者float 或者是作为数字去加减的时候就是0
                  #True 是1了

#int 和 float转换成为bool值，用的是bool函数
#注意点：只要你的数值（int 还是float）只要不为 0 ，尽快是负数，转化之后都是1
print(bool(float2))
print(bool1+bool2)
print(type(bool1+bool2))

#bool 和int 转换成为float类型，用的是float函数





