# -*- coding: UTF-8 -*-
import socket

print '【10-1】一个使用Socket进行通信的简易服务器。'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象

sock.bind(('localhost', 8001))  # 绑定到本地的8001端口
sock.listen(5)  # 在本地的8001端口上监听，等待连接队列的最大长度为5
while True:
    connection, address = sock.accept()
    try:
        connection.settimeout(5)
        buf = connection.recv(1024).decode('utf-8')  # 接收客户端的数据
        if buf == '1':
            connection.send(b'welcom to server!')
        else:
            connection.send(b'please go out!')
    except socket.timeout:
        print "time out"
    connection.close()