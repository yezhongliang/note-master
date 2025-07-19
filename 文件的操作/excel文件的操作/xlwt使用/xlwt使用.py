# -*- coding: utf-8 -*-
"""
@Time    :2022/8/12 15:14
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""
xlwt库的写入，写入到xls文件

操作五步骤
    1.import xlwt
    2.创建一个对象（.xls）文件，book=xlwt.Workbook(encoding='utf-8')
    3.创建一个sheet工作表:  sh1 = book.add_sheet('username_pwd')
    4.添加内容：
        操作1增加字段：给每个单元格添加值，单元格行和列分别从0开始
        sh1.write(0,0,'username')  行，列，内容
        sh1.write(0,1,'pwd')       行，列，内容
        操作2写入值：
        row1 = ['admin','123456']
        for i in range(len(row1)):  #这里根据row1的长度循环2次，0和1
            sh1.write(1,i,row1[i])  当i=0时，写入的是第二行，第一列，admin
                                    当i=1时，写入的是第二行，第二列，123456
                                    (UI自动化第一天,0,'admin')  (UI自动化第一天,UI自动化第一天,'123456')
    5.保存文件 book.save(文件名.xls)  #路径+文件名

"""

# #例子1：在一个.xls文件中写入数据，并保存在login.xls
# import xlwt
# #创建一个excel，因为如果不用utf-8，写入中文是不行的
# book = xlwt.Workbook(encoding='utf-8')
# #创建一个sheet工作簿
# sh1 = book.add_sheet('第一个工作表')
# #写入字段
# sh1.write(0,0,'username') #0,0代表第一行第一列，索引位，写入字段username
# sh1.write(0,1,'pwd')   #0，1代表第一行第二列，索引位，写入字段pwd
# #写入数据
# row1 = ['admin','123456']
# for i in range(len(row1)):
#     sh1.write(1,i,row1[i])  #如果想要写入到第三行，直接改索引位
# #保存excel表格，可以选择保存的路径
# book.save('login11.xls')  #这样会保存在当前路径
# book.save('D://login11.xls')  #保存在别的路径，需要path+filename
# # book.save('D:/login.xlsx')  #write是不支持slxs的写入的，
#                         # 但是不能用office打开，能用wps打开
#
#
#第一步：导包
import xlwt

#第二步：创建一个xls的表格
book = xlwt.Workbook(encoding='utf-8')

#第三步：创建一个sheet表格
sheet1 = book.add_sheet('this_is_my_first_sheet')

#第四步：写入内容--写入字段
sheet1.write(0,0,'哈哈')
sheet1.write(0,1,'pwd')

#写入内容--写入数据
# row1 = ['admin','123456']
row2 = [['zhangsan','123456'],['lisi','123456']]
# for i in range(len(row1)):
#     sheet1.write(1,i,row1[i])

#第五步：保存文件
book.save('yonghu.xls')




