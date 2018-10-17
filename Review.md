# 知识手册
这是学习过程中整理的笔记，用于复习和索引。

概念解释和具体代码详见[NoteBook](src/NoteBook.py)。

**Warning**：本文档用到HTML代码，不受Github支持。如需查看目录、表格等，请下载使用本地编译器查看。
[toc]
## Chapter2 Python语言基础
### 1.常量和变量
#### i.常量
包括数字、字符串、布尔值、空值。可定义命名常量，Python中很复杂。
#### ii.数和字符串
##### a.数
数分为整数形（int）、长整数型（long）、浮点数型（float）、布尔型（bool）和复数型（complex）5种。
##### b.字符串
字符串是字符组成序列。
巧用单引号和双引号。
知识点：转义符号、三引号、Unicode字符串、自然字符串、子字符串。
##### c.空值
None，很特殊。
#### iii.变量
命名规则：字母或下划线开头，包含字母、数字或下划线，不包含空格、减号。
不能使用关键字定义。

知识点：变量的传递和地址：id()

### 2.数据类型
五种数据类型：简单数据类型、列表、元组、字典和集合。
#### i.简单数据类型
简单数据类型包括数字、字符串。

要求掌握的函数：

int()、long()、float()；计算字符串表达式：eval()。

str()、可打印字符串repr(obj)；ASCII码的两个函数：chr(整数)、ord(字符)；转十六进制字符串：hex(整数)；转八进制字符串：oct(整数)。

#### ii.列表
[A,'b',...]
##### a.打印列表：print(List)
##### b.获取长度：len(List)
##### c.访问元素：List[index]
##### d.添加元素：List.append(ele)，List.insert(index,ele)，List1.extend(List2)
##### e.合并列表：List3 = List1 + List2
##### f.删除元素：del List[index]
##### g.索引元素：List.index[value]
##### h.遍历列表：for i in range(len(List))，for index,value in enumerate(List)
##### i.排列列表：升序List.sort()，反序List.reserve()
##### j.产生列表：range(start,end)，结果[start,end)
##### k.多维列表：[[A,b,...],...]，List[index1][index2]

#### iii.元组
(A,'b',...)
元组不可更改。
##### a.获取长度：len(Tuple)
##### b.访问元素：Tuple(index)
##### c.遍历元组：for i in range(len(Tuple))，for index,value in enumerate(Tuple)
##### d.排序元组：巧用函数list()、tuple()

#### iv.字典
{'A':'a', 'B':'b', ...}
##### a.打印字典：print(Dict)
##### b.获取长度：len(Dict)
##### c.访问元素：Dict[key]
##### d.添加元素：Dict[key] = value（有则改之，无则加勉）
##### e.合并字典：Dict1.update(Dict2)
##### f.删除元素：Dict.pop(key)（返回值并删除）
##### g.判断元素：key in Dict
##### h.遍历字典：for key in Dict.keys()，for value in Dict.values()
##### i.清空字典：Dict.clear()
##### j.字典嵌套：Dict[key1][key2]

#### v.集合
set(['A','b',...]);
frozenset({'A','b',...})

##### a.获取长度：len(Set)
##### b.访问元素：for e in Set
##### c.添加元素：Set.add(ele)
##### d.删除元素：Set.remove(ele)
##### e.清空集合：Set.clear()
##### f.判断元素：ele in Set
##### g.遍历元素：for e in Set
##### h.子集和超集：比较符号
##### i.集合运算：并集|，交集&，差集-，对称差分^、S1.symmetric_difference(S2)

### 3.运算符和表达式
#### i.运算符
##### a.算术运算符
`+, -, *, /, %, **, //.`

##### b.赋值运算符
`=, +=, -=, *=, /=, %=, **=, //=.`

##### c.位运算符（二进制）
`&, |, ^, ~, <<, >>.`

##### d.比较运算符
`==, !=, <>, <, >, <=, >=`

##### e.逻辑运算符（Bool型）
`and, or, not`

##### f.字符串运算符
`+, *, [], [,], in, not in,r/R.`

##### g.运算符优先级
记不住的=。=

#### ii.表达式

### 4.Python对象
#### i.基本概念
`对象（Object）、类（Class）、封装、继承、方法、构造函数、析构函数。`
#### ii.定义和使用类
声明类、定义类的对象、成员变量、构造函数__init__、析构函数__del__。

特殊规则：__ xxx __ 表示系统定义名字，__ xxx表示类中私有变量名。

#### iii.类的静态成员
静态变量、静态方法。

类名访问静态变量和对象名访问结果互不干扰。
静态方法无法访问实例变量，但可通过类名引用静态变量。

#### iv.类方法
类方法可以调用类方法，无法访问实例变量，但可通过cls访问静态变量。

#### v.isinstance()函数
isinstance(对象名, 类名或类型名)

判断对象是否属于指定类或类型。

#### vi.类的继承和多态（没搞清楚）
class B(A)，B继承A的属性和函数。

抽象类和多态没搞清楚。

#### vii.对象的序列化
import pickle
##### a.将对象序列化成字符串
ListB = pickle.dumps(ListA)

反序列化：
ListA = pickle.loads(ListB)

##### b.将对象序列化到文件
p = open('data.pkl','wb');
pickle.dump(List, p);
List = pickle.load(p);

#### viii.对象的赋值
新对象名 = 原有对象名

## Chapter3 常用Python语句
知识点：赋值语句、循环语句、条件分支语句、异常处理语句。
### 1.赋值语句
#### i.解包
x,y,z = 序列

序列包括字符串、列表、元组。

#### ii.链式赋值
x = y = z = value

### 2.控制语句
#### i.条件控制
`if,else,elif.`
#### ii.循环语句
while语句、for语句、continue语句、break语句。

### 3.异常处理语句
try-except语句。

不用记，用时查。

## Chapter4 Python函数
### 1.声明和调用函数
声明：def语句。
### 2.参数和返回值
#### i.函数中传递参数
普通参数：参数名。
列表和字典参数：列表会字典名。
定义函数时可设置参数默认值。

**可变长参数**：f(*t)，调用函数时参数个数可变，t的格式为元组。
f(**t)类似，t的格式为字典。

#### ii.函数的返回值
return语句，可以返回值、列表或字典。

### 3.全局变量和局部变量
全局变量全局有效，局部变量定义的函数中有效，冲突则局部优先。

### 4.常用Python内置函数
#### i.数学运算函数
`abs,pow,round,divmod`

round：四舍五入；
divmode：商和余数。

#### ii.字符串处理函数
##### a.大小写变换
##### b.输出对齐方式
##### c.搜索和替换
##### d.分割和组合
##### e.字符串判断

### 5.函数式编程
**lambda表达式**
map函数
filter函数
reduce函数
zip函数

### 6.闭包和递归
### 7.迭代器和生成器

## Chapter5 Python模块
模块以.py形式储存，保存在Python主目录下的Lib目录中。

import 模块名
### 1.常用模块
#### i.sys模块
##### a.系统平台：sys.platform
##### b.命令行参数：python command.py a b c
##### c.退出应用：sys.exit(n)，0无误，1有误。
##### d.系统编码：sys.getdefaultencoding()
##### e.搜索路径：sys.path
添加路径：sys.path.append(指定目录)

#### ii.platform模块
操作系统、Python版本等信息，详见Notebook文件。

#### iii.数学相关
math模块、random模块、decimal模块、fractions模块。

四个表格，待补充。

#### iv.time模块
时间信息。
##### a.当前时间戳：time.time()
##### b.时间戳转换为当前时区：time.localtime()
##### c.格式化输出时间戳：time.strftime(格式化字符串,struct_time)
格式化字符串的符号规则见Notebook。
##### d.直接获取当前时间：time.ctime()

### 3.自定义和使用模块

## Chapter6 I/O编程
### 1.输入和显示数据
输入数据 = input(提示字符串)

print函数的用法：
输出字符串和格式化输出数字。

十六进制整数：%x。
八进制整数：%o。

浮点数用法：%总长度.小数位数f，总长度包含小数点。

### 2.文件操作
#### i.打开文件
文件对象 = open(文件名, 访问模式, buffering)
#### ii.关闭文件
f.close()
#### iii.读取内容
str = f.read([b]);

按行读取：
list = f.readlines();
str = readline();

in关键字
in关键字按行遍历：
for line in f:
#### iv.写入数据
##### a.写入内容：f.write()
##### b.写入序列：f.writelines(seq)
#### v.文件指针
##### a.指针位置：pos = f.tell()
##### b.移动指针：f.seek(offset,where)
#### vi.截断文件
f.truncate([size]);丢弃后面内容。
#### vii.文件属性
fileStats = os.stat(文件路径和文件名)
#### viii.shutil模块
##### a.复制文件：shutil.copy(src, dst)
##### b.移动文件：shutil.move(src, dst)
#### ix.os模块
##### a.删除文件：os.remove(src)
##### b.重命名文件：os.rename(src, dst)

### 3.目录编程
os模块应用
##### a.获取当前目录：os.getcwd()
##### b.获取目录内容：os.listdir(path)
##### c.创建目录：os.mkdir(path)
##### d.删除目录：os.rmdir(path)

## Chapter7 使用Python程序操作计算机
os.system("str")控制计算机，"str"为CMD命令语句。

被SMTP和POP3邮件部分搞得很绝望，文件夹里有失败的代码。

## Chapter8 数据结构
Python内置数据结构：列表、元组、字典等。

Python拓展数据结构：栈、队列、树、链表等。

数据结构是数据的组织方式、存储方式；算法指运算方法。数据结构是算法的基础。

### 1.栈
栈的特性：后进先出（LIFO）。
常用操作：
##### a.检查空栈：isEmpty()
##### b.进栈操作：push()
##### c.出栈操作：pop()
##### d.返回栈顶：peek()
##### e.检查大小：size()

### 2.队列
队列特性：先进先出（FIFO）。
常用操作：
##### a.检查空队：isEmpty()
##### b.入队操作：enqueue()
##### c.出队操作：dequeue()[=pop(0)]
##### d.返回队首：head()
##### e.返回队尾：tail()
##### f.检查大小：length()

### 3.树
非线性，共有元素节约空间。

二叉树是**有序树**，顺序存储和链式存储。数据域、左子树域和右子树域。

遍历方法：先序遍历、中序遍历、后序遍历。

### 4.链表
非连续、非顺序的存储方式。

数据域和指针域。

单向链表、单向循环链表、双向链表、双向循环链表。

常用操作：
##### a.判断空链：isEmpty()
##### b.链首添加元素：add()
##### c.链尾添加元素：append()
##### d.寻找元素位置：index()
##### e.移除元素：remove()
##### f.插入元素：insert()
##### g.遍历链表：travel()

## Chapter9 多任务编程
### 1.多进程编程
进程的概念：指令的实际运行体。

进程的状态：被创建、就绪、运行、阻塞、挂起、终止。
### 2.进程编程
创建进程的模块：subprocess, win32process, ctypes。
#### i.subprocess模块
##### a.运行进程：subprocess.call([可执行程序, 参数])
##### b.创建进程执行命令：subprocess.Popen()
#### ii.win32process模块
##### a.创建进程：win32process.CreatProcess()
#### iii.kernel32
创建对象：kernel32 = windll.kernel32
##### a.枚举进程：kernel32.CreatToolhelp32Snapshot()
##### b.首个进程：kernel32.Process32First(hSnapshot, byref(fProcessEntry32))
##### c.下个进程：kernel32.Process32Next(hSnapshot, byref(fProcessEntry32))
### 3.线程编程
线程是进程的子集，进程内部线程资源共享。

线程的状态：初始化、就绪、延迟就绪、备用、运行、等待、过渡、终止。
#### 关键：threading模块！
##### i.创建线程：t = threading.Thread()
##### ii.守护线程：t.setDaemon()
##### iii.阻塞线程：t.join()
##### iv.指令锁
###### a.创建指令锁：lock = threading.Lock()
###### b.申请指令锁：lock.acquire([timeout])
###### c.释放指令锁：lock.release()
##### v.可重入锁
###### a.创建可重入锁：lock = threading.RLock()
###### b.申请可重入锁：lock.acquire()
###### c.释放可重入锁：lock.release()
##### vi.信号量
###### a.创建信号量：s = threading.Semaphore(value)
###### b.申请信号量：s.acquire()
###### c.释放信号量：s.release()
##### vii.事件
###### a.创建事件：e = threading.Event()
###### b.标记True：e.set()
###### c.标记False：e.clear()
###### d.标记阻塞：e.wait()
##### viii.定时器（Thread的派生类）
###### a.创建定时器：timer = threading.Timer(t,f)
###### b.启动定时器：timer.start()
## Chapter10 Python网络编程
### 网络通信模型和TCP/IP协议簇
#### OSI参考模型
开放系统互连参考模型（Open System Interconnection Reference Model）简称为OSI参考模型。分为7个层次：
- 物理层 Physical Layer
- 数据链路层 Data Link Layer
- 网络层 Network Layer
- 传输层 Transport Layer
- 会话层 Session Layer
- 表示层 Presentation Layer
- 应用层 Application Layer

低三层：网络通信链路；高四层：端到端数据通信。每层为数据包加一个头部。

不是所有数据都要经过7层，比如同一网段二层通信、路由器间的三层通信等。

信息交换单元称为协议数据单元（PDU）。
| OSI参考模型中的层次 |   PDU的特定名称   |
|:-------------------:|:-----------------:|
|       传输层        | 数据段（Segment） |
|       网络层        | 数据包（Packet）  |
|     数据链路层      |  数据帧（Frame）  |
|       物理层        |    比特（Bit）    |
#### TCP/IP协议簇体系结构
TCP/IP协议簇规范了网络设备之间数据往来的格式和传送方式。包含网络接口层、网络层、传输层和应用层。

<div style="text-align:center">
<table>
  <tr>
    <td>OSI参考模型</td>
    <td colspan="2">TCP/IP协议簇</td>
  </tr>
    <tr>
      <td>应用层</td>
      <td rowspan="3">应用层</td>
      <td rowspan="3">FTP,Telnet,SMTP,SNMP,NFS</td>    
    </tr>
  <tr>
    <td>表示层</td>
  </tr>
  <tr>
    <td>会话层</td>
  </tr>
  <tr>
    <td>传输层</td>
    <td>传输层</td>
    <td>CTP,UDP</td>    
  </tr>
  <tr>
    <td>网络层</td>
    <td>网络层</td>
    <td>IP,ICMP,ARP,RARP</td>    
  </tr>
  <tr>
    <td>数据链路层</td>
    <td>网络接口层</td>
    <td>Ethernet 802.3, Token Ring 802.5, X.25, Frame reley, HDLC, PPP</td>    
  </tr>
  <tr>
    <td>物理层</td>
    <td colspan="2">未定义</td>    
  </tr>
</table>
</div>

### Socket编程
#### 工作原理
- 客户端需要了解服务器的地址和应用程序端口
- 服务器应用程序必须早于客户端应用程序启动
- 客户端申请发送数据，服务器必须有足够时间响应
- 双方必须使用相同的通信协议
- 通信过程中，物理网络必须保持畅通
- 通信结束之前双方都可以中断连接
<div style="text-align:center">
<table align:"center">
  <caption>Socket编程的层次结构<caption>
  <tr><td colspan="2">应用层</td></tr>
  <tr><td colspan="2">Socket开发接口</td></tr>
  <tr><td colspan="2">传输层</td></tr>
  <tr>
    <td>TCP</td>
    <td>UDP</td>
  </tr>
  <tr><td colspan="2">网络层 IP</td></tr>
  <tr><td colspan="2">驱动</td></tr>
  <tr><td colspan="2">物理层</td></tr>
</table>
</div>
#### 基于TCP的Socket编程
##### a.创建套接字：s = socket.socket(familly, type)
##### b.绑定地址：s.bind(address)
##### c.监听状态：s.listen(backlog)
##### d.等待请求：connection, address = s.accept()
##### e.接收数据：buf = s.recv(size)
##### f.发送数据：s.send(buf)
##### g.关闭套接字：close()
#### 基于UDP的Socket编程
##### a.发送数据：s.sendto(data, (addr, port))
##### b.接收数据：data, addr = s.recvfrom(bufsize)
