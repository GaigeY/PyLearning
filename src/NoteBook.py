# -*- coding: UTF-8 -*-
import const

"""
写在开头：这个Project是我学习Python的笔记，里面有学习笔记和代码实例。
"""
class Chapter2():
    """
    -**2**- Python语言基础
    知识要点：
        常量          变量
        数据类型      简单数据类型转换
        列表          元组
        运算符        集合
        Python对象
    """

    """
    2.1 常量和变量
    常量和变量是程序设计语言的最基本元素，它们是构成表达式和编写程序的基础。
        2.1.1 常量
        2.1.2 Python中数的类型与字符串
        2.1.3 变量
    """

    def Example2_1_1(self):
        """
        2.1.1 常量
        """
        """
        常量一旦定义，不可更改。
        Python无法方便地使用const关键字定义常量，需要使用对象的方法。
        """

        print '【2-1】定义一个常量value，值为5。然后打印它的值。'
        const.value = 5
        print const.value

        print '【2-2】常量绑定后无法更改'
        # const.value = 6

    def Example2_1_2(self):
        """
        2.1.2 Python中数的类型和字符串
        """
        """
        Python常量包括数和字符串两大类
        1.数
        Python中数的类型主要分为整数型（int）、长整数型（long）、浮点数型（float）、布尔型（Bool）和复数型（complex）。
        布尔型即逻辑型，两个常量是True和False
        2.字符串
        字符串常量使用单引号（'）或者双引号（"）括起来，交叉使用。
            （1）转义符号
            特殊字符使用反斜杠（\）作为转义字符。使用情况如下所示：
            
            \n          换行
            \r          回车
            \"          "
            \\          \ 
            \（行结尾） 续行符
            \a          响铃
            \b          退格（Backspace）
            \000        空
            \v          纵向制表符
            \t          横向制表符
            （2）使用三引号
            三引号可以用3*'或者3*"实现。这条注释就是在后者中实现的。
            （3）Unicode字符串
            上述字符串都是处理ASCII码字符，如要在程序中处理中文字符串，则需要使用Unicode字符串。
            Python表示Unicode字符串，前缀u或者U即可。
            （4）自然字符串
            前缀r或者R表示“自然字符串”。在自然字符串中，特殊字符失去意义，所见即所得。
            （5）重复字符串
            Python可以使用*操作符很方便地连续输出多次重复的字符串。使用方法为：
                string*RepeatTime
            （6）子字符串
            Python可以使用[]操作符截取字符串中的子字符串。子字符串的运算方法主要有两种，一种是索引运算法[]，一种是切片运算法[:]。
            索引运算法按索引值截取字符串中指定位置的子字符，使用方法为：
                string[index]
            切片运算法按索引值截取字符串中指定开始位置和截止位置之间的字符串，使用方法如下：
                string[a:b]
            索引值a从0开始。返回从a到b-1的子字符串。a,b的默认值为首尾值。
            find()函数在字符串中查找子字符，函数原型为：
                string.find(a,StartAddress,EndAddress)
            查找成功，返回第一个出现的位置，否则返回-1。
        3.空值
        Python有一个特殊的空值常量None。
        和0及空字符串（""）不同，None表示什么都没有。
        None与任何其他的数据类型比较都永远返回False。
    """
        # ASCII码字符串的应用
        print '我是一个字符串'
        print "我是一个字符串"
        print "it's a dog"
        print '字符串常量使用单引号（\'）括起来'
        print 'I\'m a string'
        print '多行字符串的例子。\
              第一行。\
              第二行。'

        # Unicode字符串
        print u"我是Unicode字符串。"

        # 自然字符串
        print r"Newlines are indicated by \n"

        # 重复字符串
        print "【2-3】重复打印'Hello World!'三次"
        print 'Hello World!\n' * 3

        # 子字符串
        print '【2-4】打印"Hello"的各位置的子字符'
        print 'Hello'[0]
        print 'Hello'[1]
        print 'Hello'[2]
        print 'Hello'[3]
        print "Hello"[4]

        print '【2-5】使用切片法截取"Hello"的子字符串'
        print 'Hello'[:2]
        print 'Hello'[1:4]
        print 'Hello'[2:-1]

    def Example2_1_3(self):
        """
        2.1.3 变量
        """
        """
        变量是内存中命名的储存位置，与常量不同的是变量的值可以动态变化。变量和变量的名字都属于标识符。Python标识符命名规则如下：
            标识符名字的第一个字符必须是字母或下划线（_）；
            标识符名字的第一个字符后面可以由字母、下划线（_）或数字（0~9）组成；
            标识符名字是区分大小写的。也就是说Score和score是不同的。
        Example:_score,Number,number123都是有效的变量名，而123number（数字开头）,my score（空格）,my-score（减号）都是无效的。

        Python的关键字是系统中自带的具备特定含义的标识符。常用的Python关键字有and,elif,global,or,else,pass,break,continue,import,class,return,for,while等。
        在定义常量和变量时不能使用关键字作为变量名或常量名。

        Python的变量不需要声明。
        """
        print '【2-6】定义一个字符串变量a,数值变量b和布尔类型变量c。'
        a = '这是一个常量'
        b = 2
        c = True

        print '【2-7】变量值传递'
        a = "这是一个变量"
        b = a
        print b
        print '\n'
        a = "这是另一个变量"
        print b #对变量a的操作不会影响到b

        """
        使用id()函数输出变量的地址，语法如下：
        id(变量名)
        """

        print '【2-8】用id()函数输出变量地址'
        str1 = "这是一个变量"
        print "变量str1的值是："+str1
        print "变量str1的地址是：%d" %id(str1)
        str2 = str1
        print "变量str2的值是："+str2
        print "变量str2的地址是：%d" %id(str2)
        str1 = "这是另一个变量"
        print "变量str1的值是："+str1
        print "变量str1的地址是：%d" %id(str1)
        print "变量str2的值是："+str2
        print "变量str2的地址是：%d" %id(str2)

    """
    2.2 数据类型
    变量有名字和数据类型两种属性。
    Python的数据类型包括简单数据类型、列表、元组、字典和集合。简单数据类型就是数和字符串。
        2.2.1 简单数据类型转换
        2.2.2 列表
        2.2.3 元组
        2.2.4 字典
        2.2.5 集合
    """

    def Example2_2_1(self):
        """
        2.2.1简单数据类型转换
        """
        """
        Python定义变量时，不需要指定其数据类型，赋值即可决定。
        也可以使用一组函数对常量和变量进行类型转换，以便对它们进行相应的操作。
        1.转换为数字
        可以将字符串常量或变量转换为数字，包括如下的情形：
            （1）使用int()函数将字符串转换为整数，语法如下：
                int(x [,base])
            x是待转换的字符串，参数base为可选参数，指定转换后整数的进制，默认为10进制
            （2）使用long()函数将字符串转换为长整数，语法如下：
                long(x [,base])
            （3）使用float()函数将字符串或数字转换为浮点数，语法如下：
                float(x)
            （4）使用eval()函数计算字符串中的有效Python表达式并返回结果，语法如下：
                eval(str)
            参数str是待计算的Python表达式字符串。
        """
        print '【2-9】简单的类型转换例子'
        a = "1"
        b = int(a) + 1
        print b

        print '【2-10】使用eval()函数的例子'
        a = "1+2"
        print eval(a)
        """
        2.转换为字符串
            （1）使用str()函数将数值转换为字符串，语法如下：
                str(num)
            （2）使用repr()函数将对象转换为可打印字符串，语法如下：
                repr(obj)
            （3）使用chr()函数将一个整数转换为可对应ASCII码的字符，语法如下：
                chr(int)
            （4）使用ord()函数将一个字符转换为对应的ASCII码，语法如下：
                ord(str)
            （5）使用hex()函数将一个整数转换为一个十六进制字符串，语法如下：
                hex(int)
            （6）使用oct()函数将一个整数转换为一个八进制字符串，语法如下：
                oct(int)
        """
        print '【2-11】使用chr()和ord()的例子'
        print chr(65)
        print ord('A')

        print '【2-12】使用hex()和oct()的例子'
        print hex(8)
        print oct(8)

    def Example2_2_2(self):
        """
        2.2.2 列表
        """
        """
        列表（List）是一组有序存储的数据。列表具有如下特性：
            和变量一样，每个列表都有一位表示它的名称。
            一个列表的元素应具有相同的数据类型。
            每个列表元素都有索引和值两个属性，索引是一个从0开始的整数，用于标识元素在列表中的位置；值就是元素对应的值。
        1.定义列表
        下面就是一个列表的定义：
            languagelist = ['C++', 'C#', 'Java', 'Python']
        2.打印列表
        可以直接用print()函数打印列表。
        """

        print '【2-13】列表的定义和打印'
        languagelist = ['C++', 'C#', 'Java', 'Python']
        print languagelist

        """
        3.获取列表长度
        列表长度指列表中元素的数量。可以通过len()函数获取列表的长度：
            len(List)
        4.访问列表元素
        列表由列表元素组成。对列表的管理就是对列表元素的访问和操作：
            List[index]
            index是元素索引，第一个元素是0。
        """

        print '【2-14】访问列表元素'
        print languagelist[0]
        print languagelist[3]

        """
        5.添加列表元素
        可通过append()函数添加列表元素：
            List.append(NewData)
        可通过insert()函数在列表指定位置插入一个元素：
            List.insert(InsertPlace，NewData)
        还可通过extend()函数将一个列表中的每个元素分别添加到另一个列表中：
            List1.extend(List2)
        """

        print '【2-15】通过append()函数添加列表元素'
        languagelist = ['C++', 'C#', 'Java', 'Python']
        languagelist.append('javascript')
        print languagelist
        # Output: ['C++', 'C#', 'Java', 'Python', 'javascript']

        print '【2-16】通过insert()函数添加列表元素'
        languagelist = ['C++', 'C#', 'Java', 'Python']
        languagelist.insert(1,'javascript')
        print languagelist
        # Output: ['C++', 'javascript', 'C#', 'Java', 'Python']

        print '【2-17】通过extend()函数将一个列表元素依次添到另一个列表中'
        languagelist1 = ['javascript', 'Java']
        languagelist2 = ['C++', 'C#']
        languagelist1.extend(languagelist2)
        print languagelist1
        # Output: ['javascript', 'Java', 'C++', 'C#']

        """
        6.合并两个列表
        使用加号可合并列表：
            List3 = List1 + List2
        """

        print '【2-18】合并两个列表'
        languagelist1 = ['javascript', 'Java']
        languagelist2 = ['C++', 'C#']
        languagelist3 = languagelist1 + languagelist2
        print languagelist3
        # Output:['javascript', 'Java', 'C++', 'C#']

        """
        7.删除列表元素
        使用del语句可以删除指定的列表元素：
            del List[index]
        """

        print '【2-19】使用del语句删除列表元素'
        languagelist = ['C++', 'C#', 'Java', 'Python']
        del languagelist[0]
        print languagelist
        # Output:['C#', 'Java', 'Python']

        """
        8.定位列表元素
        使用index()函数获取列表中某个元素的索引：
            List.index(x)
        """

        print '【2-20】使用index()函数'
        languagelist = ['C++', 'C#', 'Java', 'Python']
        print languagelist.index('Java')
        print languagelist.index('Python')
        # Output:2
        # Output:3

        """
        9.遍历列表元素
        通过for语句和range()函数遍历列表索引：
            for i in range(len(list)):
                访问list[i]
        也可以用for语句和enumerate()函数同时遍历列表的元素索引和元素值：
            for i,value in enumerate(list):
                访问i&value
        """

        print '【2-21】for语句和range()函数遍历列表'
        languagelist = ['C++', 'C#', 'Java', 'Python']
        for i in range(len(languagelist)):
            print languagelist[i]

        print '【2-22】for语句和enumerate()函数遍历列表'
        languagelist = ['C++', 'C#', 'Java', 'Python']
        for index,value in enumerate(languagelist):
            print "第%d个元素值是【%s】"%(index,value)

        """
        10.列表排序
        可以按升序、降序、反序重新排列列表元素位置。
        sort()函数实现升序排序：
            List.sort()
        reverse()函数实现反序排序：
            List.reverse()
        降序排序可通过先sort，后reverse实现。
        """

        print '【2-23】使用sort()升序排列'
        list = ['banana', 'apple', 'pear', 'grape']
        list.sort()
        print list

        print '【2-24】使用reverse()降序排列'
        list = ['apple', 'Banana', 'pear', 'grape']
        list.reverse()
        print list

        print '【2-25】对列表进行反序排列'
        list = ['apple', 'banana', 'pear', 'grape']
        list.sort()
        list.reverse()
        print list

        """
        11.产生一个数值递增列表
        使用range()函数产生一个数值递增列表：
            range(start,end)
            start:整数，起始元素值。默认值为0。
            end:整数，结束元素值。
        range()函数返回一个列表，从start到end-1。
        """

        print '【2-26】range()函数产生数值递增列表的应用实例'
        list1 = range(10)
        list2 = range(11,20)
        for index,value in enumerate(list1):
            print "list1的第%d个元素值是【%s】" %(index,value)
        for index,value in enumerate(list2):
            print "list2的第%d个元素值是【%s】" %(index,value)

        """
        12.定义多维列表
        将多维列表视为列表的嵌套。
        """

        print '【2-27~30】二维列表的定义和打印'
        list2 = [["CPU", "Memory"], ["Harddisk","Sound Card"]]
        for i in range(len(list2)):
            print list2[i]
        #打印每一个元素
        for i in range(len(list2)):
            list1 = list2[i]
            for j in range(len(list1)):
                print list1[j]
        #2个索引
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                print list2[i][j]

    def Example2_2_3(self):
        """
        2.2.3 元组
        """
        """
        元组（Tuple）与列表非常相似，它具有以下性质：
        （1）一经定义，元组的内容不能改变。
        （2）元组元素可以储存不同类型的数据，可以是字符串、数字，甚至元组。
        （3）元组元素由圆括号括起来：
            t = (1, 2, 3, 4)
        1.访问元组元素
        通过索引访问元组元素：
            元组[元素]
        2.获取元组长度
        元组长度指元组中元素的数量。通过len()获取长度：
            len(元组)
        3.遍历元组元素
        使用for语句和range()函数遍历列表索引，也可以使用for语句和enumerate()函数。
        4.排序
        元组的内容不能改变，可以将元组转换成列表，对列表排序，再重新赋值给元组。
        """

        print '【2-31~34】元组的访问、长度和遍历'
        t = (1, 2, 3, 4)
        print t[0]
        print t[3]
        print len(t)

        t = ('C++', 'C#', 'Java', 'Python')
        for i in range(len(t)):
            print t[i]
        for index,value in enumerate(t):
            print "第%d个元素值是【%s】" %(index,value)

        print '【2-35】对元组进行升序排列'
        t = ('C++', 'C#', 'Java', 'Python')
        l = list(t)
        l.sort()
        t = tuple(l)
        print t

        print '【2-36】对元组进行反序排列'
        t = ('C++', 'C#', 'Java', 'Python')
        l = list(t)
        l.reverse()
        t = tuple(l)
        print t

    def Example2_2_4(self):
        """
        2.2.4 字典
        """
        """
        字典也是内存中保存一组数据的数据结构，每个字典元素都有键（Key）和值（Value）两个属性。键用于定义和标识字典元素，可以是一个字符串或整数。
        字典元素就是一个“键/值对”。
        1.定义字典
        使用{}括号定义：
            d1 = {}
        键和值直接用冒号（:）分隔，元素间用逗号（,）分隔：
            d2 = {'name':'小明', 'gender':'男', 'age':'18', 'score':'80'}
        2.打印字典
        直接用print()函数打印：
            print(Dict)
        3.获取字典长度
        字典长度指字典中元素的数量。通过len()函数获取字典长度：
            len(Dict)
        4.访问字典元素
        对字典的管理就是对字典元素的访问和操作：
            Dict[key]
        5.添加字典元素
        通过赋值在字典中添加/修改元素：
            Dict[key] = value
        6.合并两个字典
        使用update()函数将两个字典合并：
            Dict1.update(Dict2)
        7.删除字典元素
        使用pop()函数删除元素，并返回删除的元素值：
            Dict.pop(key)
        8.判断字典是否存在元素
        使用in关键字判断字典元素：
            key in Dict
        9.遍历字典元素
        使用for...in语句遍历字典的键和值：
            for key in Dict.keys(): #key
                访问 Dict[key]
            for value in Dict.values(): #value
                访问 value
        10.清空字典
        使用clear()函数清空字典元素：
            Dict.clear()
        11.字典的嵌套
        字典里面还可以嵌套字典，访问方法为：
            Dict[key1][key2]
        """
        print '【2-37~40】字典的定义、打印、访问和元素添加。'
        d = {'name': 'Johney', 'gender': 'Male', 'age': '18', 'score': '80'}
        print d
        print len(d)

        print d['name']
        print d['gender']
        print d['age']
        print d['score']

        d['score'] = 100
        print d

        print '【2-41~42】合并两个字典，删除指定元素。'
        d1 = {'name': 'Johney', 'gender':'Male'}
        d2 = {'age': '18', 'score': '80'}
        d1.update(d2)
        print d1

        d1.pop('score')
        print d1

        print '【2-43】使用in关键字。'
        d = {'age': '18', 'score': '80', 'name': 'Johney', 'gender': 'Male'}
        if 'name1' in d:
            print d['name1']
        else:
            print '不包含键为name1的元素'

        print '【2-44~45】使用for...in语句分别遍历字典的键和值。'
        for key in d.keys():
            print '键'+key+ '的值：'+ d[key]
        for value in d.values():
            print value

        print '【2-46】清空字典'
        d.clear()
        print d

        print '【2-47】嵌套字典的例子'
        d = {'name':{'first':'Johney','last':'Lee'},'age':40}
        print d['name']['first']

    def Example2_2_5(self):
        """
        2.2.5 集合
        """
        """
        集合由一组无序排列的元素组成，分为可变集合（set）和不可变集合（frozenset）。
        1.使用set()函数创建可变集合，使用frozenset()函数创建不可变集合：
            s = set('python')
            fs = frozenset('python')
        注意！集合的元素是无序的。
        2.获取集合长度
        集合长度指集合元素数量，通过len()函数获取集合长度：
            len(set)
        3.访问集合元素
        集合本身是无序的，不能为集合创建索引或切片操作，只能循环遍历集合元素。
        """
        print '【2-48~51】创建可变集合、不可变集合，获取长度并遍历元素'
        s = set('python')
        print type(s)
        print s

        fs = frozenset('python')
        print type(fs)
        print fs

        print len(s)
        for e in s:
            print e

        """
        4.添加集合元素
        通过调用add()和update()函数在集合中添加元素，前者添加单个值，后者多个值。
        """
        print '【2-52~53】分别使用add()和update()函数添加集合元素'
        s = set('python')
        s.add('0')
        print s

        s = set([1, 2, 3])
        s.update([4, 5, 6])
        print s

        """
        5.删除集合元素
        remove()函数用于删除指定的集合元素，clear()函数用于删除指定集合的所有元素：
            Set.remove(element)
            Set.clear()
        """
        print '【2-54】删除集合元素'
        s = set([1, 2, 3])
        s.remove(1)
        print s #删除 1

        s.clear()
        print s #清空 s

        """
        6.判断集合是否存在元素
        使用in判断集合元素，存在则返回True，否则返回False：
            element in set
        7.遍历集合元素
        使用for...in语句遍历集合的值：
            for element in set:
                访问element
        """
        print '【2-55】判断集合元素。'
        s = set([1, 2, 3])
        if 2 in s:
            print 'exist'
        else:
            print 'not exist'

        print '【2-56】使用for语句遍历集合。'
        for e in s:
            print e

        """
        8.子集和超集
        对应于数学中的子集的概念，集合关系操作符可判断集合关系。
        操作符有：'==','!=','<','<=','>','>='。
        9.集合的并集
        集合的并集由所有属于集合A和集合B的元素组成，通过|操作符实现计算：
            s = s1 | s2
        也可以使用union()函数实现计算：
            s = s1.union(s2)
        10.集合的交集
        & 操作符可计算两集合的交集：
            s = s1 & s2
        也可使用intersection()函数实现计算：
            s = s1.intersection(s2)
        11.集合的差集
        集合的差集由所有属于A但不属于B的元素组成，通过-操作符实现计算：
            s = s1 - s2
        也可使用difference()函数实现计算：
            s = s1.difference(s2)
        12.集合的对称差分
        集合的对称差分是集合A和B的并集减去交集。使用^操作符计算：
            s = s1 ^ s2
        也可使用symmetric_difference()函数实现计算：
        s = s1.symmetric_difference(s2)
        """
        print '【2-57】判断两个集合关系'
        s1 = set([1, 2])
        s2 = set([1, 2, 3])
        if s1 != s2:
            if s1 < s2:
                print 's1是s2的真子集'
            if s2 > s1:
                print 's2是s1的超集'

        print '【2-58~59】分别使用|和union()计算两个集合的并集'
        s1 = set([1, 2])
        s2 = set([1, 2, 3])
        s = s1 | s2
        print s

        s = s1.union(s2)
        print s

        print '【2-60~61】分别使用&和intersection()计算两个集合的交集'
        s1 = set([1, 2, 3])
        s2 = set([3, 4])
        s = s1 & s2
        print s

        s = s1.intersection(s2)
        print s

        print '【2-62~63】分别使用-和difference()计算两个集合的差集'
        s = s1 - s2
        print s

        s = s1.difference(s2)
        print s

        print '【2-64~65】分别使用^和symmetric_difference()计算两个集合的对称差分'
        s = s1 ^ s2
        print s

        s = s1.symmetric_difference(s2)
        print s

    """
    2.3 运算符和表达式
    运算符是程序设计语言的最基本元素，是构成表达式的基础。
        2.3.1 运算符
        2.3.2 表达式
    """

    def Example2_3_1(self):
        """
        2.3.1 运算符
        """
        """
        在Python中，运算符可以指定进行的运算符类型。
        Python支持算术运算符、赋值运算符、位运算符、比较运算符、逻辑运算符、字符串运算符、成员运算符和身份运算符等基本运算符。
        1.算术运算符
        算术运算符可以实现数学运算。
            +       相加运算
            -       相减运算
            *       乘法运算
            /       除法运算
            %       求模运算（求余运算）
            **      幂运算
            //      整除运算
        2.赋值运算符
        赋值运算符将其右侧的常量或变量赋值到运算符左侧的变量中。
            =       直接赋值
            +=      加法赋值
            -=      减法赋值
            *=      乘法赋值
            /=      除法赋值
            %=      取模赋值
            **=     幂赋值
            //=     整除赋值
        3.位运算符
        位运算符允许对整型数中指定的位进行置位。
            &       按位与运算
            |       按位或运算
            ^       按位异或运算
            ~       按位非运算
            <<      位左移运算
            >>      位右移运算
        4.比较运算符
        比较运算符是对两个数值进行比较，返回一个布尔值。
            ==      等于运算符
            !=      不等运算符
            <>      不等运算符，与'!='相同
            <       小于运算符
            >       大于运算符
            <=      小于等于运算符
            >=      大于等于运算符
        5.逻辑运算符
            and     逻辑与运算符
            or      逻辑或运算符
            not     逻辑非运算符
        6.字符串运算符
            +       字符串连接
            *       重复输出字符串
            []      获取字符串中指定索引位置的字符
            [,]     截取字符串中的一部分
            in      成员运算符，包含则返回True
            not in  成员运算符，不包含则返回True
            r/R     指定原始字符串
        7.运算符优先级
            优先级由高到低排列是：指数运算、逻辑非和正负号、乘除取模取整、加减、位左右移运算、按位与运算、按位异或运算和按位或运算、比较运算、赋值运算、身份运算、成员运算、逻辑运算
        """

        print '【2-66】赋值运算符实例。'
        x = 3
        x += 3
        print x
        x -= 3
        print x
        x *= 3
        print x
        x /= 3
        print x

        print '【2-67】逻辑运算符实例'
        x = True
        y = False
        print 'x and y = ', x and y
        print 'x or y = ', x or y
        print 'not x = ', not x
        print 'not y = ', not y

        print '【2-68】字符串运算符实例'
        b = 'hello '
        a = b + 'world!'
        print a
        print a*2
        print r'hello\nworld!'

    def Example2_3_2(self):
        """
        2.3.2 表达式
        """
        """
        表达式由常量、变量和运算符等组成。如前述的：
            a = b + c
            a = b - c
            a = b * c
            a = b / c
            a = b % c
            a += 1
            b = a ** 2
        函数、对象等都可以成为表达式的一部分。
        """

    """
    2.4 Python对象
    面向对象编程是Python采用的基本编程思想，它可以将属性和代码集成在一起，定义为类，从而使程序设计更加简单、规范、有条理。
    Python的内置对象类型主要有数字、字符串、列表、元组、字典、集合等。在Python中一切都是对象。
        2.4.1 面向对象程序设计思想概述
        2.4.2 定义和使用类
        2.4.3 类的静态成员
        2.4.4 类方法
        2.4.5 使用isinstance()函数判断对象类型
        2.4.6 类的继承和多态
        2.4.7 对象的序列化
        2.4.8 对象的赋值
    """

    """
        2.4.1 面向对象程序设计思想概述
        面向对象程序设计的一些基本概念：
            （1）对象（Object）：
            面向对象程序设计思想可以将一组数据和与这组数据有关操作组装在一起，形成一个实体，这个实体就是对象。
            （2）类（Class）：
            具有相同或相似性质的对象的抽象就是类。
            对象的抽象是类，类的具体化就是对象。
            （3）封装：
            将数据和操作捆绑在一起，定义一个新类的过程就是封装。
            （4）继承：
            类之间的关系，一个类共享了一个或多个其他类定义的结构和行为。
            子类可以对基类的行为进行扩展、覆盖、重定义。从同一个类中继承得到的子类具有多态性，即相同的函数名在不同子类中有不同的实现。
            （5）方法：
            也称为成员函数，是指对象上的操作，作为类声明的一部分来定义。
            方法定义了对一个对象可以执行的操作。
            （6）构造函数：
            一种成员函数，用来在创建对象时初始化对象。构造函数一般与它所属的类完全同名。
            （7）析构函数：
            析构函数与构造函数相反，当对象脱离其作用域时（例如声明对象的函数调用完毕），系统自动执行析构函数。
            析构函数往往用来做“清理善后”的工作。
        
        2.4.2 定义和使用类
        类是面向对象程序设计思想的基础，可以定义指定类的对象。
        类中可以定义对象的属性（特性）和方法（行为）。
        1.声明类
        在Python中，可以使用class关键字来声明一个类，其基本语法如下：
            class 类名:
            成员变量
            成员函数
        同样，Python使用缩进标识类的定义代码。
        类的成员函数必须有一个参数self，而且位于参数列表的开头。
        self就代表类的实例（对象）自身，可以使用self引用类的属性和成员函数。
        """
    '''
class Person:
    def SayHello(self):
        print 'Hello!'
print '【2-69~70】定义一个类Person，定义并使用对象。'
p = Person()
p.SayHello()
    '''
    """
        2.定义类的对象
        对象是类的实例。只有定义了具体的对象，才能使用类。创建方法：
            对象名 = 类名()
        3.成员变量
        在类定义中，可以定义成员变量并同时对其赋初始值。
        """
    '''
print '【2-71】定义一个字符串类MyString，定义成员变量string，并同时对其赋初始值。'
class MyString:
    str = "MyString"
    def output(self):
        print (self.str)
s = MyString()
s.output()
    '''
    """
        在类的成员函数中使用self引用成员变量。
        注意！Python使用下划线作为变量前后缀来指定特殊变量，规则如下：
            __xxx__表示系统定义名字。
            __xxx表示类中的私有变量名。
        类的成员变量可以分为两种情况，一种是公有变量，一种是私有变量。
            公有变量可以在类的外部访问，它是类与用户之间交流的接口。用户可以通过公有变量向类中传递数据和获取类中的数据。
            为了保证类的设计思想和内部结构并不完全对外公开，在类的外部都无法访问私有变量。
        在Python中，除了__xxx格式的成员变量外，其他的成员变量都是公有变量。
        4.构造函数
        构造函数是类的一个特殊函数，它拥有一个固定的名称，即__init__（注意，函数名是以'__'开头和结束的）。
        当创建类的对象实例时系统会自动调用构造函数，通过构造函数对类进行初始化操作。
        """
    '''
print '【2-72】在类MyString中使用构造函数。'
class MyString:
    def __init__(self):
        self.str = "MyString"
    def output(self):
        print self.str
s = MyString()
s.output()
    
print '【2-73】使用带参数的构造函数。'
class UserInfo:
    def __init__(self, name, pwd):
        self.username = name
        self._pwd = pwd
    def output(self):
        print '用户：'+self.username+'\n密码：'+self._pwd
u = UserInfo("admin", "123456")
u.output()
    '''
    """
        5.构析函数
        Python构析函数有一个固定的名称，即__del__()。通常在构析函数中释放类所占用的资源。
        使用del语句删除一个对象，释放它所占用的资源。
        """
    '''
print '【2-74】构析函数实例'
class MyString:
    def __init__(self): #构造函数
        self.str = "MyString"
    def __del__(self): #构析函数
        print 'byebye~'
    def output(self):
        print self.str
s = MyString()
s.output()
    '''
    """
        2.4.3 类的静态成员
        静态变量和静态方法是类的静态成员。
        1.静态变量
        在类中可以定义静态变量，静态变量只属于定义它们的类。
        Python不需要显式定义静态变量，任何公有变量都可以作为静态变量使用：
            类名.变量名
        """
    '''
print '【2-75】定义一个类User，使用静态变量online_count记录当前在线的用户数量。'
class Users(object):
    online_count = 0
    def __init__(self): # 构造函数，创建对象时User.online_count加1
        Users.online_count += 1
    def __del__(self): # 构析函数，释放对象时User.online_count减1
        Users.online_count -= 1
a = Users() # 创建User对象
a.online_count += 1
print Users.online_count # User.online_count不受对象影响
    '''
    """
        2.静态方法
        与静态变量相同，静态方法只属于它的类，而不属于具体的对象。静态方法具有如下特点：
            （1）静态方法无需传入self参数，因此在静态方法中无法访问实例变量。
            （2）在静态方法中不可以直接访问类的静态变量，但可以通过类名引用静态变量。
        静态方法无法访问实例变量，也不能直接访问类的静态变量，所以静态方法与定义的类没有直接关系，而是起到类似函数工具库的作用。
        可以使用装饰符@staticmethod定义静态方法：
            class 类名:
                @staticmethod
                def 静态方法名():
                    方法体
        对象名或类名都可以调用静态方法，二者没有什么区别。
        """
    '''
print '【2-76】静态方法的实例。'
class MyClass: # 定义类
    var1 = 'String 1'
    @staticmethod #静态方法
    def staticmd():
        print '我是静态方法'
MyClass.staticmd()
c = MyClass()
c.staticmd()
    '''
    """
        2.4.4 类方法
        类方法是Python的一个新概念。类方法有如下特性：
            （1）可以使用函数名调用，与静态方法一样。
            （2）无法访问实例变量，但可以访问类的静态变量，与静态方法一样。
            （3）需传入代表本类的cls参数。
        可以使用装饰符@classmethod定义类方法：
            class 类名:
                @classmethod
                def 类方法名(cls):
                    方法体
        对象名和类名都可以调用类方法，二者没有区别。类方法有一个参数cls，代表定义类方法的类，可以通过cls访问类的静态变量。
        """
    '''
print '【2-77】类方法的实例。'
class MyClass: # 定义类
    val1 = 'String 1'
    def __init__(self):
        self.val2 = 'Value 2'
    @classmethod # 类方法
    def classmd(cls):
        print '类：' + str(cls) + '，val1：' + cls.val1 + '，无法访问val2的值'
MyClass.classmd()
c = MyClass()
c.classmd()
    '''
    """
    2.4.5 使用isintance()函数判断对象类型。
    isinstance()函数可以检测一个给定的对象是否属于（继承于）某个类或类型，如果是则返回True，否则返回False：
        isinstance(对象名，类名或类型名)
    """
    '''
class MyClass: # 定义类
val1 = 'String 1' # 静态变量
def __init__(self):
self.val2 = 'Value 2'
c = MyClass()
print isinstance(c,MyClass)
l = list([1, 2, 3, 4])
print isinstance(l,list)
    '''
    """
    2.4.6 类的继承和多态
    继承和多态是面向对象程序设计思想的重要机制。
    类可以继承其他类的内容，包括成员变量和成员函数。从一个类中继承得到的子类也具有多态性，相同的函数名在不同子类中有不同的实现。
    1.继承
    子类拥有父类的所有属性和函数。
    可以在定义类时指定其父类：
        class A:
            def __init__(self, property):   # 构造函数
                self.propertyA = property   # 类A的成员变量
            def functionA():                # 类A的成员函数
    从类A派生一个类B：
        class B (A):
            propertyB           # 类B的成员变量
            def functionB():    # 类B的成员函数
    从类B中可以访问到类A中的成员变量和成员函数：
        objB = B()              # 定义一个类B的对象objB
        print objB.propertyA    # 访问类A的成员变量
        objB.functionA()        # 访问类A的成员函数
    类B是类A派生出来的，继承了类A的属性和方法。
    """
    '''
print '【2-79】类继承的实例'
import time
class Users:
    username = ''
    def __init__(self, uname):
        self.username = uname
        print '（构造函数：' + self.username + '）'
    # 显示用户名
    def dispUserName(self):
        print self.username

class UserLogin(Users):
    def __init__(self, uname, lastLoginTime):
        Users.__init__(self, uname) # 调用父类User的构造函数
        self.lastLoginTime = lastLoginTime
    def dispLoginTime(self):
        print '登陆时间为：' + self.lastLoginTime
# 获取当前时间
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# 声明三个对象
myUser_1 = UserLogin('admin', now)
myUser_2 = UserLogin('lee', now)
myUser_3 = UserLogin('zhang', now)
# 分别调用父类和子类函数
myUser_1.dispUserName()
myUser_1.dispLoginTime()
myUser_2.dispUserName()
myUser_2.dispLoginTime()
myUser_3.dispUserName()
myUser_3.dispLoginTime()
    '''
    """
    2.抽象类和多态
    使用面向对象程序设计思想，对类的继承实现应用程序的层次化设计。
    类的继承关系是树状的，一个根类可以派生出多个子类，子类还可以派生出其他子类。
    每个子类都可以从父类中继承成员变量和成员函数，实际上相当于继承了一套程序设计框架。
    
    Python可以实现抽象类的概念。
    抽象类是包含抽象方法的类，而抽象方法不包含任何实现的代码，只能在其子类中实现抽象函数的代码。
        （1）定义抽象类
        Python通过类库abc实现抽象类，因此在定义抽象类之前需要从类库abc导入ABCMeta类和abstractmethod类：
            from abc import ABCMeta, abstractmethod
        ABCMeta是Metaclass for defining Abstract Base Classes的缩写，也就是抽象基类的元类。元类是创建类的类。定义代码：
            __metaclass__ = ABCMeta
        例如：
            class myabc(object):
                __metaclass__ = ABCMeta
                ......
        在抽象类里可以定义抽象方法：
            @abstractmethod
        抽象方法不包含任何实现代码，其函数体通常使用pass，例如：
            class myabc(object):
                __metaclass__ = ABCMeta
                @abstractmethod
                def abcmethod (self):pass
        （2）实现抽象类
        可以从抽象类派生子类。方法和普通类的派生和继承一样。
        （3）多态
        多态指抽象类中定义的一个方法，可以在其子类中重新实现，不同子类的实现方法也不同。
    """
    '''
print '【2-80】抽象类和多态的实例。创建一个抽象类shape，它定义了一个画图类的基本框架。'
from abc import ABCMeta, abstractmethod
class Shape(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.color = 'black' # 默认使用黑色

    @abstractmethod
    def draw(self):pass
# 创建类Shape的子类circle
class circle (Shape):
    def __init__(self, x, y, r): # define C(x,y) and r
        self.x = x
        self.y = y
        self.r = r
    def draw(self):
        print 'Draw Circle: (%d, %d, %d)' %(self.x, self.y, self.r)
# 从类Shape中派生出画直线的类line
class line (Shape):
    def __init__(self, x1, y1, x2, y2): #define begin and end
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def draw(self):
        print 'Draw line: (%d, %d, %d, %d)' %(self.x1, self.y1, self.x2, self.y2)
# 调用函数
c = circle(10, 10, 5)
c.draw()

l = line(10, 10, 20, 20)
l.draw()

print '【2-86】在【2-80】的基础上定义一个类circle的对象mycircle，对其设置成员变量值，再将其赋值到新的对象newcircle中。'
mycircle = circle(20, 20, 5)
# 复制对象
newcircle = mycircle
newcircle.draw()
'''

    def Example2_4_7(self):
        """
        2.4.7 对象的序列化
        """
        """
        序列化（Serialization）是将对象的状态信息转换为可储存或传输形式的过程。
        序列化时，对象将当前状态写入到临时或永久存储区，通过从存储区读取或反序列化对象可以重新创建该对象。
        在Python中，序列化过程成为pickle，可以将对象pickle成字符串、文件或者任何类似于文件的对象，也可以将这些字符串、文件或类似于文件的对象unpickle成原来的对象。
        pickle模块用于实现基本的数据序列和反序列化。
            import pickle
        1.将对象序列化成字符串
        pickle.dumps()方法将对象序列化成字符串。
        pickle.loads()方法实现反序列化过程。
        """

        import pickle
        print '【2-82】对列表对象进行序列化。'
        lista = ['C++', 'C#', 'Java', 'Python']
        listb = pickle.dumps(lista)
        print listb

        print '【2-83】将对象序列化成字符串。'
        listc = pickle.loads(listb)
        print listc

        """
        2.将对象序列化到文件
        pickle.dump()方法可以将对象序列化到文件：
            pickle.dump(被序列化的对象, 文件对象)
        在序列化到文件之前，需要打开文件，并得到文件对象。
        
        open()函数可以打开指定文件：
            文件对象 = open(文件名,访问模式,buffering)
        参数文件名用于指定要打开的文件，通常需要包含路径，可以是绝对路径，也可以说相对路径。
        参数访问模式用于指定打开文件的模式，执行序列化操作时，通常使用'wb'作为访问模式参数，表示以二进制写模式打开文件。
        整型参数buffering是可选参数，用于指定访问文件所采用的缓冲方式：
            buffering = 0，表示不缓冲；
            buffering = 1，表示只缓冲一行数据；
            buffering > 1，表示使用给定值作为缓冲区大小。
            
        pickle.load()方法可以实现反序列化的功能：
            被序列化的对象 = pickle.load(文件对象)
        反序列化之前需要先访问文件，并得到文件对象。具体操作同dump。 
        """

        print '【2-84】将对象序列化到文件。'
        output = open('..\\data\\data.pkl','wb')
        pickle.dump(lista, output)
        output.close()

        print '【2-85】从文件data.pkl反序列化。'
        f = open('..\\data\\data.pkl','rb')
        list = pickle.load(f)
        print list
        f.close()

        """
        2.4.8 对象的赋值 
        同普通变量，对象也可以通过赋值操作和传递函数参数等方式进行复制。
        通过赋值操作，实现对象复制：
            新对象名 = 原有对象名
        """

class Chapter3():
    """
    -** 3 **- 常用Python语句
    知识要点：
        赋值语句        分支语句
        循环语句        异常处理语句
    """
    """
    3.1 赋值语句
    赋值语句是Python语言中最简单、最常用的语句。赋值语句定义变量并为其赋初值。
    """
    def Example3_1(self):

        print '【3-1】赋值语句例子'
        a = 10
        a += 1
        print a
        a *= 10
        print a
        a **= 2
        print a

        """
        3.1.1 通过赋值语句实现序列解包
        Python序列包括字符串、列表、元组。
        序列解包是将序列中储存的值指派给各个变量：
            x, y, z = 序列
        被解包的序列里的元素数量必须与'='左侧的变量数量相同。
        """

        print '【3-2】赋值实现序列解包。'
        x, y, z = (1, 2, 3)
        print x
        print y
        print z

        """
        3.1.2 链式赋值
        链式赋值可以一次性将一个值指派给多个变量：
            变量1 = 变量2 = 变量3 = 值
        变量1、变量2和变量3同时被赋值。
        """

        print '【3-3】链式赋值。'
        x = y = z = 3
        print x
        print y
        print z

    """
    3.2 控制语句
    Python中有专门的控制语句来控制代码段的执行方式。
    不同功能的控制语句称为控制流。
    """

    def Example3_2_1(self):
        """
        3.2.1 条件分支语句
        """
        """
        条件分支语句指，当指定表达式取不同值时，程序运行的流程也发生相应的分支变化。
        Python提供的条件分支语句包括if语句、else语句和elif语句。
        1.if语句
        if语句是最常用的一种条件分支语句：
            if 条件表达式:
                语句块
        如果语句块中包含多条语句，这些语句必须拥有相同的缩进。
        """

        print '【3-4~5】if语句和嵌套if语句的例子。'
        a = 150
        if a > 10:
            print '变量a大于10'
            if a > 100:
                print '变量\$a大于100'

        """
        2.else语句
        将else语句与if语句结合使用，指定不满足条件时执行的语句：
            if 条件表达式:
                语句块1
            else:
                语句块2
        """

        print '【3-6】if...else...语句的例子。'
        if a > 10:
            print '变量a大于10'
        else:
            print '变量a小雨或等于10'

        """
        3.elif语句
        elif语句是else语句和if语句的组合，等同于C中的else if：
            if 条件表达式1:
                语句块1
            elif 条件表达式2:
                语句块2
            elif 条件表达式3:
                语句块3
            ......
            else:
                语句块n
        
        """

        print '【3-7】显示当前系统日期的Python代码，用到了if、elif和else语句。'
        import datetime
        str = '今天是'

        d = datetime.datetime.now()
        print d.weekday()
        if d.weekday() == 0:
            str += '星期一'
        elif d.weekday() == 1:
            str += '星期二'
        elif d.weekday() == 2:
            str += '星期三'
        elif d.weekday() == 3:
            str += '星期四'
        elif d.weekday() == 4:
            str += '星期五'
        elif d.weekday() == 5:
            str += '星期六'
        else:
            str += '星期日'
        print str

    def Example3_2_2(self):
        """
        3.2.2 循环语句
        """
        """
        Python的循环语句包括while语句和for语句。
        1.while语句
        while语句的基本语法结构：
            while 条件表达式:
                循环语句体
        """

        print '【3-8】while语句实例。'
        i = 1
        sum = 0
        while i < 11:
            sum += i
            i += 1
        print sum

        """
        2.for语句
        for语句基本语法结构：
            for i in range(begin, end):
                循环体
        循环计数器i从start开始，到end结束，退出循环。
        for语句还可以用于遍历元组、列表、字典和集合等序列对象。
        """

        print '【2-9】for语句实例。'
        i = 1
        sum = 0
        for i in range(1,11):
            print i
            sum += i

        print sum

        """
        3.continue语句
        循环体中，continue语句跳过本次循环后面的代码，重新开始下一次循环。
        """

        print '【3-10】只计算1~100之间偶数和。'
        i = 1
        sum = 0
        for i in range(1,101):
            if i % 2 ==1:
                continue
            sum += i

        print sum

        """
        4.break语句
        循环体中，break语句跳出循环体。
        """

        print '【3-11】将[3-8]修改为使用break语句跳出循环体。'
        i = 1
        sum = 0
        while True:
            if i == 11:
                break
            sum += i
            i += 1
        print sum

    """
    3.3 异常处理语句
    """
    def Example3_3(self):
        """
        程序在运行过程中可能会出现异常情况。
        """
        """
        
        异常处理语句用于捕捉异常情况并进行处理，避免程序异常退出。
        Python的异常处理语句是try-exception：
            try:
                <try语句块>
            except [<异常处理类>, <异常处理类>, ... .] as <异常处理对象>:
                <异常处理代码>
            finally:
                <最后执行代码>
        通常在finally块中释放资源。
        """

        print '【3-12~13】发生除零错误时不进行和进行异常处理的情况'
        # i = 10
        # print 30 / (i - 10)
        try:
            i = 10
            print 30 / (i - 10)
        except Exception as e:
            print e
        finally:
            print "执行完成"

class Chapter4():
    """
    -** 4 **- Python函数
    知识要点：
        声明函数            方法调用
        在函数中传递参数    函数的返回值
        变量的作用域        全局变量和局部变量
        Python内置函数      函数式编程
        调用函数
    """
    """
    4.1 声明和调用函数
    函数包含两个部分：声明这个部分是函数，定义这个函数包含的功能。
    """

    """
    4.1.1 声明函数
    使用关键字def创建Python自定义函数：
        def 函数名(参数列表):
            函数体
    参数列表可以为空，参数之间用逗号（,）分隔。函数体可以是一条语句，也可以多条语句。
    Python函数体唯一的分隔符是一个冒号（:），接着代码本身是缩进的。函数体比def关键字多一个缩进。
    """
    '''
def PrintWelcome():
    print '【4-1】创建一个简单的函数PrintWelcome，它的功能是打印字符串"欢迎使用Python"。'
    print '欢迎使用Python'

def PrintString(str):
    print '【4-2】定义函数PrintString，通过打印内容'
    print str

def sum(num1, num2):
    print '【4-3】定义一个函数sum()，计算并打印两个参数之和。'
    print num1 + num2
    '''

    """
    4.1.2 调用函数
    直接使用函数名调用函数，系统函数和自定义函数调用方法是一致的。
    如果函数存在参数，调用函数时也需要使用参数。
    """
    '''
print '【4-4】调用len()函数，返回字符串student长度。'
print len("student")

print '【4-5】调用[4-3]声明的函数sum()，计算100+200之和。'
sum(100, 200)
    '''

    """
    4.2 参数和返回值
    参数和返回值与函数交换数据。
    """

    """
    4.2.1 列表和字典参数
    1.普通参数
    Python按值传递参数。
    值传递指调用函数时将常量或变量的值（称为实参）传递给函数的参数（称为形参）。实参和形参互不相干。
    """
    '''
print '【4-6】函数中按值传递实例。'
def func1(num):
    num += 1
a = 10
func1(a)
print a

print '【4-7】分别打印实参和形参的地址。'
def func2(num):
    print 'address of num: ', id(num)
a = 10
func2(a)
print 'address of a: ', id(a)
    '''

    """
    2.列表和字符参数
    除了普通变量以外，列表、字典变量能向函数内部批量传送数据。
    列表或字典作为函数参数时，函数内部操作会影响实参。
    """
    '''
print '【4-8】列表作为函数参数的实例。'
def sum(list):
    total = 0
    for x in range(len(list)):
        print str(list[x]) + '+'
        total += list[x]
    print '=' + str(total)
list = [10, 20, 30, 40]
sum(list)

print '【4-9】字典作为函数参数的实例。'
def print_dict(dict):
    for (k, v) in dict.items():
        print 'dict[%s] =' % k, v
dict = {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange'}
print_dict(dict)

print '【4-10】函数中修改列表参数的实例。'
def swap(list):
    temp = list[0]
    list[0] = list[1]
    list[1] = temp
list = [10,20]
print list
swap(list)
print list

print '【4-11】函数中修改字典参数的实例。'
def changeA(dict):
    dict['a'] = 1

d = {'a': 10, 'b': 20, 'c': 30}
changeA(d)
print d
'''

    """
    3.参数的默认值
    Python中可为参数设置默认值。
    定义函数时直接在参数后面使用'='为其设置默认值。
    调用函数而不指定该参数值时，函数体中以默认值为该参数。
    
    注意！有默认值的参数只能出现在没有默认值的参数后面。
    错误范例：
        def func1(a = 1, b, c = 10):
            函数体
    
    4.可变长参数
    Python支持可变长度的参数列表。
    可变长参数可以是元组或列表，参数以*开头表示一个元组：
        def func(*t):
    任意多个实参调用func()函数，如：
        func(1,2,3,4)
    也可以不指定可变长参数，此时可变长参数是一个没有元素的元组或字典。
    
    参数以**开头表示一个字典：
        def func(**t):
    任意多个实参调用func()函数：
        key = value
    """
    '''
print '【4-12】设置参数默认值的实例。'
def say(message, times = 1):
    print message * times
say('hello')
say('Python', 3)

print '【4-14】以元组为可变长参数的实例。'
def func1(*t):
    print '可变长参数数量如下：'
    print len(t)
    print '依次为：'
    for x in range(len(t)):
        print t[x]

func1(1,2,3,4)

print '【4-15】用可变长参数计算任意一组指定数字之和。'
def sum(*t):
    sum = 0
    for x in range(len(t)):
        print str(t[x]) + '+'
        sum += t[x]
    if len(t) > 0:
        print '=' + str(sum)
sum(1, 2)
sum(1, 2, 3, 4)
sum(11, 22, 33, 44, 55)
print '【4-16】调用函数时不指定可变长参数。'
sum()

print '【4-17】以字典为可变长参数的实例。'
def summy(**t):
    print t
summy(a = 1, b = 2, c = 3)
    '''
    """
    4.2.2 函数的返回值
    return语句返回函数值并退出函数。
    """
    '''
print '【4-18】对[4-13]中sum()函数改造，函数返回相加结果。'
def sum(num1, num2):
    return num1 + num2
print sum(1, 3)

print '【4-19】返回指定列表中的偶数。'
def filter_even(list):
    list1 = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list1.append(list[i])
            i -= 1
    return list1
list = [1,2,3,4,5,6,7,8,9,10]
list2 = filter_even(list)
print list2
    '''


if __name__ == "__main__":
    # c2 = Chapter2()
    # c3 = Chapter3()
    c4 = Chapter4()
    # c2.Example2_1_1()
    # c2.Example2_1_2()
    # c2.Example2_1_3()
    # c2.Example2_2_1()
    # c2.Example2_2_2()
    # c2.Example2_2_3()
    # c2.Example2_2_4()
    # c2.Example2_2_5()
    # c2.Example2_3_1()
    # c2.Example2_4_7()
    # c3.Example3_1()
    # c3.Example3_2_1()
    # c3.Example3_2_2()
    # c3.Example3_3()