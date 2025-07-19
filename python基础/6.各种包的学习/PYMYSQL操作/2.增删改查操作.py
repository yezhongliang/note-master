# -*- coding: utf-8 -*-
"""
@Time    :2022/8/17 15:24
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
from time import  sleep

#1.导包
import pymysql
#2.设置数据库连接属性
conn = pymysql.connect(host='192.168.203.158',
                       user='root',
                       password='Aa123456.',
                       database='cms',
                       port=3306,
                       autocommit=True
                       )
#3.生成游标


#4.写sql，增删改查,注意增删改这三个操作，需要手动提交,才能生效，除非你加上了autocommit这个参数=True


#5.执行sql语句,execute返回的结果是查询的条数res = cur.execute(sql)


# conn.commit()  #增、删、改操作需要增加这句commit的代码，如果不加，数据库的数据更新不了；
#             另外的方式：autocommit = True
#6.获取具体的数据,fetchall() 获取游标所有的数据库,


#7.关闭游标

#8.关闭连接

