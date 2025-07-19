# -*- coding: utf-8 -*-
"""
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
from 文件的操作.ini文件的操作.ini文件介绍 import ini_utils
import pymysql


class Mysql_object():
    # def __init__(self,host,user,password,database,port,charset='utf8',autocommit=True):
    #     self.host = host
    #     self.user = user
    #     self.password = password
    #     self.database = database
    #     self.prot = port
    #     self.charset = charset
    #     self.autocommit = autocommit

        #数据库连接设置
    def connect(self):
        self.conn = pymysql.connect(host=ini_utils(section='mysql',option='host'),
                               user=ini_utils(section='mysql',option='user'),
                               password=ini_utils(section='mysql',option='password'),
                               database=ini_utils(section='mysql',option='database'),
                               port=ini_utils(section='mysql',option='port'),
                               autocommit=True)
        #生成游标
        self.cur = self.conn.cursor()

        return self.conn,self.cur

    def query_select(self,sql):
        """
         select 查询语句
        :param sql:
        :return:
        """
        self.sql = sql.lower()   #lower是把字符串全部转换成为小写
        try:
            self.cur.execute(self.sql)
        except:
            print('sql error')

        finally:
            pass
