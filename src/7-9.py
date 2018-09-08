# -*- coding: UTF-8 -*-

import sys
from poplib import POP3
import socket
from getpass import getpass

# POP3服务器
POP3SVR = 'pop3.sina.com'
username = input("输入Email：")
password = getpass("输入密码：")
try:
    recvSvr = POP3(POP3SVR)
    recvSvr.user(username)
    recvSvr.pass_(password)
    # 获取服务器上信件信息，返回是一个列表，第一项是邮件数，第二项是字节数。
    ret = recvSvr.stat()
    print ret
    # 退出
    recvSvr.quit()
except (socket.gaierror, socket.error, socket.herror) as e:
    print e
    sys.exit(1)