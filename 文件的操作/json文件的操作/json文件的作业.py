# -*- coding: utf-8 -*-
"""
@Time    :2023/1/16 17:01
@version :Python3.7.4
@Software:pycharm2020.3.2
"""


"""
封装一个读取/写入/清空json文件的类
"""
import json
class Jsonutil():

    def read_jsondata(self):
        with open('jsondata.json', mode='r') as file:
            object = json.load(file)
        return object

    def write_jsondata(self,data):
        pass

    def clear_jsondata(self):
        with open('jsondata.json', mode='w') as file:
            file.truncate()

