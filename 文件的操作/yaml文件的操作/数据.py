# -*- coding: utf-8 -*-
"""
@Time    :2022/8/12 19:25
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
dic = {
    'name':'Tester',
    'age':10,
    'score':[10,20,30],
    'isTrue':True,
    'member':{'zhangsan':'101','lisi':'200'}
}
# print(dic['score'][2])  #拿到列表里面的30这个元素

#字典数据转成yaml数据格式


"""读取yaml 文件
读取yaml文件的操作流程：
导包：import yaml
打开yaml文件：with open(文件名，模式) as f(变量名):
读取yaml文件内容：
    data = yaml.safe_load(file)
    print(data,type(data))
with open 不需要close文件，因为用的是上下文管理器
    
"""
#读取yaml里面的数据：
#pip install PyYAML
#导包
import yaml
# #创建一个file变量用于打开并且接收
# file = open('test.yaml',mode='r',encoding='utf-8')
# #用data去接收经过加载过来的yaml数据
# data = yaml.safe_load(file)

#直接打印出data是什么数据，并且打印类型
# print(type(data),data)
# print(data['dic']['score'][2])  #拿到30
# file.close()

# with open(r'D:\TestTool\project_for8\文件的操作\yaml文件的操作\test.yaml',mode='r',encoding='utf-8') as file1:
#     data =  yaml.safe_load(file1)
# print(data)
# print(data['dic']['score'][2])

# with open('test.yaml') as file1 :
#     data = yaml.safe_load(file1)
#     print(data)


#读取test.yaml文件，用的是safe_load方法
# with open(file='test.yaml',mode='r') as  yaml_file:
#     yaml_data = yaml.safe_load(yaml_file)
# print(yaml_data)
# print(type(yaml_data))

#写入yaml文件：
dict1 = {'test1':123456}
with open(file='test.yaml',mode='a') as  yaml_file:
    yaml.safe_dump(data=dict1,stream=yaml_file)


