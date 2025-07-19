"""
proxies参数 --代理设置
"""
"""
对于某些网站，在测试的时候请求几次，能正常获取内容。
但是一旦开始大规模、频繁地爬取，网站可能会弹出验证码，或者跳转到登录验证页面，
更有甚者可能会直接封禁客户端的IP，导致一定时间内无法访问。
为了防止这种情况，我们需要使用代理来解决这个问题，这就需要用到proxies参数。
"""

import requests

proxies = {
  	#该代理服务器在免费代理网站上得到的，这样的网站有很多
    'http': 'http://161.35.4.201:80',
    'https': 'https://161.35.4.201:80'
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
