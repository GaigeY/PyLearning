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

    """
    4.3 全局变量和局部变量
    函数中可以定义变量。函数中定义的变量称为局部变量，函数体外定义的变量是全局变量。
    """

    """
    4.3.1 变量的作用域
    局部变量旨在定义它的函数内部有效；全局变量在定义后的代码中都有效，包括它后面定义的函数体内。
    局部变量和全局变量同名，则只有局部变量有效。
    """
    '''
print '【4-20】局部变量和全局变量作用域的实例。'
a = 100     # 全局变量
def setNumber():
    a = 10  # 局部变量
    print a     # 打印a
setNumber()
print a
'''
    """
    4.3.2 在IDLE的调试窗口中查看变量的值
    在程序中使用print()函数输出变量的值，是了解程序运行情况的常用方法。
    也可以在IDLE的调试窗口中查看变量的值，这种方法更直观。
    1.设置断点
    断点是调试器的功能之一，可以让程序中断在需要的地方，从而方便对其分析。
    2.单步调试
    设置断点后，运行程序，可以停在断点处，然后逐条语句单步运行。
    单步调试看到程序的运行过程，同时可以查看在某一时刻某个变量的值。
    
    4.3.3 在PyCharm的调试窗口中查看变量的值
    PyCharm可以更方便地调试Python程序。
    调试程序可以在运行程序时查看大多数源代码信息，例如行数、变量信息、函数等。
    1.设置和应用断点
    傻瓜操作。Run -> Toggle Line Breakpoint
    2.调试Python程序
    点击Debug按钮，调试当前的Python程序。程序会暂停在断点代码处，并在下方的Debug窗格中显示变量的值。
    3.单步运行
    程序员采用单步运行跟踪程序的运动轨迹。
    选择Run -> Step Over或Step Into执行单步运行。程序前面的剪头图标会移动到下一行。
    Step Into和Step Over的区别：调用函数时，Step Into会进入函数并停留在函数的第一行，Step Over会越过函数，停留在函数后面的第一行。
    """

    """
    4.4 常用Python内置函数
    Python提供了很多内置函数。
    内置函数就是Python中被自动加载的函数，任何时候都可以用。
    """

    """
    4.4.1 数学运算函数
    如下表所示：
        abs()           abs(x)                             返回x的绝对值
        pow()           pow(x,y)                           返回x的y次幂
        round()         round(x[,n])                       返回浮点数x的四舍五入值，保留n位小数
        divmod()        divmod(a,b)                        返回a除以b的商和余数，在一个元组中：(a/b,a%b)
    """
    '''
print '【4-21】数学运算函数的实例。'
print abs(-1)
print round(80.23456,2)
print pow(2,3)
print divmod(8,3)
    '''
    """
    4.4.2 字符串处理函数
    字符串处理函数是一个程序设计语言的基本功能。
    1.字符串中字符大小写的变换
    如下表所示：
        lower()         str.lower()                         将字符串str中的字母转换为小写字母
        upper()         str.upper()                         将字符串str中的字母转换为大写字母
        swapcase()      str.swapcase()                      将字符串str中的字母大小写互换
        capitalize()    str.capitalize()                    将字符串str中的首字母大写
        title()         str.title()                         将字符串str中所有单词的首字母大写，其余为小写
    2.指定输出字符串时的对齐方式
    如下表所示：
        ljust()         str.ljust(width,[fillchar])         左对齐字符串str，总宽度为width，不足部分以fillchar指定的字符填充，默认为空格
        rjust()         str.rjust(width,[fillchar])         右对齐字符串str，总宽度为width，不足部分以fillchar指定的字符填充，默认为空格
        center()        str.center(width,[fillchar])        居中对齐字符串str，总宽度为width，不足部分以fillchar指定的字符填充，默认为空格
        zfill()         str.zfill(width)                    将字符串str变成width长，右对齐，不足部分以0补足
    3.搜索和替换
    如下表所示：
        find()          str.find(substr[,start[,end]])      返回字符串str中substr首次出现的位置，没有则返回-1
        index()         str.index(substr[,start[,end]])     返回字符串str中substr首次出现的位置，没有则返回运行错误
        rfind()         str.rfind(substr[,start[,end]])     返回字符串str中substr最后出现的位置，没有则返回-1
        rindex()        str.rindex(substr[,start[,end]])    返回字符串str中substr最后出现的位置，没有则返回运行错误
        count()         str.count(substr[,start[,end]])     返回字符串str中substr出现的次数
        replace()       str.replace(oldstr,newstr[,count])  把oldstr换成newstr，替换次数上限为count
        strip()         str.strip([chars])                  删除字符串str首尾指定字符，默认为空白符（'\n','\r','\t',''...）
        lstrip()        str.lstrip([chars])                 删除字符串str开头指定字符，默认为空白符（'\n','\r','\t',''...）
        rstrip()        str.rstrip([chars])                 删除字符串str末尾指定字符，默认为空白符（'\n','\r','\t',''...）
        expandtabs()    str.expandtabs(tabsize)             把字符串str每个tab换成tabsize个空格，默认8个
    4.分隔和组合
    如下表所示：
        split()         str.split([sep[,maxsplit]])         依据seq把str分割成列表，maxsplit是分割次数
        splitlines()    str.splitlines([keepends])          把str按行分割成一个列表，keepends为True则每行保留行分隔符
        join()          str.join(seq)                       将seq以字符串str连接成一个新的字符串
    5.字符串判断相关
        startswith()    str.startswitch(substr)             判断str是否以substr开头
        endswith()      str.endswitch(substr)               判断str是否以substr结尾
        isalnum()       str.isalnum()                       判断str是否全为字母或数字
        isalpha()       str.isalpha()                       判断str是否全为字母
        isdigit()       str.isdigit()                       判断str是否全为数字
        islower()       str.islower()                       判断str是否全为小写字母
        isupper()       str.isupper()                       判断str是否全为大写字母
    """
    '''
print '【4-22】字符大小写变换函数的实例。'
str1 = 'hello world'
str2 = 'HELLO WORLD'
str3 = 'Hello world'
print str1.upper()
print str2.lower()
print str3.swapcase()
print str3.swapcase()
print str1.capitalize()
print str2.title()

print '【4-23】指定输出字符串对齐方式函数的实例。'
str1 = 'hello world'
print str1.ljust(30, "*")
print str1.rjust(30, "*")
print str1.center(30, "*")
print str1.zfill(30)

print '【4-24】搜索和替换字符串函数的实例。'
str1 = 'Hello world'
print str1.find('l')
print str1.index('o')
print str1.rfind('l')
print str1.rindex('o')
str2 = '    Hello'
print str2.replace(' ','*')
print str2.strip()

print '【4-25】分隔和组合字符串函数的实例。'
str1 = 'hello world Python'
list1 = str1.split()
print list1
str1 = 'hello world\nPython'
list1 = str1.splitlines()
print list1
list1 = ['hello', 'world', 'Python']
str1 = '#'
print str1.join(list1)

print '【4-26】与字符串判断相关函数的实例'
# coding = gb2312
str = 'python String function'
print str + ".startwith('t') 的结果"
print str.startswith('t')
print str + ".endwith('t') 的结果"
print str.endswith('t')
print str + ".isalnum() 的结果"
print str.isalnum()
str = 'pythonStringfunction'
print str + ".isalnum() 的结果"
print str.isalnum()
print str + ".isalpha() 的结果"
print str.isalpha()
print str + ".isupper() 的结果"
print str.isupper()
print str + ".islower() 的结果"
print str.islower()
print str + ".isdigit() 的结果"
print str.isdigit()
str = '3423'
print str + ".isdigit() 的结果"
print str.isdigit()
    '''

    """
    4.5 函数式编程
    函数式编程是一种典范。
    """

    """
    4.5.1 函数式编程概述
    函数式编程是面向对象之前最流行的编程思想。
    1.什么是函数式编程
    函数式编程是一种编程的基本风格，也就是构建程序的结构和元素的方式。
    函数式编程将计算过程看作数学函数，也就是可以使用表达式编程。相同的参数调用函数会得到相同的结果。
    下面介绍几个与函数式编程有关的概念：
        （1）头等函数（First-class Function）
        一个编程语言把函数视为头等函数，则称其拥有头等函数。
        拥有头等函数的编程语言可以将函数作为其他函数的参数，也可以将函数作为其他函数的返回值。
        拥有头等函数的编程语言可以把函数赋值给变量或储存在元组、列表、字典、集合和对象等数据结构中。
        有的语言还支持匿名函数。
        拥有头等函数的编程语言中，函数名没有任何特殊的状态，将函数看作function类型的二进制类型。
        （2）高阶函数（Higher-order Function）
        高阶函数是头等函数的一种实践，将其他函数作为参数或返回结果。
        （3）纯函数
        纯函数具有特性：
            纯函数与外界交换数据只有唯一通道——参数和返回值。
            纯函数不操作全局变量，没有状态、无I/O操作，不改变传入的任何参数值。理想情况下不会传入任何外部数据。
            纯函数很容易移植到新运行环境，最多只需修改类型定义。
            纯函数具有引用透明性（Referential Transparency）。同一输入值一定得到相同输出值。
        （4）递归
        函数式编程语言中，循环通常通过递归实现。
        递归就是函数里调用自身；使用递归策略时，必须有一个明确的递归结束条件，称为递归出口。
    2.函数式编程的优点
        （1）便于单元测试
        单元测试指对软件中最小可测试单元进行检测验证。
        函数是最小可测试单元的一种。
        （2）便于调试
        函数式编程语言的bug易于重现。
        （3）适合并行执行
        并行通常指程序不同部分同时运行而互不干扰。
        程序并行执行的最大问题是或成死锁，死锁指两个或两个以上的进程（线程）因资源争夺造成互相等待的现象。
    
    4.5.2 Python函数式编程常用的函数
    1.lambda表达式
    Lambda表达式是一种匿名函数，从数学的λ演算得名。
    λ演算用来定义可计算函数。
        （1）Python匿名函数
        Python的Lambda表达式函数体只能有唯一语句，也就是返回值表达式语句：
            返回函数名 = lambda参数列表 : 函数返回值表达式语句
        （2）Lambda表达式数组
        Lambda表达式作为数组（或列表、字典）元素，定义方法为：
            数组名 = [(Lambda表达式1), (Lambda表达式2), ...]
        调用数组中Lambda表达式的方法：
            数组名[索引]( Lambda表达式的参数列表)
        （3）Lambda表达式作为函数的返回值
        在普通函数中返回Lambda表达式。
    """
    '''
print '【4-27】使用Lambda表达式的例子。'
sum = lambda x,y,z : x+y+z
print sum(1,2,3)
# 等价于def sum(x,y,z)

print '【4-28】定义一个Lambda表达式数组，分别是平方、立法和四次方。'
Arr = [(lambda x : x ** 2), (lambda x : x ** 3), (lambda x : x ** 4)]
print Arr[0](2),Arr[1](2),Arr[2](2)

print '【4-29】定义一个函数math，可以返回加法、减法、乘法和除法的Lambda表达式。'
def math(o):
    if o == 1:
        return lambda x,y : x+y
    if o == 2:
        return lambda x,y : x-y
    if o == 3:
        return lambda x,y : x*y
    if o == 4:
        return lambda x,y : x/y

action = math(1) # 返回加法Lambda表达式
print '10+2',action(10,2)
action = math(2) # 返回减法Lambda表达式
print '10-2=',action(10,2)
action = math(3) # 返回乘法Lambda表达式
print '10*2,=',action(10,2)
action = math(4) # 返回除法Lambda表达式
print '10/2.=',action(10,2)
    '''
    """
    2.使用map()函数
    map()函数将指定序列中的所有函数作为参数调用指定函数，并将结果构成一个新的序列返回：
        结果序列 = map(映射函数, 序列1[, 序列2, ...])
    map()函数的参数中，序列数取决于映射函数的参数数量。
    序列1、序列2等元素会按顺序作为映射函数的参数，映射函数的返回值将作为map()函数返回序列的元素。
    """
    '''
print '【4-30】使用map()函数依次计算2、4、6、8、10的平方。'
arr = map(lambda x : x ** 2, [2, 4, 6, 8, 10])
for e in enumerate(arr):
    print e

print '【4-31】在map()函数中对两个序列进行处理。'
arr = map(lambda x,y: x+y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
for e in enumerate(arr):
    print e
    '''
    """
    3.filter()函数
    filter()函数对指定序列执行过滤操作：
        filter(function, sequence)
    function接受一个函数，返回布尔值True或False。sequence可以是列表、元组或字符串。
    filter()函数以序列参数sequence中每个元素为参数调用function，调用结果为True的元素最后作为返回值。
    """
    '''
print '【4-32】filter()函数的实例。'
def is_even(x):
    return x % 2 == 0

arr =  filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for e in enumerate(arr):
    print e
    '''
    """
    4.reduce()函数
    reduce()函数将指定序列中所有元素作为参数按一定的规则调用指定函数：
        计算结果 = reduce(映射函数, 序列)
    映射函数必须有2个参数。以序列前两个元素调用映射函数，将返回结果和第三个元素调用函数，以此类推，直至最后一个元素。
    从Python3.0开始，reduce()函数不再被集成在Python内置函数中，需引用functools模块，才能调用reduce()函数。
    """
    '''
print '【4-33】使用ruduce()函数计算1-10的整数和。'
# def add(x,y): return x+y
add = lambda x,y : x+y
sum = reduce(add, range(1, 11))
print sum
    '''
    """
    5.zip()函数
    zip()函数以一系列列表作为参数，将列表对应的函数打包成一个个元组，返回这些元组组成的列表。
    打包结果前面加上*，实现解压。
    """
    '''
print '【4-34】zip()函数的实例。'
a = [1, 2, 3]
b = [4, 5, 6]
z = [7, 8, 9]
zipped = zip(a, b, z)
for element in zipped:
    print element

print '【4-35】zip()函数传入参数不等的实例。'
a = [1, 2, 3]
b = [4, 5, 6, 7, 8, 9]
zipped = zip(a, b)
for element in zipped:
    print element

print '【4-35】zip()函数将打包结果解压。'
a = [1, 2, 3]
b = [4, 5, 6]
zipped = zip(a, b)
unzipped = zip(*zipped)
for element in unzipped:
    print element
    '''
    """
    4.5.3 普通编程方式与函数式编程的对比
    相比较而言，函数式编程具有如下特点：
        （1）代码更简单。
        （2）数据、操作、返回值都放一起。
        （3）没有循环体，几乎没有临时变量，无序分析程序的流程行尾数据变化过程。
        （4）代码定义需要做什么，而不是怎么做。
    """
    '''
print '【4-37~38】分别以普通编程方式和函数式编程方式计算列表中正数和。'
list = [2, -4, 9, -5, 6, 13, -12, -3, 8, -11, 16]
sum = 0
for i in range(len(list)):
    if list[i] > 0:
        sum += list[i]
print sum

sum = filter(lambda x : x > 0, list)
s = reduce(lambda x,y : x+y, sum)
print s
    '''

    """
    4.6 闭包和递归函数
    """

    """
    4.6.1 闭包
    Python中，闭包（Closure）指函数的嵌套。
    在函数内部定义一个嵌套函数，将嵌套函数视为一个对象，作为它的函数的返回结果。
    """
    '''
# coding = utf-8
def func_lib():
    def add(x,y):
        return x+y
    return add      # 返回函数对象

fadd = func_lib()
print fadd(1, 2)
    '''
    """
    4.6.2 递归函数
    递归函数指直接或间接调用自身的函数。
    """
    '''
print '【4-40】递归函数计算阶乘。'
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print fact(5)
    '''

    """
    4.7 迭代器和生成器
    """

    """
    4.7.1 迭代器
    迭代器是访问集合内元素的一种方式。
    迭代对象从序列（列表、元组、字典、集合）的第一个元素开始遍历。迭代器不能回退，只能往前行进迭代。
    1.iter()函数
    内建的工厂函数iter(iterable)获取序列的迭代器对象：
        迭代器对象 = iter(序列对象)
    next()函数获取迭代器的下一个函数：
        next(迭代器对象)
    2.enumerate()函数
    enumerate()函数将列表或元组生成一个有序号的序列。
    """
    '''
print '【4-41】iter()函数的实例。'
list = ['C++', 'C#', 'Java', 'Python']
it = iter(list)
print next(it)
print next(it)
print next(it)
print next(it)

print '【4-42】enumerate()函数的实例。'
# coding = utf-8
list = ['C++', 'C#', 'Java', 'Python']
for index,value in enumerate(list):
    print "第%d个元素是%s" % (index,value)
    '''
    """
    4.7.2 生成器
    生成器（Generator）是一个特殊的函数，它具有如下特点：
        （1）生成器函数都包含一个yield语句，执行到yield语句时函数返回。
        （2）生成器函数可以记住上一次返回时在函数体中的位置，对生成器函数的下一次调用跳转至该函数中间，而上次调用的所有局部变量保持不变。
    生成器的返回值有一个__next__()方法，恢复生成器执行，并直到下一个yield表达式处。
    """
    '''
    print '【4-43】生成器的实例。'
def addlist(alist):
    for i in alist:
        yield i + 1
alist = [1, 2, 3, 4]
for x in addlist(alist):
    print x
print '【4-44】__next__()方法实现[4-43]的功能。'
def addlist(alist):
    for i in alist:
        yield i + 1
alist = [1, 2, 3, 4]
x = addlist(alist)
print x.next()
print x.next()
print x.next()
print x.next()
    '''

class Chapter5():
    """
    -** 5 **- Python模块
    模块是Python语言一个重要概念，将函数按功能划分到一起，以便日后使用或共享。
    知识要点：
        模块的基本概念        random模块
        sys模块               fractions模块
        math模块              time模块
        decimal模块           platform模块
        自定义模块
    """

    """
    5.1 模块的概念
    """

    """
    5.1.1 什么是模块
    函数是可以实现一项或多项功能的一段程序；模块是很多功能的扩展，是可以一项或多项功能的程序块。
    模块的范围比函数要广。模块里可以重用多个函数。
    Python的模块以.py文件的形式储存。
    
    5.1.2 如何导入模块
    使用模块前必先导入：
        import 模块名
    访问模块中的函数：
        模块名.函数名(参数列表)
    访问模块中的变量：
        模块名.变量
    """

    """
    5.2 Python标准库中的常用模块
    Python标准库是Python自带的开发包，是Python的组成部分，会随Python解释器一起安装在系统中。
    """

    def Example5_2_1(self):
        """
        5.2.1 sys模块
        """
        import sys

        """
        sys模块是Python标准库中最常用的模块之一。
        sys模块获得命令行参数，从而实现从程序外部向程序传递参数的功能；也可以获取程序路径和当前系统平台等信息。
        1.获取当前的操作系统平台
        使用sys.platform获取当前的操作系统平台
        """

        print '【5-1】使用变量sys.platform打印当前的操作系统平台。'
        print sys.platform

        """
        2.使用命令行参数
        命令行参数是运行程序时命令行中给定的参数。例如：
            python command.py a b c
        a,b,c连同command.py都是命令行参数，可以向程序中传递数据。
        sys模块的argv数组用于获取Python命令行参数。sys.arg[0]是当前运行的脚本文件名，sys.arg[1]是第一个命令行参数，sys.arg[2]是第二个命令行参数。
        3.退出应用程序
        sys.exit()函数退出应用程序：
            sys.exit(n)
        n=0时程序无错误退出；n=1时程序有错误退出。
        """

        print '【5-2】打印命令行参数：打开命令行窗口，切到src目录，输入"Python例5-2.py a b c"'
        print '【5-3】使用sys.exit()函数的例子'

        """
        4.字符编码
        对字母和符号进行编码的二进制代码称为字符代码。
        常用的字符编码为ASCII码（美国标准信息交换码）。
        常用的处理中文的字符编码包括GB2312、GBK和BIG5等。
            GB2312编码：中华人民共和国国家汉字信息交换用编码，全称《信息交换用汉字编码字符集——基本集》。大陆和新加坡等地使用。
            GBK编码：汉字内码扩展规范。繁简一库。
            BIG5编码：一种繁体中文汉字字符集，与GB2312存在冲突。
        UTF-8:8-bit Unicode Transformation Format，又称万国码。
        
        sys.getdefaultencoding()函数用于获取系统当前编码。
        
        5.搜索模块的路径
        sys.path()获取搜索模块的路径。
        """

        print '【5-4】打印系统当前编码。'
        print sys.getdefaultencoding()

        print '【5-5】打印Python搜索模块的路径。'
        print sys.path

        """
        sys.path实际上是一个列表，第一个元素就是当前程序所在是目录。
        如需Python到制定目录搜索模块文件，向sys.path中添加指定的目录：
            sys.path.append(指定的目录)
        """

    def Example5_2_2(self):
        """
        5.2.2 platform模块
        """
        import platform

        """
        python中，platform模块给我们提供了很多方法去获取操作系统的信息
        如：
            platform.platform()     #获取操作系统名称及版本号，'Windows-7-6.1.7601-SP1'
            platform.version()      #获取操作系统版本号，'6.1.7601'
            platform.architecture() #获取操作系统的位数，('32bit', 'WindowsPE')
            platform.machine()      #计算机类型，'x86'
            platform.node()         #计算机的网络名称，'hongjie-PC'
            platform.processor()    #计算机处理器信息，'x86 Family 16 Model 6 Stepping 3, AuthenticAMD'
            platform.uname()        #包含上面所有的信息汇总，uname_result(system='Windows', node='hongjie-PC',
                                        release='7', version='6.1.7601', machine='x86', processor='x86 Family
                                        16 Model 6 Stepping 3, AuthenticAMD')
        
        还可以获得计算机中python的一些信息：
            platform.python_build()
            platform.python_compiler()
            platform.python_branch()
            platform.python_implementation()
            platform.python_revision()
            platform.python_version()
            platform.python_version_tuple()
        """

        print '【5-6】打印当前操作系统名称及版本号。'
        print platform.platform()

        print '【5-7】打印当前操作系统类型。'
        print platform.system()

        print '【5-8】打印当前操作系统的版本信息。'
        print platform.version()

        print '【5-9】打印当前操作系统的位数。'
        print platform.architecture()

        print '【5-10】打印当前计算机的类型信息。'
        print platform.machine()

        print '【5-11】打印当前计算机的网络名称。'
        print platform.node()

        print '【5-12】打印当前计算机的处理器信息。'
        print platform.processor()

        print '【5-13】打印当前计算机的综合信息。'
        print platform.uname()

        print '【5-14】打印Python版本信息。'
        print platform.python_build()

        print '【5-15】打印Python主版本信息。'
        print platform.python_version()
        print platform.python_version_tuple()

        """
        platform.python_version()函数获取Python的修订版本信息。
        修订版本是版本库的一个快照（每次修改的备份），当版本库不断扩大时，必须有手段来识别这些快照。
        因此需要为每个修订版本定义修订版本号。
        """

        print '【5-16】打印Python的编译器信息。'
        print platform.python_compiler()

        """
        获取Python分支信息
        分支是软件控制中的一个概念，一个分支是某个开发主线的一个拷贝，分支可以为特定客户实现需求。
        分支的意义在于，在不干扰开发主线的情况下，和主线并行开发，待开发结束后合并回主线中。
        可以在主线上创建分支，再在分支上创建分支。
        """

        print '【5-17】打印Python的分支信息。'
        print platform.python_branch()

        """
        获取Python解释器的实现版本信息
        Python的解释器版本有很多种实现方式：
            CPython：
                默认的python实现。
                脚本大多数情况下都运行在这个解释器中。
                CPython是官方的python解释器，完全按照python的规格和语言定义来实现，所以被当作其他版本实现的参考版本。
                CPython是用C语言写的，当执行代码的时候Pythond代码会被转化成字节码（bytecode）。
                所以CPython是个字节码解释器。
                当我们从Python官网下载安装包安装，或者是通过类似 "apt-get" 或者 "yum"工具安装的时候，安装的都是CPython版本。
            PyPy
                一个很多地方都和CPython很像的实现，但是这个解释器本身就是由Python写成。
                然而这个解释器的代码先转化成C，然后在编译。
                PyPy被认为要比CPython性能更好，因为CPython会把代码转化成字节码，PyPy会把代码转化成机器码。
            Psyco
                一个类似PyPy，但是很好的解释器。
                现在已经被PyPy取代了，有可能的话，使用PyPy来代替Psyco。
            Jython
                用java实现的一个解释器。Jython允许程序员写Python代码，还可以把java的模块加载在python的模块中使用。
            IronPython
                使用C#语言实现，可以使用在.NET 和 Mono 平台的解释器。
                tip: Mono 是提供.NET-compatible 工具的开源框架。
            CLPython
                用Common Lisp实现的解释器，现在不提倡使用。
                它允许Python和Common Lisp的代码混合使用。
                跟Python2兼容。
            PyS60(Python for S60)
                是诺基亚 S60 平台的一个实现版本，不赞成使用。
            ActivePython
                基于CPython然后添加一系列拓展的一个实现。
                是由ActiveState发布的。Python2 和 Python3 都兼容。
            Cython(不是CPython)
                一个允许把Python代码转化成C/C++代码或者使用各种各样的C/C++模块/文件的实现。
                换句话说，Cython是C/C++ 和Python的一个桥梁。
                Cython也是Python的一种方言。开发者也可以使用Cython来执行Python脚本，并且执行效率比CPython更快。
                tips: Python 模块 modules 和 类库libraries是一个东西，只是叫法不同。
            QPython
                CPython解释器的一个安卓接口。
                QPython来自Python的安卓模块。
                可以在 Google Play中找到QPython。
            Kivy
                一个开源的框架(使用Python解释器)，它可以运行在 Android, iOS, Windows, Linux, MeeGo, Android SDK, 和 OS X平台上。
                支持Python3，开发者正在开发其兼容Cython上的Python3。
            SL4A (Scripting Layer for Android)
            一个允许安卓上执行各种脚本语言的兼容层。
            SL4A 有很多的模块，我们比较关注的是“Py4A” (Python for Android)。
            Py4A 是安卓平台上的一种CPython。
        其他
            还有很多其他的不同实现。例如WPython，DSPython 请参见 Wiki。
        """

        print '【5-18】打印Python解释器的实现版本信息。'
        print platform.python_implementation()

    def Example5_2_3(self):
        """
        5.2.3 与数学有关的模块
        """
        import math
        import random
        import fractions

        """
        包括math模块、random模块、decimal模块和fractions模块。
        
        1.math模块
        math模块用于数学处理，可以实现基本数学运算：
            import math
        math模块定义了e和pi两个常量。
        """

        print '【5-19】打印e和pi的值。'
        print math.e,math.pi

        """
        math模块的常用方法：
            asin            math.asin(x)            返回x的反正弦
            asinh           math.asinh(x)           返回x的反双曲正弦
            atan            math.atan(x)            返回x的反正切
            atan2           math.atan2(x)           返回y/x的反正切
            atanh           math.atanh(x)           返回x的反双曲正切
            ceil            math.ceil(x)            返回大于等于x的最小整数
            copysign        math.copysign(x,y)      返回与y同号的x的值
            cos             math.cos(x)             返回x的余弦
            cosh            math.cosh(x)            返回x的余切
            degrees         math.degrees(x)         将x弧长转为角度，与radians为反函数
            exp             math.exp(x)             返回e^x
            fabs            math.fabs(x)            返回x的绝对值
            factorial       math.factorial(x)       返回x!
            floor           math.floor(x)           返回小于等于x的最大整数
            fmod            math.fmod(x,y)          返回x对y取模的余数
            fsum            math.fsum(x)            返回x阵列值的各项和
            hypot           math.hypot(x,y)         返回x,y的平方和开方
            isinf           math.isinf(x)           x为无穷大则返回True，否则返回False
            isnan           math.isnan(x)           x不是数字则返回True，否则返回False
            log             math.log(x,a)           返回log_a x，a默认为e
            log10           math.log10(x)           返回lg x
            pow             math.pow(x,y)           返回x^y
            radians         math.radians(c)         将x角度转为弧长，与degree为反函数
            sin             math.sin(x)             返回x的正弦
            sinh            math.sinh(x)            返回x的双曲正弦
            sqrt            math.sqrt(x)            返回x的开方
            tan             math.tan(x)             返回x的正切
            tanh            math.tanh(x)            返回x的双曲正切
            trunc           math.trunc(x)           返回x的整数部分
        """

        print '【5-20】math模块的实例。'
        print 'math.ceil(3.4) =',math.ceil(3.4)
        print 'math.fabs(-3) =',math.fabs(-3)
        print 'math.floor(3.4) =',math.floor(3.4)
        print 'math.sqrt(4) =',math.sqrt(4)
        print 'math.trunc(3.4) =',math.trunc(3.4)

        """
        2.random模块
        random模块用于生成随机数。
            random          random.random()                             生成一个[0,1)的随机浮点数
            uniform         random.uniform(a,b)                         生成一个[a,b]或[b,a]的随机浮点数
            randint         random.randint(a,b)                         生成一个[a,b]的随机整数
            randrange       random.randrange([start],stop[,step])       生成一个[star,stop)内star+i*step的随机数
            choice          random.choice(sequence)                     从序列seq中随机获取一个元素
            shuffle         random.shuffle(x[,random])                  将列表x中的元素打乱
            sample          random.sample(sequence,k)                   从指定序列中随机获取长度为k的片段
        """

        print '【5-21】随机生成一个0-100的整数。'
        print random.randint(0,99)

        print '【5-22】随机选取一个0-100的偶数。'
        print random.randrange(0, 101, 2)

        print '【5-23】随机选取一个浮点数。'
        print random.random

        print '【5-24】从指定字符集合里随机选取一个字符。'
        print random.choice('jioadsf$@#&%^()$@%')

        print '【5-25】将一个列表中的元素打乱。'
        list = [1, 2, 3, 4, 5, 6]
        print random.shuffle(list)
        print list

        print '【5-26】从指定序列中随机获取指定长度的片段。'
        print random.sample(list,3)

        """
        3.decimal模块
        浮点数缺乏精确性，decimal模块提供了一个Decimal数据类型用于浮点数计算。
        与内置二进制浮点数实现float相比，Decimal数据类型更适用于金融应用和其他需要精确十进制表达的情况。
        导入decimal模块：
            from decimal import Decimal
        定义Decimal类型的数据：
            Decimal(数字字符串)
        
        Decimal在一个独立的上下文环境下工作，通过getcontext()方法获取当前环境。
        例如，decimal.getcontext().prec用于设定小数点精度。
        导入getcontext：
            from decimal import getcontext
        """

        print '【5-27】Decimal数据类型的实例。'
        from decimal import Decimal
        print Decimal('1.0') / Decimal('3.0')

        print '【5-28】getcontext的实例。'
        from decimal import getcontext
        getcontext().prec = 6
        print Decimal('1.0') / Decimal('3.0')

        """
        4.fractions模块
        fractions模块用于表现和处理分数。
        首先要导入模块：
            import fractions
        定义分数数据的方法：
            x = fractions.Fraction(分子，分母)
        
        Fraction对象会自动进行约分。
        """

        print '【5-29】fractions模块定义分数的实例。'
        x = fractions.Fraction(1, 3)
        print x

        print '【5-30】Fraction对象自动约分的实例。'
        x = fractions.Fraction(1, 6)
        print x * 4

    def Example5_2_4(self):
        """
        5.2.4 time模块
        """
        import time

        """
        time模块是Python标准库中最常用的模块之一，time模块可以提供各种操作时间的函数。
        
        1.时间的表示方式
        计算机可以使用时间戳和struct_time数组两种方式表示时间。
        Unix时间戳（Unix Timestamp）或称Unix时间（Unix Time）、POSIX时间（POSIX Time）是格林尼治时间1970年元旦零点起至当前的秒数。
        struct_time数组包含9个元素，具体如下：
            year        四位数的年份
            month       月份
            day         日期
            hours       小时
            minutes     分钟
            seconds     秒
            weekday     星期，星期一为0
            Julia day   一年有几天，1-366
            DST         是否为夏令时
        
        2.获取当前时间
        time.time()函数用于获取当前时间的时间戳。
        
        3.将一个时间戳转换成一个当前时区的时间戳
        time.localtime()函数用于转换当前时区的struct_time。
        
        4.格式化输出struct_time时间
        time.strftime()函数按照指定的格式输出struct_time时间：
            time.strftime(格式字符串, struct_time时间)
        可以使用的日期和时间符号如下：
            %y  两位数的年份表示    00-99
            %Y  四位数的年份表示  0000-9999
            %m  月份                01-12
            %d  月内中的一天         0-31
            %H  24小时制小时数       0-23
            %I  12小时制小时数      01-12
            %M  分钟数              00-59
            %S  秒数                00-59
            %a  本地简化的星期名称
            %A  本地完整化的星期名称
            %b  本地简化的月份名称
            %B  本地完整化的月份名称
            %c  本地相应的日期表示和时间表示
            %j  年内的一天          001-366
            %p  本地A.M.或P.M.
            %U  一年中的星期数       00-53     星期日是一星期的开始
            %w  星期                  0-6      星期日是一星期的开始
            %W  一年中的星期数       00-53     星期一是一星期的开始
            %x  本地相应的日期表示
            %X  本地相应的时间表示
            %Z  当前时区的名称
            %%  %号本身
        
        5.直接获取当前时间的字符串
        time.ctime()返回当前时间的字符串。
        """

        print '【5-31】time.time()函数的实例。'
        print time.time()

        print '【5-32】time.localtime()函数的实例。'
        print time.localtime(time.time())

        print '【5-33】time.strftime()函数的实例。'
        print time.strftime('%Y-%m-%d',time.localtime(time.time()))

        print '【5-34】time.ctime()函数的实例'
        print time.ctime()

    """
    5.3 自定义和使用模块
    """

    def Example5_3_3(self):
        """
        5.3.1 创建自定义模块
        """
        """
        把函数组织到模块中。
        在其他程序引用模块中定义的函数。
        增加代码的重用性。
        
        模块是一个.py文件，其中包含函数的定义。
        """

        print '【5-35】创建一个模块mymodule.py，其中包含2个函数PrintString和sum()。'

        """
        一个应用程序中可以定义多个模块，通常使用易读的名字标识它们。例如数学相关为mymath.py，数据库相关为mydb.py。
        """

    def Example5_3_4(self):
        """
        5.3.2 使用自定义模块
        """
        """
        导入自定义模块的方法与导入Python标准库中模块的方法相同。
        """

        print '【5-36】假定[5-35]创建的模块mymodule.py与本例保存在同一目录下，引用其中的函数。'
        import mymodule # 导入mymodule模块
        mymodule.PrintString("Hello Python") # 调用PrintString()函数
        mymodule.sum(1,2)   # 调用sum()函数

if __name__ == "__main__":
    # c2 = Chapter2()
    # c3 = Chapter3()
    # c4 = Chapter4()
    c5 = Chapter5()
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
    # c5.Example5_2_1()
    # c5.Example5_2_2()
    # c5.Example5_2_3()
    # c5.Example5_2_4()
    # c5.Example5_3_3()
    c5.Example5_3_4()