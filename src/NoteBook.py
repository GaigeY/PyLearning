# -*- coding: UTF-8 -*-
import const

class Experience():
    """
    写在开头：这个Project是我学习Python的笔记，里面有学习笔记和代码实例。
    """
    """
    -**2**- Python语言基础
    # 知识要点：
    # 常量          变量
    # 数据类型      简单数据类型转换
    # 列表          元组
    # 运算符        集合
    # Python对象
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

    def Example2_4(self):
        """
        2.4实例较少，笔记集成到一个Example中。
        """
        """
        """


if __name__ == "__main__":
    exp = Experience()
    # exp.Example2_1_1()
    # exp.Example2_1_2()
    # exp.Example2_1_3()
    # exp.Example2_2_1()
    # exp.Example2_2_2()
    # exp.Example2_2_3()
    # exp.Example2_2_4()
    # exp.Example2_2_5()
    #exp.Example2_3_1()