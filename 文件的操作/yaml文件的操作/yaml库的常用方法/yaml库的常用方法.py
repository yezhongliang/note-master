# -*- coding: utf-8 -*-
"""
@Time    :2023/1/16 11:47
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""
对于YAML文件的读取和写入方法有：
读取yaml文件
    yaml.load() ---官方提示不安全，yaml库在5.1会有这个提示,不推荐使用
    yaml.safe_load() ---推荐使用
写入yaml文件
    yaml.dump()
    yaml.safe_dump() ----官方推荐使用
    yaml.dump_all()
    yaml.safe_dump_all()


"""
import yaml

# #yaml.load()
# # with open(r'test.yaml') as file:
# #     data = yaml.load(file)
# #     print(data)
# #
# # #yaml.safe_load()
# # with open(r'test.yaml') as file2:
# #     data = yaml.safe_load(file2)
# #     print(data)

# #yaml.dump---不推荐使用
# list1 = ['zhangsan','lisi','wangwu']
# with open('test.yaml',mode='a+') as file3:
#     yaml.dump(data=list1,stream=file3)
#
# #yaml.safe_dump  ----推荐
# list2 = ['zhangsan','lisi','wangwu','liuniu']
# with open('test.yaml',mode='a+') as file4:
#     yaml.safe_dump(list2,file4)

#yaml.safe_dump ----推荐
# dict1 = {'username':'admin','password':123456}
# with open('test.yaml',mode='w+') as file5:
#     yaml.safe_dump(dict1,file5)




