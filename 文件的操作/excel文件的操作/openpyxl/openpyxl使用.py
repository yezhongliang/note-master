# -*- coding: utf-8 -*-
"""
@Time    :2022/8/12 16:48
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""openpyxl打开xlsx文件写入数据的操作流程：本来有--》再写入
导包：import openpyxl
打开文件(.xlsx文件)：book = openpyxl.load_workbook(文件名)
使用sheet工作表：sh1=book.active或者
    sh1=book.get_sheet_by_name('第一个')  或者sh1=book['Sheet1']
写入数据
单元格写入：sh1['F2'] = 'PASS'  或者 sh1.cell(3,6).value='FAIL'  行和列的索引值是从1开始的   
2.整行写入：
	new_row = ['post-xml接口', 'post', 'https://httpbin.org/post']
	sh1.append(new_row)  #默认在有数据的下一行增加
保存文件：book.save(文件名.xlsx)

"""
# # 案例1：对api.xlsx写入数据
# #导包
# import openpyxl
# #定义一个book
# book =openpyxl.load_workbook('api.xlsx') #本来就有，然后写入数据
#
# #根据工作簿的name定义一个sheet1
# sheet1 = book.active  #默认第一个
# # sheet2 = book.get_sheet_by_name('哈哈')
# # sheet2['F2'] = 'hahahahahaa'
# # sheet2.cell(3,6).value='FAIL'
#
# # #在sheet1里面去操作了，操作的方法是根据单元格名字输入,无论行还是列
# sheet1['F1'] = 'hello'
# # sheet1.cell(2,6).value = 'Hello' #F2
# # #写入一行内容，放在一个列表里面去写入,会自动写入后有数据的下一行里面
# # new_row = ['hello',True,'Python','test']
# # sheet1.append(new_row)
# # #保存
# book.save('api.xlsx')

"""openpyxl创建新的xlsx文件写入数据的操作流程：本来没有--》创建后--》写入
导包：import openpyxl
创建一个新的workbook对象：book=openpyxl.Workbook()
创建新工作表：sh1=book.create_sheet([index=0,title='First Sheet'])
写入数据
1.单元格写入：sh1['F2'] = 'PASS'  或者 sh1.cell(3,6).value='FAIL'  行和列的索引值是从1开始的   
2.整行写入：
	new_row = ['post-xml接口', 'post', 'https://httpbin.org/post']
	sh1.append(new_row)
保存文件：book.save(文件名.xlsx)
"""
#案例：新建student.xlsx，并写入数据：sno，sname，class，UI自动化第一天,'test','8班'
#导包
# import openpyxl
# #创建一个book ，excel文件
# book = openpyxl.Workbook()
# #新建一个sheet1并且改名字
# sheet1= book.create_sheet(index=UI自动化第一天,title='one_sheet')#index=UI自动化第一天，表示第一个工作簿，并给一个title
# #写入数据
# # row1 = ['sno','sname','class']
# # row2 = ['UI自动化第一天','test','8班']
# # sheet1.append(row1)
# # sheet1.append(row2)
# book.save('api.xlsx')


"""
openpyxl读取xlsx文件数据的操作流程：
导包：import openpyxl
打开文件(.xlsx文件)：book = openpyxl.load_workbook(文件名)
使用sheet工作表：sh1=book.active或者sh1=book.get_sheet_by_name('Sheet1')  或者sh1=book['Sheet1']
读取sheet工作表的属性信息
当前sheet的名称：sh1.title
当前sheet的总行数：sh1.max_row  #指的是有数据的行数
当前sheet的总列数：sh1.max_column  #指的是有数据的列数
xlsx文件所有sheet名称：book.sheetnames
读取数据
按单元格读取：cell1 = sh1['A1'].value 或者  cell2= sh1.cell.value 行和列的索引值是从1开始的
按行读取：for row in sheet.iter_rows(min_row=1,max_row=3):
                      for cell in row:
                            print(cell.value,end='\t')
                        print()
按列读取：for row in sheet.iter_rows(min_col=1,max_col=3):
                      for cell in row:
                            print(cell.value,end='\t')
                        print()
"""
#导包
# import  openpyxl
# #新建一个book
# book = openpyxl.load_workbook('api.xlsx')
# #拿到第一个sheet并且右sh1来接受
# sh1 = book.active
# #用cellx来接收sh1工作簿里面单元格A1的值
# cellx = sh1['A1'].value
# #打印cellx的值
# print(cellx)


# import openpyxl
# book = openpyxl.load_workbook('111.xlsx')
# # sheet1 = book.active
# sheet1 = book['Sheet1']
# sheet1['B3'] = '1111111'
# row = ['111','222','33443']
# sheet1.append(row)
# # sheet1['A1']='学习openpyxl'
#
# book.save('111.xlsx')

import openpyxl
book =openpyxl.Workbook()
sheet1 = book.create_sheet(title='第一个工作簿',index=0)
sheet1['A1'] = 'zhangsan'
sheet1['A2'] = 'lisi'
sheet1.cell(3,3).value='damazi'
row = ['admin','123456']
sheet1.append(row)
book.save('222.xlsx')




