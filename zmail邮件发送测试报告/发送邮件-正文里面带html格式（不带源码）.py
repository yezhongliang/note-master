# -*- coding: utf-8 -*-
"""
@Time    :2022/8/15 23:30
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
@Time    :2022/8/15 23:06
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""zmail发送邮件：主题+html正文
导包  import zmail
邮件内容：包含：主题（subject）、正文（content_text）-文本格式
发件人信息包含：发件人账号，密码（授权码）nukmkroaoqctbcdb
    如何获取授权码：QQ邮箱-设置-账户-POP3设置并开启，选择短信验证
创建zmail发送邮件的服务：z_server = zmail.server(username,password)
收件人信息包含：收件人地址，邮件内容
发送邮件：z_server.send_mail(recipients,mail)
群发邮件，收件人地址卸载一个列表中，多个收件人以逗号隔开
"""
import  zmail

#发件人
sender = ('822703304@qq.com','ojyvzgzggshfbbia')

#收件人
receiver = ['2213929113@qq.com','3050671343h@gmail.com','1602663559@qq.com','2780226055@qq.com']

#邮件内容：主题+正文，需要用字典来存储，键不能乱写哦，有固定用法
with open(r'D:\TestTool\project_for12\zmail邮件发送测试报告\report.html',mode='rb') as file1:
    content = file1.read()

msg = {
    'subject':'邮件主题：好看的html格式',
    'content_html':content
}

#发送邮件
    #发送邮件的准备1：创建zmail发送邮件服务
# email = zmail.server(sender) #看源码，需要传两个值运行这条胡报错
# email = zmail.server(sender[0],sender[UI自动化第一天])
email = zmail.server(*sender)  #*星号有解包的作用
    #准好好了，发送邮件
email.send_mail(receiver,msg)  #看源码，需要传两个值

#运行后，有的邮件会被退回来，因为敏感词和多次发送的原因
