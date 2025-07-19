# -*- coding: utf-8 -*-
"""
@Time    :2022/8/22 17:17
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""
"""
公司实战中处理验证码的方法：（UI自动化的拦路虎：验证码）
验证码的类型：拖拉到一个缺口上、文字顺序、寻找同样类型的图片、加减乘除
1.跟开发沟通，让他设置一个万能的验证码（前后端开发）
    验证码：选数字的、拖拉拽、选中文
    例子：注册功能，输入手机号15521048080后，获取验证码，然后开发写死一个验证码888888
    
2.跟开发沟通，让他屏蔽掉（测试环境或验收环境屏蔽）验证码的验证（前后端开发）

3.获取验证码然后对验证码进行处理后再识别
    3.1.OCR技术（识别率较低导致成功率较低，但是是正常的，图像识别技术-这些技术大公司会提供）
        腾讯、百度
    3.2.cookie的方式去验证 --实现免登录
        网站登录后都会有一个cookie，用户每次访问都需要带上对应cookie才能知道你是谁
    
4.直接将某些包含验证码的用例给去掉（这就是为什么UI自动化难开展，覆盖率不高的其中一个原因）
"""

# cookie有一定的局限性：
#     1.大型网站验证机制比较特殊，这种特殊的情况下可能无法实现登录的操作
#     2.如果登录的用户数据不同，实现不方便
#     3.cookie有时效性，会过期，具体按照公司的规定来

#使用百度网盘演示cookie实现免登录，前提：手动先登录
# driver.get_cookies()  #获取cookie
# driver.add_cookie(cookie_dict)  #写入cookie

from selenium import  webdriver
from time import sleep

driver = webdriver.Chrome()   #登录（手动登录一次）--网站自动保存cookie--我们去获取cookie，然后用这个cookie去登录，直接跳过账号以及密码
driver.get('https://pan.baidu.com/')
sleep(60)
#获取cookie
cookie = driver.get_cookies()
print(cookie)  #输出的是一个列表类型，要把列表转换成为字典的数据类型
#写入cookie
cookies = [{'domain': '.baidu.com', 'expiry': 1672285355, 'httpOnly': True, 'name': 'ab_sr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1.0.1_MTlmNWRkNjBkNGNmNGM2MDIyMzg1MjQ5MGU0ZWZhOWY0N2FkOGIyNTQwMzIzMjNhNmZiNzg3MjYyOWM0ZTgzNTBjNjA5OGU2OTQzNGQzYWRkNTE3OGYwOTA1MDg2MjE2MGZlMjQ2ZDUzM2NiY2NjZmVkNzQyYTExMDk2MTM2YTAyZmI1ZjczNDAzYjlkNjJkMWIwMjE2YjFiN2ZmYjA4NjY3MTM3ZjBlOGUzNTczY2MwMDgyZjU4ZGMyYWUyMTc5'}, {'domain': '.pan.baidu.com', 'expiry': 1674956552, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '7c3886acda85c34a97d47c9e9166087bf17dd2fc48a6bd339209fc3bdddbf0fc'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'secure': False, 'value': 'fALZual_o_odXlahPvMviTqb'}, {'domain': '.baidu.com', 'expiry': 1706838151, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '11NExRYUNvTUVmbnN-RHZMMmlIWnFsZFUwTGZ-a1Y0VGxkOVlsbkNQMkVmZFJqSUFBQUFBJCQAAAAAAAAAAAEAAAA2e5WNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAITwrGOE8KxjYy'}, {'domain': '.pan.baidu.com', 'expiry': 1672364553, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '14993107159512809606%3ACU2JWesajwAsm%2FB3S%2Bbc6XlibiKzYuqj3qZ5gZSyz8bdXU7GPexxBUci2O0YbEjpZCwIlIAmj0qdrygk2hUCKKKK%2FFH5WUxXs3ltqdL44oL59Pi4d3uHw3ZNBoZ8i0CTW8pfgMw2m%2FrQ8rlESRQE3CZTnz2RR6t%2BZFCUk453j8DrbkBUnMiFfw%3D%3D'}, {'domain': '.baidu.com', 'expiry': 1706838151, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': '11NExRYUNvTUVmbnN-RHZMMmlIWnFsZFUwTGZ-a1Y0VGxkOVlsbkNQMkVmZFJqSUFBQUFBJCQAAAAAAAAAAAEAAAA2e5WNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAITwrGOE8KxjYy'}, {'domain': '.baidu.com', 'expiry': 1703814125, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2A108AF77BE9277F2B492DF64AE04782:FG=1'}, {'domain': 'pan.baidu.com', 'expiry': 1674870154, 'httpOnly': False, 'name': 'ndut_fmt', 'path': '/', 'secure': False, 'value': '4621F02E09F1DA34F302A41CED1FCCB7CAAA0259761590233326954CA2302864'}, {'domain': '.baidu.com', 'expiry': 1674870125, 'httpOnly': True, 'name': 'newlogin', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1703814125, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '2A108AF77BE9277F2B492DF64AE04782:FG=1'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'XFCS', 'path': '/disk', 'secure': False, 'value': '5158E20479D843C41462CD302A70F3917034DC12C3C85E98AF90E2469242348A'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'XFI', 'path': '/disk', 'secure': False, 'value': 'aa72919b-3f58-5bd8-fae5-b8df14e725a4'}]

for i in cookies:
    driver.add_cookie(i)
#访问网站
driver.get('https://pan.baidu.com/')
sleep(10)
driver.quit()

















