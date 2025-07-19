# -*- coding: utf-8 -*-
"""
@Time    :2022/8/30 0:33
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
import requests
import jsonpath
"""
接口关联的意思就是：两个接口之间有关联，下游接口需要上游接口响应体/响应头
里面的数据，如果返回的是json数据的格式，则可以用jsonpath把想要的数据提取出来，
然后用一个变量来接收，然后在下一个接口的请求头或者请求体里面传进去即可。
"""







