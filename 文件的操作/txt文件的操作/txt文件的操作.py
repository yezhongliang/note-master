# -*- coding: utf-8 -*-
"""
@Time    :2022/8/11 15:29
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
txt文件的操作（excel和yaml文件的操作）
    主要使用的场景：自动化框架中日志信息的记录
txt文件的操作的流程：
    1.打开这个文件--》filename = open(路径,模式) 
    2.对这个文件进行读/写-->file.write/read
    3.关闭这个文件 -->file.close()，如果不关闭，则打开的文件越来越多，电脑会越来越卡
模式：
    r（read）:
        r:只读的方式打开，文件如果不存在则会报错
        rb：以二进制格式打开用于只读，常用于图片，音频，视频等
        r+：打开一个文件用于 读写,会覆盖掉前面等字符数的字符
    w（write）:
        w：写方式打开，文件不存在则会创建一个文件，如果文件本来就存在，则会覆盖之前的内容
        wb：写方式打开，以二进制的方式写入
        w+：打开一个文件用于读写，会清空之前的内容
    a(append)：
        a:追加方式打开，如果文件不存在则会创建，存在则会后面追加新的内容
        ab：二进制格式打开一个文件
        a+：打开一个文件用于读写操作，不会清空之前的内容，读取的时候需要注意：因为此模式下指针默认会放在
        最后面，需要用seek(0) 这个方法去把指针放到最前面再去读取
"""
"""open函数，此函数用于打开文件进行操作
stream字段：流文件(理解为文件的相对路径或者绝对路径)
转义：\t(空格键) \n（换行键）   \a \b   \\表示一个斜杠
防止转义：字符串前面加r，或者每一个转义符之间加一个\
"""

# #第一步：打开一个文件
# file_1 = open(file=r'D:\TestTool\project_for18\文件的操作\txt文件的操作\test.txt',mode='r')
# #第二步：对文件进行读或者写
# data = file_1.read()
# print(data)
# #第三步：关闭这个文件
# file_1.close()


#读取文件：用read方法来读取文件，一个字一个字的读取
# file_2 = open(file='test1.txt',mode='r')#相对路径，只需要填写文件名即可，但是使用
# #相对路径的时候，要注意写代码的文件要和备操作的文件在同一个目录里面
# data1 = file_2.read()
# print(data1)
# file_2.close()


#读取文件：用readline方法来读取文件
#默认是读取第一行，当传了值后，按字节去读取
# file_2 = open(file='test1.txt',mode='r')#相对路径，只需要填写文件名即可，但是使用
# data1 = file_2.readline(-1)
# print(data1)
# file_2.close()

#读取文件：用readlines方法来读取文件，读取完后会存在一个列表里面，一般用for循环来读取
# file_2 = open(file='test1.txt',mode='r')#相对路径，只需要填写文件名即可，但是使用
# data1 = file_2.readlines()
# print(data1)
# file_2.close()


#write 写入操作 w
# file1 = open(file='test4.txt',mode='w')
# # file1.write("{'name':'zhangsan'}")
# file1.close()


#追加写操作 a
# file2 = open(file='test2.txt',mode='a+')
# file2.write('hahahaha\nhahahaha\nssss\n')
# file2.close()

#r+
# file1 = open(file='test4.txt',mode='r+')
# data = file1.read()
# file1.write('hahaa')
# print(data)
# file1.close()


# #a+ 光标移动，用的方法是seek()
# file1 = open(file='test4.txt',mode='a+')
# d = file1.read()
# print("移动光标之前输出的内容：{}".format(d))
# #移动光标到最左边
# file1.seek(1)
# d1 = file1.read()
# print("移动光标之后输出的内容：{}".format(d1))
# file1.close()


with open(file='test4.txt',mode='r+') as file1:
    data = file1.read()
#特点：只要是除了这个with，里面的write的操作就会自动被保存

# 面试题：
# 1.open和with open的区别是什么？
# open要手动关闭文件，但是withopen是自动关闭文件的
# 2.为什么with open会自动关闭文件呢？
# 因为with这个关键字用的是上下文管理器
# 3.什么是上下文管理器？
# __init__ __new__称为python的魔法函数（python的）
# with自带了两个魔法函数：__enter__,__exit__














