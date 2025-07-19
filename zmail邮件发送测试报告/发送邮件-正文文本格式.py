# -*- coding: utf-8 -*-
"""
@Time    :2022/8/15 22:43
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""zmail发送邮件：主题+文本格式正文
导包  import zmail
邮件内容：包含：主题（subject）、正文（content_text）-文本格式
发件人信息包含：发件人账号，密码（授权码）ojyvzgzggshfbbia
    如何获取授权码：QQ邮箱-设置-账户-POP3设置并开启，选择短信验证
    授权码每次重新打开设置后会重置，如果不重新打开设置，授权码则一直不变
    
创建zmail发送邮件的服务步骤：
    1.声明发送人：需要发送人的QQ邮箱号和授权码（授权码在设置里面拿取）
    2.声明收件人：收件人的QQ邮箱号
    3.z_server = zmail.server(username,password)
        收件人信息包含：收件人地址，邮件内容
    4.发送邮件：z_server.send_mail(recipients,mail)
        群发邮件，收件人地址卸载一个列表中，多个收件人以逗号隔开
"""

import  zmail


# 授权码：pdaodhoxmmnlbcei

#发件人，需要填写邮箱以及授权码，发件人需要用元组数据类型来存储
sender = ('822703304@qq.com','pdaodhoxmmnlbcei')

#收件人,单个接收人就用字符串接收，多个接收人就用列表来接收
# receiver = ''
#发送给多个收件人
receiver=['924993987@qq.com','2493549806@qq.com']

#邮件内容：主题+正文，需要用字典来存储，键不能乱写哦，有固定用法
# subject:是邮件的主题
# content_text：是邮件的正文内容
msg = {
    'subject':'今天星期二，学习一下zmail发送邮件',
    'content_text':'发送给两位同学的正文内容'
        }

#发送邮件
    #发送邮件的准备1：创建zmail发送邮件服务
# email = zmail.server(sender) #看源码，需要传两个值运行这条会报错
z_server = zmail.server(sender[0],sender[1])


# email = zmail.server(*sender)  # *星号 有解包的作用，解包的意思就是把一个元组里面的数据拆开来传值

#准好好了，发送邮件
z_server.send_mail(recipients=receiver,mail = msg)



#运行后，有的邮件会被退回来，因为敏感词和多次发送的原因

