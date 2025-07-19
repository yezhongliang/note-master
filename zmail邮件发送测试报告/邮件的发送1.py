# -*- coding: utf-8 -*-
"""
@Time    :2022/8/15 22:23
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
背景：以前做回归测试时候，需要大量的手工操作去做回归测试（这里的回归测试指的是对旧功能的回归）
做完回归测试，需要发送邮件，以前邮件是通过手写的形式发送，效率低，浪费时间多，不方便
解决方案：用自动化做回归测试，减少人力的投入，自动化执行脚本去回归旧功能，执行完旧功能后，自动发送生成的邮件给
对应的领导或者自己，通过查看这些邮件去查看旧功能是否有问题


学习的发送邮件的库：zmail--》第三方库，比较简单，学习成本低。注意：zmail只支持python3
不学习的库：smtplib--》python自带的库，比较难，实现相同的功能，步骤非常繁琐

安装zmail --》pip install zmail
              pip install zmail -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

发送邮件都是通过SMTP服务器来发送的，常见的邮箱服务
SMTP协议来发送的。
网易邮箱：smtp.163.com  端口号：25
QQ邮箱：smtp.qq.com  端口号：25
Foxmail： SMTP.foxmail.com  端口号：25

ssh协议：端口号为22，用于工具对服务器的连接

smtp服务，smtp协议走的默认端口号都是25

"""




























