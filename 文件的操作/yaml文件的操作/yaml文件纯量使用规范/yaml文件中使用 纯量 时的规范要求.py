# -*- coding: utf-8 -*-
"""
@Time    :2023/1/14 10:49
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
1) 数值直接以数值类型表示
yaml示例：price: 12.50   
转为Python字典：{'price': 12.5}


2）布尔值用true和false表示。
yaml示例：isAdult: true
转为Python字典： {'isAdult': True}
yaml示例：isAdult: false
转为Python字典： {'isAdult': False}


3）null用~表示。
yaml示例1：parentId: ~
转为Python字典： {'parentId': None}
yaml示例2：parentId: null
转为Python字典： {'parentId': None}


4）时间采用 ISO8601 格式。
示例：date: 2020-12-14

5) 日期采用复合 iso8601 格式的年、月、日表示。
示例：datetime: 2019-12-14t21:59:43


6) 如果需要用到强制类型转换请使用"!!数据类型 数据取值"
示例：passwd: !!str 123456
     gender: !!str true
转为Python字典： {'passwd': '123456', 'gender': 'true'}
"""

import yaml
with open('yaml_chunliang',mode='r') as file1:
    data = yaml.safe_load(file1)
    print(data)

