# -*- coding: utf-8 -*-
"""
@Time    :2023/1/14 15:06
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
1）使用key + ":" + 取值
示例： name： zhangsan
转为python字典：{'name': 'zhangsan'}

2) 字典嵌套字典的表示方法
示例：
    data:
        user1:
            username: test01
            password: 123456
        user2:
            username: test02
            password: 123456
转为python字典：
    {'data': {'user1': {'username': 'test01', 'password': 123456}, 'user2': {'username': 'test02', 'password': 123456}}}

3) 字典嵌套数组的表示方法
示例：
    data:
        -
            username: test01
            password: 123456
        -
            username: test02
            password: 123456
    转为python字典：
    {'data': [{'username': 'test01', 'password': 123456}, {'username': 'test02', 'password': 123456}]}

"""

import yaml
with open('yaml_shuzu',mode='r') as file:
    data = yaml.safe_load(file)
    print(data)