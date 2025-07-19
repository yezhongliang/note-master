# -*- coding: utf-8 -*-
"""
@Time    :2022/8/17 12:10
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""安装：pip install pymysql
pymysql是python用来连接数据库的。
操作步骤：
    1.导包:import pymysql
    2.数据库连接设置：conn = pymysql.connect(host,user,passwd,port,database,charset)
    3.生成游标： cur = conn.cursor()  #标识
    4.编写sql语句：sql = 'select * from xx'
    5.执行sql语句：cur.excute(sql)
    6.获取数据： data = cur.fetchall()  
    7.关闭游标：cur.close
    8.关闭连接：conn.close()
增删改查四个操作，只有查是不需要提交的，增删改都是要提交
提交分为两个方式：一个是自动提交(在创建连接的时候，autocommit=True)，
一个是手动提交：conn.commit() 
"""

#1.导包
import pymysql
#2.设置数据库连接属性,connect类
# conn = pymysql.connect(host='192.168.203.179',
#                        port=3306,
#                        user='root',
#                        password='Aa123456.',
#                        database='18bandb_copy',
#                        autocommit=True)
#
# #3.生成游标
# cur = conn.cursor()
#
# #4.写sql
# #insert_sql
# insert_sql = 'insert into test18 values(3,"zhangsan",18,18,10)'
# # delete_sql
# delete_sql = 'delete from test18 where name like "autotest%"'
# # update_sql
# # select_sql
# select_sql = "select * from test18"
#
# #5.执行sql语句,execute返回的结果是查询的条数
# cur.execute(delete_sql)
#
#
# #6.获取具体的数据,fetchall() 获取游标所有的数据,
#                 # fetchone()获取游标所有记录中的第一条
#                 #fetchmany()获取游标记录中的多条，需要传值获取多少条，看源码
# # data = cur.fetchall()
# # print(data)
#
# # 思考1：sql一共拿到10条数据，
# # 然后先用fetchone()输出一条，
# # 然后再用fetchmany()输出3条，他们分别输出的是哪些数据呢？
#
#
# #7.关闭游标
# cur.close()
#
# #8.关闭连接
# conn.close()


def mysql_connection_utils():
    import pymysql
    conn = pymysql.connect(host='192.168.203.182',
                           port=3306,
                           user='root',
                           password='Aa123456.',
                           database='cms',
                           autocommit=True)
    cur = conn.cursor()
    delete_sql = 'delete from sys_user where user_name like "test_cms_%"'

    cur.execute(delete_sql)
    cur.close()

    conn.close()


mysql_connection_utils()











































