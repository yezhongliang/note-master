# -*- coding: utf-8 -*-
"""
@Time    :2023/1/16 18:07
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

import pymysql
import threading
class ZaoShuJu():
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.203.158',
                                    user = 'root',
                                    password='Aa123456.',
                                    database='cms',
                                    port=3306,
                                    autocommit=True)
        self.cursor = self.conn.cursor()

    def SQL(self,sql_type):
        if sql_type == 'query':
            self.sql = "select * from sys_user"
            self.cursor.execute(self.sql)
            return self.cursor.fetchall()
        elif sql_type =='delete':
            self.sql = "delete from sys_user where user_name like '%test%'"
            self.cursor.execute(self.sql)
        elif sql_type =='insert':
            self.sql = "insert into sys_user values(null,'test666','e10adc3949ba59abbe56e057f20f883e','zhangsan','15521048080','123@qq.com','0','0',null,'l',0, '2022-12-09 17:36:29',-4,'2022-12-09 17:36:29' ,-4)"
            self.cursor.execute(self.sql)
        else:
            pass


a = ZaoShuJu()
a.SQL(sql_type='insert')
while 1:
    a.SQL(sql_type='insert')












