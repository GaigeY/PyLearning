# -*- coding: UTF-8 -*-
import const

class Experience():
    """
    写在开头：这个Project是我学习Python的笔记，里面会有各种试验。
    """


    def ConstUse(self):
        # 该部分是书本2.1.1实例，实例共有三组

        # 【2-1】定义一个常量value，值为5。然后打印它的值。
        const.value = 5;
        print const.value;

if __name__ == "__main__":
    exp = Experience()
    exp.ConstUse()