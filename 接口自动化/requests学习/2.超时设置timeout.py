"""
timeout学习，用于处理响应时间长的问题
"""
"""超时设置
在本机网络状况不好或者服务器网络响应太慢甚至无响应时，
我们可能会等待特别久的时间才可能收到响应，甚至到最后收不到响应而报错。
为了应对这种情况，应设置一个超时时间，这个时间是计算机发出请求到服务器返回响应的时间，
如果请求超过了这个超时时间还没有得到响应，就抛出错误。这就需要使用timeout参数实现，单位为秒。

timeout没有默认值
"""


import requests
try:
    res = requests.request(method='get',url='https://www.baidu.com',timeout = 0.01).text
    print(res)
#异常捕获
except:
    print(1111111)
