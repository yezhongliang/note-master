# -*- coding: utf-8 -*-
"""
@Time    :2022/8/10 15:02
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
range方法：range 是序列，用于生成一系列的数字
    1.range(m,n,k) 
        m:初始值
        n：表示的是结束，n也是取不到的，取左不取右
        k：表示的是步长，k可以不填，不填则默认为1
    2.range(m,n)
        m:初始值
        n：表示的是结束，n也是取不到的，取左不取右
    3.range(n)--》range(0,n,1)
        n:表示的是末尾，也是取左不取右
        m：默认是0开始了
        k：默认是1
"""



# student id name yuwen shuxue yingyu
# 求三科总分最高的学生的姓名 max sum name
# select name from student max(sum(yuwen+ shuxue + yingyu))
# 思路：三科求和 然后排序（降序排序） 然后 limit

# 数据库对于测试人员的使用方向：
# 1.校验数据（查看页面显示的数据和数据库的数据是否一致）
# 2.造数据（存储过程） 存储过程造数据：当表和表之间的关联非常多的时候，或者字段较多的时候，
# 造数据起来非常麻烦（在cms造文章表的数据）
# mysql增：create database 、 create table  create view 、create procedure、alter table add
#       删：drop （database，table ，删字段）---不保留表的定义-DDL语句
#         truncate 清空表   ---保留DDL语句（建表语句）
#         delete （删除表里面的某些数据）
#       改：update
#       查：select （where ，group by，order by，in not in，limit ）
#            left join、 right join 、inner join 、where
# mysql数据库的基本数据类型：int bigint  float char varchar date  datetime
# 约束：主键约束，外键约束，自增约束，非空约束，默认值约束
# 存储过程：造数据--create procedure test(n int)
# 索引：主键索引，唯一索引，普通索引（索引的增删改查），索引的作用，索引为什么失效，在什么
# 情况在容易失效。索引存储在什么地方？索引是不是越多越好？
# 视图：view ，视图的作用，视图的增删改查



