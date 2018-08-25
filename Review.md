# 复习手册
这是复习所用的笔记，具体代码详见Notebook.py。

## Chapter 2
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
对象（Object）、类（Class）、封装、继承、方法、构造函数、析构函数。
#### ii.定义和使用类
声明类、定义类的对象、成员变量、构造函数__init__、析构函数__del__。

特殊规则：__xxx__表示系统定义名字，__xxx表示类中私有变量名。

#### iii.类的静态成员
静态变量、静态方法。

类名访问静态变量和对象名访问结果互不干扰。
静态方法无法访问实例变量，但可通过类名引用静态变量。

#### iv.类方法
类方法可以调用类方法，无法访问实例变量，但可通过cls访问静态变量。

#### v.isinstance()函数
isinstance(对象名, 类名或类型名)

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

## Chapter 3 常用Python语句
知识要点：赋值语句、循环语句、条件分支语句、异常处理语句。
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
while语句、for语句、continue语句、break语句

### 3.异常处理语句
try-except语句。

不用记，用时查。

## Chapter 4 Python函数
### 1.声明和调用函数
声明：def语句。
### 2.参数和返回值
#### i.函数中传递参数
普通参数：参数名。
列表和字典参数：列表会字典名。
定义函数时可设置参数默认值。

**可变长参数**：f(*t)，调用函数时参数个数可变。
**t为字典。

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