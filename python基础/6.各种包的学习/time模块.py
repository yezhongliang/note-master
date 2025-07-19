# -*- coding: utf-8 -*-
"""
@Time    :2023/1/19 11:51
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""time模块---python自带的模块
时间的3种表示方式：
1.当前的时间戳：time.time()
2.当前的时间元组：time.localtime(),
    后续会用到时间元祖的年月日来生成自动化测试报告的文件名
3.英文显示时间字符：time.asctime()
时间戳：指的是格林威治（伦敦）时间1970年1月1日0分0秒其到现在的总秒数，每一秒都在变化增加
时间元组：用一个元组装起来的9组数字表示时间
4.线程等待/强制等待 sleep(),形参的值单位是秒，是整数

time模块用处：
1.使得线程等待/程序等待，多少秒之后再去进行
2.用来生成文件，文件名字带上时间格式

"""

import  time

#时间戳：时间戳是1970年1月1日格林威治时间到当前时间所经历的秒数
# time.time
# print('当前的时间戳为：{}'.format(time.time()))

#时间元组
# print("当前的时间元组：{}".format(time.localtime()))
# print('当前的年份是：{}'.format(time.localtime().tm_year))
# print('当前的月份是：{}'.format(time.localtime().tm_mon))
# print('当前的日是：{}'.format(time.localtime().tm_mday))
# print('数据类型是：',type(time.localtime().tm_mday))

# 2023/5/3 时:分:秒
# print(str(time.localtime().tm_year)+'-'
#       +str(time.localtime().tm_mon)+'-'
#       +str(time.localtime().tm_mday)+ ' '
#       +str(time.localtime().tm_hour)+':'
#       +str(time.localtime().tm_min)+ ':'
#       +str(time.localtime().tm_sec))

def File_time_create():
    file_time = (
      str(time.localtime().tm_year)+'-'
      +str(time.localtime().tm_mon)+'-'
      +str(time.localtime().tm_mday)+ ' '
      +str(time.localtime().tm_hour)+':'
      +str(time.localtime().tm_min)+ ':'
      +str(time.localtime().tm_sec))
    return  file_time

def File_time_create_other_function():
    Time_yuanzu = time.localtime()
    time1 = str(Time_yuanzu.tm_year) + '年' + str(Time_yuanzu.tm_mon) + '月' + str(Time_yuanzu.tm_mday) + '日' + str(
        Time_yuanzu.tm_hour) + '时' + str(Time_yuanzu.tm_min)
    file_name = str(time1) + ' report.html'
    return file_name

# file_time = File_time_create()
# print(file_time)

#asctime，时间字符串的显示形式
# print(time.asctime())


#线程等待 、强制等待
# time.sleep(5)
# print('睡了多少秒')
