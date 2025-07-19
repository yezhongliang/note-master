"""
requests_study
"""
"""
学习一下requests的SSL设置,一般是用来处理请求https的请求
根据参数verify设置，verify参数默认是True，可以修改成为False，但是会有警告
解决警告的办法1：自己封装日志级别，把警告的级别不显示

解决告警的办法2： disable_warnings
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)


"""

import requests
import yaml
with open('headers.yml') as file:
    headers_data = yaml.safe_load(file)

headers = headers_data
url ='https://yaodr.sinohealth.com/api/v1/login/login'
method = 'post'
params_data = {"login":"15521048080","password":"123456"}
response = requests.request(method=method,
                            url=url,
                            params=params_data,
                            verify=False,
                            headers=headers).json()
print(response)

