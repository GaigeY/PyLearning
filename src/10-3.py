# -*- coding: UTF-8 -*-
import socket
print '【10-3】演示使用sendto()函数发送数据报的方法。'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 创建UDP SOCKET
port = 80001             # 服务器端口
host = '192.168.0.101'  # 服务器 IP
while True:
    msg = input()       # 接受用户输入
    if not msg:
        break           # 发送数据
    s.sendto(msg.encode(),(host,port))
s.close()