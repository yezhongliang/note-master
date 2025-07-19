# -*- coding: utf-8 -*-
"""
@Time    :2022/8/15 23:29
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""
                                    pdaodhoxmmnlbcei
zmail发送邮件：主题+文本格式正文
导包  import zmail

邮件内容：包含：主题（subject）、正文（content_text）-文本格式、attachments（附件）
发件人信息包含：发件人账号，密码（授权码）

    如何获取授权码：QQ邮箱-设置-账户-POP3设置并开启，选择短信验证
    
创建zmail发送邮件的服务步骤：
    1.声明发送人：需要发送人的QQ邮箱号和授权码
    2.声明收件人：收件人的QQ邮箱号
    3.z_server = zmail.server(username,password)
        收件人信息包含：收件人地址，邮件内容
    4.发送邮件：z_server.send_mail(recipients,mail)
        群发邮件，收件人地址卸载一个列表中，多个收件人以逗号隔开

UI自动化实际的一个流程：
背景：为什么要做自动化？自动化的目的是什么？怎么去实施？
为什么要做自动化？
    为了提高回归测试的效率，以及在无人值守的时间里面去自动运行自动化脚本对环境进行巡检
    
怎么去实施？
    我们写好脚本之后，把脚本上传到代码仓库（github/gitlab），
    然后通过jenkins这个工具，自动定时去构建这些脚本，
    然后执行完脚本之后，自动生成测试报告，并且自动把测试报告发送到指定的邮箱里面去。
"""

# import  zmail
# def send_mail1():
    #发件人
    # sender = ''

    #收件人
    # receiver = ''

    #发送给多个收件人
    #receiver=['收件人1','收件人2','收件人3']

    #邮件内容：主题+正文，需要用字典来存储，键不能乱写哦，有固定用法
    # msg = {
    #     'subject':'邮件主题：测试zamil发送邮件是否成功',
    #     'content_text':'这是正文',
    #     'attachments':[
    #
    #                     ]
    #         }
    #添加两个附件attachments的值用列表的形式去存附件:'attachments':[附件1，附件2]

    #发送邮件
        #发送邮件的准备1：创建zmail发送邮件服务

    # email = zmail.server(*sender)  #*星号有解包的作用
        #准好好了，发送邮件
    # email.send_mail(receiver,msg)  #看源码，需要传两个值
    #
    # #运行后，有的邮件会被退回来，因为敏感词和多次发送的原因
    #
    #
    # #练习：把发送邮件的功能封装成为一个类，便于以后调用。
    # #要求实例化对象和调用实例方法的时候，不需要传值

import zmail
from 文件的操作.ini文件的操作.ini文件介绍 import ini_utils
def send_mail_utils():
    z_server = zmail.server(username=ini_utils('zmail','sender_username'),
                            password=ini_utils('zmail','password'))

    msg = {
        'subject':'邮件主题：测试zamil发送邮件是否成功',
        'content_text':'这是正文内容，我要测试一下到底行不行！！！',
        'attachments':r'D:\TestTool\project_for18\接口自动化\结合unittest运行两个接口\report18.html'}

    z_server.send_mail(recipients=[ini_utils('zmail','receiver1'),ini_utils('zmail','receiver2')],
                       mail=msg)

send_mail_utils()




