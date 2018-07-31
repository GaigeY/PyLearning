# -*- coding: UTF-8 -*-
# Filename: const.py
# 定义一个常量类实现常量的功能

class _const:
    """
    该类定义了一个方法__setattr__和一个异常ConstError。
    ConstError类继承自类TypeError，通过调用类自带的字典__dict__，判断定义的常量是否包含在字典中。
    如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值，从而可以避免给常量重复赋值。

    最后两行代码的作用是把const类注册到sys.modules这个全局字典中。
    """
    class ConstError(TypeError):pass
    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const (%s)" %name
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()