# -*- coding: UTF-8 -*-
# The example is failed. Do not run it.

import sys
import smtplib
import socket
from getpass import getpass

class SMTPHeloError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

if len(sys.argv) < 4:
    print "[*]usage:%s server fromaddr tooddr " % sys.argv[0]

server = sys.argv[1]    # 第一个参数是SMTP服务器
fromaddr = sys.argv[2]  # 第二个参数是发件人地址
toaddr = sys.argv[3]    # 第三个参数是收件人地址

# 邮件内容
message = """
To: %s
From: %s
Subject: Test Message from 7-8.py

Hello, this is a simple SMTP_mail example.
""" % (toaddr, fromaddr)

def auth_login():
    username = input("Input your username:")
    password = getpass("Input password:")
    try:
        s = smtplib.SMTP(server)    # 连接到服务器
        print s.ehlo()
        code = s.ehlo()[0]          # 返回服务器的特性
        usesesmtp = 1
        if not (200 <= code <= 299):  # 200-299都是正确的返回值
            usesesmtp = 0
            code = s.ehlo()[0]
            raise SMTPHeloError(code)
        if usesesmtp and s.has_extn('size'):
            print u"允许发送文件的大小为" + s.esmtp_features['size']
            if len(message) > int(s.esmtp_features['size']):
                print u"邮件内容太大，程序中断。"
                sys.exit(2)

        if usesesmtp and s.has_extn('auth'):
            print u"\r\n使用认证连接。"
            try:
                s.login(username, password)
            except smtplib.SMTPException as e:
                print u"认证失败：",e
                sys.exit(1)
        else:
            print u"服务器不支持认证，使用普通连接。"
        s.sendmail(fromaddr, toaddr, message)   # 如果支持认证则输入用户名密码进行认证，否则使用普通形式进行传输
    except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
        print u"***邮件成功发送***"
        print e
        sys.exit(1)
    else:
        print u"***邮件成功发送***"