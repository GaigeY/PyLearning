#PyBlueZ模块
Python对蓝牙的支持是通过PyBlueZ模块实现的。

网上关于蓝牙的中文学习资料过少，所以我不得不求助于外文网站。本文是蓝牙学习所整理的笔记。

> 返回Review文件[请点这里](Review.md)。

PyBlueZ模块主要是TCP协议传输。UDP可百度搜索：Python bluetooth UDP
[toc]
## 函数列表
##### 查找设备：bluetooth.discover_devices(duration, lookup_name, flush_cache, lookup_class)
返回的是以(addr, name)为一组的序列。
##### 访问设备：find_service(address)
address是地址，address=None意味着访问所有设备信息。每个元字典的key为：name、host、description、provider、protocol、port、service-classes、profiles、service-id。
##### RFCOMM连接：s=BluetoothSocket(RFCOMM)
RFCOMM连接的函数和socket的大体对应。
###### 绑定地址：s.bind()
###### 监听状态：s.listen()
###### 获取端口：s.getsockname()[]
###### 获取终端信息：s.accept()
###### 终端连接：s.connect((host,port))
###### 传输数据：s.send(data)
###### 开放连接：advertise_service(s)
##### 获取本地地址：bluetooth.read_local_bdaddr()
## 实战经验
实战Blog地址：“src\PyBlueZ\Python and Bluetooth.html”
请下载并在本地查看。
