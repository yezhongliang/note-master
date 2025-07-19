# -*- coding: utf-8 -*-
"""
@Time    :2023/1/16 16:04
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""
封装一个读取/写入/清空yaml文件的类
"""
# test-yaml.py内容
import os
import yaml


class Yamlutil:
    # 读取yaml文件
    def read_yaml(self):
        with open(os.getcwd()+'\extract.yaml', mode='r', encoding='utf-8') as file:
            data = yaml.safe_load(stream=file)
            return data

    # 写入yaml文件,注意w会覆盖写
    def write_yaml(self,data):
        with open(os.getcwd() + "\extract.yaml", mode='w', encoding='utf-8') as file:
            yaml.safe_dump(data=data, stream=file)

    # 清除文件
    def clear_yaml(self):
        with open(os.getcwd() + "\extract.yaml", mode='w', encoding='utf-8') as file:
            file.truncate()


#读取
# object = Yamlutil()
# data = object.read_yaml()
# print(data)

#写入
# object = Yamlutil()
# object.write_yaml({'password':123456})

#清空
# a = Yamlutil()
# a.clear_yaml()


