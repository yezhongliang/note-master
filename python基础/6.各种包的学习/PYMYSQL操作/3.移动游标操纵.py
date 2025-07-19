# -*- coding: utf-8 -*-
"""
@Time    :2022/8/17 16:51
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
#1.导包
import pymysql
#2.设置数据库连接属性
conn = pymysql.connect(host='192.168.203.166',
                       user='root',
                       password='Aa123456.',
                       database='cms',
                       port=3306,
                       autocommit=True)
#3.生成游标
cur = conn.cursor()

#4.写sql
sql = 'select * from test limit 5'

#5.执行sql语句,execute返回的结果是查询的条数res = cur.execute(sql)
cur.execute(sql)

#6.获取具体的数据,fetchall() 获取游标所有的数据库,
data = cur.fetchall()
print(data)
"""
相对位置一开始只能往左移，
绝对位置一开始只能往右移，
不然都会报错：out of range
"""
#游标的移动操作：相对位置的移动，绝对位置的移动
#6.1相当位置的移动,以当前游标为起点，往右移是传正数，往左移是负数
# cur.scroll(value=-3)
# res = cur.fetchall()
# print(res)

#6.2绝对位置的移动，以第一个元素为起点
cur.scroll(value=4,mode='absolute')
res =cur.fetchall()
print(res)

#7.关闭游标
cur.close()
#8.关闭连接
conn.close()

#题目1：对mysql数据库操作，进行封装，封装成一个方法，供给teardown去直接调用
# teardown需要有 quit， 还有pymysql对数据的删除

#题目2：用ui自动化的方式去cms增加一个用户，
# 然后用pymysql对数据库进行连接，然后对这条新增的数据进行删除（delete * from sys_user where name = like）