# -*- coding: utf-8 -*-
"""
@Time    :2022/8/9 15:35
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
字符串的格式化输出：
    1.%d  %s  %f  用百分号+英文的方式来占位，只要占了一个位置，就要有一个变量来接收
        %d--->输出整数（传入整数）
        %s--->输出字符串
        %f--->输出浮点型数据
        print(    'A是：%d，B是：%s，C是%f'% (value1,value2,value3)   )
    2.{}.format
        {}{}{}.format(value1,value2,value3)    
"""

#输出一个自我介绍：自我介绍的内容有年龄，性别，收入，住址，爱好
# print("我的年龄是：%d"%(18))
# print(    "我的年龄是：%d  。。。。我的性别是：%s"%(19,'男')   )
# print("我的年龄是： %d ****  我的性别是：%s  **** 我的收入是：%f *** 我的爱好是：%s"%(20,'女',21000.9,'唱跳rap篮球'))
# print("%d %s %f" %(100,'111',8.88))


"""2.{}.format
         {}{}{}.format(value1,value2,value3)
print('我的年龄：{}   我的性别：{}    我的收入: {}  我的爱好：{}'.format(21,'男',2100,'爱好测试'))
"""
#四个坑，但是只有3个萝卜不报错的操作方法
age = 30
sex = '男'
incoming = 2100
aihao = "Select * from people where age=20 and tall =180 and incoming = 100W and sex ='男' "
print('我的年龄：{}   我的性别：{}    我的收入: {}  我的爱好：{}'.format(age,sex,incoming,aihao))

