# -*- coding: utf-8 -*-
"""
@Time    :2022/8/12 15:47
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
xlrd库读取xls、xlsx文件
在xlrd1.2.0之后，就不支持xlsx的读取了
步骤：
    1.import xlrd
    2.打开一个文件（xls或者xlsx文件）book=xlrd.open_workbook('login.xls')有路径可以拼接
    3.使用sheet工作表 sh1=book.sheet_by_name('第一个工作表')
                      sh1 = book.sheet_by_index(0)  #也是第一个sheet
    4.读取sheet工作表的属性信息
        print('sheet名称：',sh1.name)
        print('sheet总行数：',sh1.nrows) #有数数据的总行数
        print('sheet总列数{}：'.format(sh1.ncols)) #有数据的总列数
    5.读取sheet工作边存储的文本内容
        5.1读取一行：row1=sh1.row_values(0) 索引位去读，row-行
        5.2读取一列：col1=sh1.col_values(0) 索引位去读  col-列
        5.3读取一个单元格：
            cell_1=sh1.cell_value(0,0) #前面的0是行，后面的0是列
            cell_2=sh1.cell(0,0).value
"""
#案例1：读取login.xls的工作表名、总列数、总行数以及存储的数据
#导包
import xlrd
#打开test1.xls文件
# book = xlrd.open_workbook('test1.xls')
#使用sheet工作表（可名字可索引位，索引位为常用）,打开第一个工作表
# sheet1 = book.sheet_by_index(0)
#读取sheet的属性信息
# print(sheet1.name)

#读取有多少个工作簿
# print(book.sheets())

#获取工作簿的行数有多少
# print(sheet1.nrows)
#获取工作簿的列数有多少
# print(sheet1.ncols)

#读取一个单元格的内容：
# cell_data = sheet1.cell_value(0,0)
# print(cell_data)

# #读取一行的内容：
# row_data = sheet1.row_values(1)
# print(row_data)
# #读取一列的内容：
# col_data = sheet1.col_values(0)
# print(col_data)

#读取第一行的 第一和第二列的内容
# data = sheet1.row_values(0,start_colx=0,end_colx=2)
# print(data)
# #读取第一列的  第一行和第二行的内容？



#读取xlsx文件的工作表名、总行数、纵列竖以及存储的数据


#扩展1:以行的方式读取，要求读取所有的内容，tips：for range
# nrows = sheet1.nrows
# for i in range(nrows):  #0 1 2 3 4
#     print(sheet1.row_values(i))

#扩展2：以列的方式读取所有的内容  #意义不大


#扩展3：以单元格的方式读取，要求读取所有的内容，双重for循环
# nrows = sheet1.nrows
# for i in range(nrows):  #0 1 2 3 4
#     for j in :  #拿到的行的长度如何确认？
#         print(sheet1.cell_value(i,j))

book2 = xlrd.open_workbook('test1.xlsx')
sheet = book2.sheet_by_index(0)
data = sheet.row_values(0)
print(data)