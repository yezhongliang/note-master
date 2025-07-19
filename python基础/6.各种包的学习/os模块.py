# -*- coding: utf-8 -*-
"""
@Time    :2023/1/19 11:51
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
os模块是Python中整理文件和目录最为常用的模块，
该模块提供了非常丰富的方法用来处理文件和目录,
下面讲解一些最常用的方法：
1.os.getcwd(),获取当前文件的文件夹路径
2.os.listdir(path)，获取path里面的所有文件
3.os.path.exists(path),传入一个path路径，判断指定路径下的目录是否存在。存在返回True，否则返回False
    可以用相对路径 也可以用绝对路径
4.os.mkdir(path)，传入一个path路径，创建单层单个文件夹，文件夹存在则会报错,
    所以创建之前需要判断一下有无这个文件夹    
5.os.makedirs(path),传入一个path路径，生成一个递归的文件夹,文件存在则会报错
6.os.path.join(path1,path2)，传入两个path路径，将该路径拼接起来，形成一个新的完整路径
    path1\path2
"""






