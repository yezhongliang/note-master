""""""
"""
可以用来处理UI自动化的时候，弹出来登录的操作
"""
import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost:8080/manager/html',auth=HTTPBasicAuth('admin','123456'))
print(r.status_code)

