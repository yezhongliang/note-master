""""""
"""
ini文件一般作为配置文件来使用
文件里面可以有多个节点:[test]
[test]
tester1=haha
tester2=kaixin
tester3=henkaixin

读取ini文件可以用open的方法一行行的读取，但是不方便
建议使用configparse（内置模块）
模块里面常用的方法：
    1.read--获取文件名
    2.items获取某个节点的所有键值对
    3.sections获取所有的节点名
    3.get获取某个节点的某个键对应的值
"""

import  configparser
# #声明一个对象用于操作
# data_object = configparser.ConfigParser()
#
# #读取,相对路径的方式读取
# data_object.read('config.ini',encoding='utf-8')
#
# #1.获取所有节点
# all_jiedian = data_object.sections()
# print(all_jiedian)
#
# #2.获取某个节点的所有键值对,获取出来的是列表嵌套元素的数据
# # [('tester1', 'zhangsan'), ('tester2', 'lisi'), ('tester3', 'wangwu')]
# # items = data_object.items('tester')
# # print(items)
#
# #遍历获取：
# # for key,value in data_object.items('tester'):
# #     print(key,value)
#
# #3.获取某个节点下某个键对应的值,用的get的方法，第一个值传的是节点，第二个值传的是key
# res = data_object.get('tester','tester1')
# print(res)


# data = configparser.ConfigParser()
#
# data.read('config.ini')
#
# keys = data.sections()
# print("所有的节点包含：{}".format(keys))
#
# key_values = data.items('tester')
# print(key_values)
#
# value = data.get('mysql_config','username')
# print(value)
#

def ini_utils(section, option):
    file = r'D:\TestTool\project_for18\文件的操作\ini文件的操作\config.ini'
    ini_object = configparser.ConfigParser()
    ini_object.read(file)
    data= ini_object.get(section, option)
    return data



# a = ini_utils(section='mysql',option='user')
# print(a)