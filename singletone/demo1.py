# -*- coding: utf-8 -*-

"""类实现
"""
class singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            origin = super(singleton, cls)
            cls._instance = origin.__new__(cls, *args, **kwargs)
        return cls._instance

class Mycls(singleton):
   a = 1

m1 = Mycls()
m1.a = 2

print(Mycls().a)   # 2
