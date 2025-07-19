# -*- coding: utf-8 -*-
"""
@Time    :2022/8/28 23:56
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

# 补充：cookie、session、token的区别
"""json的数据格式
1.json是什么？JavaSript对象和数组 的字符串表示法
    java script object notation，json数据是一种轻量级的数据，
    前后端常用json数据格式来传输数据
    http协议的，基本上都是用的json格式的数据
    jmeter -》json提取器
    
python的字典：
dict1 = {key1:value1,
        key2:value2}
dict1 = {'name':'zhangsan','sex':'男'}

查看好看的json格式：bejson.com


2.json的语法规则：
a.数据在名称/值（键值对中）：{"name":"zs"}
b.数据由逗号分隔：{"name":"zs","age":18}
c.大括号保存对象：{"name":"zs","age":"18"}
d.中括号保存数组:'{"score":[100,200,300]}
字典中的列表 在json中叫做数组
字典中的True在json用true表示
字典中的False在json中用false表示
字典中可以嵌套元组，但是json只能嵌套数组[]
字典中的空表示None,json中的空表示null
json的key只能是字符串

3.json数据如何取值：
    方式1：对象名.key值
    方式2：对象名[key值] --》这个取值方式和字典的取值方式是一样的
    数组的话是和列表一样去取值[索引值]

4.json与python的数据类型对比
    json        key值只能是字符串
                value值可以是字符串、对象、数组，布尔值(true/false)或者null
    dict        key可以是number类型（整数、浮点数、布尔值），字符串
                value值可以是number（整数、浮点数、布尔值(True/False)），字符串、元组、列表、字典
    json的数组和python的列表对比：
    json
    定义：数组可以包含多种数据类型         列表也可以包含多种数据类型
    取值：数组只能通过正向索引取值         列表可以通过正向和反向取值
    切片：数组不支持切片                   列表支持切片
    
5.json与dict的互相转换
导包：import json
json转字典的函数：json.loads
字典转json的函数：json.dumps

6.jsonpath的使用，pip install jsonpath
什么是jsonpath?第一个第三方的模块，常用于提取json里面的数据，常用于接口测试。类似于xpath //*[@id='']
jsonpath的操作符：
$     表示根节点
@     当前节点由过滤谓词处理
*     通配符，代表所有
..    不管任何位置，选择所有符合条件的数据
.     当前路径
"""
#5.json与dict之间的转换

import json #那就json转字典，用的是dumps
#dict转json  dumps
#语法：json.dumps(dict)
# dict1 = {'name':'zhangsan',
#         'age':20,
#         'job':'tester'}
# json_test = json.dumps(dict1)
# print(json_test)
# print(type(json_test))

#json转字典,很多时候，json的数据来源是json文件，需要通过读取json文件里面的数据，再把json内容转换成为字典
# json_data = '{"name":"zhangsan","age":20,"job":"tester"}'
# # print(json_data,type(json_data)) #目前还是json
# dict_data = json.loads(json_data)
# print(dict_data,type(dict_data))


# with open("test.json",mode='r') as json_file:
#   data = json_file.read()
# print(data,type(data))
# dict_data = json.loads(data)
# print(dict_data,type(dict_data))

#6.jsonpath的应用 pip install jsonpath
import jsonpath
json_object = { "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}



import jsonpath
"""
jsonpath的语法：
jsonpath.jsonpath(对象名,'表达式')
"""
# with open('test.json') as file1:
#   data = json.decoder
#   print(data)

"""
提取第二本书的价格
提取所有书的价格
提取所有商品的价格
提取第一本书的价格
提取第一本书的价格和作者
提取出单车的颜色
提取出最后一本书title
"""

import jsonpath

# #提取所有商品的价格,jsonpath.jsonpath(对象,'表达式')

# #提取所有书的价格

# #
# #提取所有商品的价格
# all_prices3 = jsonpath.jsonpath(json_object,'$.store..price')
# print(all_prices3)
#
# 提取第一本书的价格
# first_booke_price = jsonpath.jsonpath(json_object,"$.store.book[0]['price']")
# first_booke_price_2 = jsonpath.jsonpath(json_object,"$..book[0]['price']")
# print(first_booke_price_2)
#提取第一本书的价格和作者
# one_book_price_and_author = jsonpath.jsonpath(json_object,'$.store.book[0].[price,author]')
# print(one_book_price_and_author)

# 1.提取出单车的颜色
# dancheyanse = json_object["store"]["bicycle"]["color"]
# print(dancheyanse,type(dancheyanse))
# danche = jsonpath.jsonpath(json_object,'$..color')
# print(danche,type(danche))

# 2.提取出最后一本书title
# zuihoubooktitle = jsonpath.jsonpath(json_object,'$..book[3].title')
# print(zuihoubooktitle)

# 3.提取所有书的价格
# allbookprice = jsonpath.jsonpath(json_object,'$..book..price')
# print(allbookprice)

# 4提取所有商品的价格
# a = jsonpath.jsonpath(json_object,'$..price')
# print(a)

# 5.提取第一本书的价格
# a = jsonpath.jsonpath(json_object,'$..book[0].price')
# print(a)

# 6.提取第一本书的价格和作者
# a = jsonpath.jsonpath(json_object,'$..book[0].[price,author]')
# print(a)

#所有书的价格
# all = jsonpath.jsonpath(json_object,'$..book..price')
# print(sum(all))


# dict2 = {'yuwen':100,'shuxue':200,'yingyu':300}
#把dict数据转换成为json数据（注意是 json数据的字符串表示法）
# json_data = json.dumps(dict2)
# print(json_data,type(json_data))

#把json数据的字符串表示法的数据转换成为dict
# json_data1 = '{"name":"zhangsan","incoming":9000}'
# dict_data = json.loads(json_data1)
# print(dict_data,type(dict_data))


# 序列化和反序列化？
# 序列化：把对象转换成为文件存储（文件存储：文件其实对于电脑来说就是0101010这些二进制码）
# 反序列化：把文件里面的内容读取出来转换成为对象，用with open的方式读取出来就是反序列化

import json

#json文件的读取的方法
# with open('test1.json',mode='r') as json_file:
#   json_data = json_file.read()
# print(json_data)
#
# dict_data = json.loads(json_data)
# print(dict_data,type(dict_data))

#json文件的清空
# with open('test1.json',mode='w+') as json_file:
#   json_file.truncate()

#json文件的写入：json文件一开始没有内容
dict_data = '{"tester3":"zhangsan"}'
with open('test1.json',mode='a')  as json_file:
  json_file.write(dict_data)

#json文件的写入：json文件一开始有内容，然后追加内容：
#思路：先把json文件里面的内容读取出来，然后把读取出来的内容进行转换成dict，然后把你要新增的
#数据和之前的内容进行拼接，拼接完之后，再转换成为str，再写进去









