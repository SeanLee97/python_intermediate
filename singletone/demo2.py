# -*- coding: utf-8 -*-

"""装饰器实现
"""

def singleton(cls, *args, **kwargs):
    instance = {}
    def wrap_fn():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrap_fn

@singleton
class Mycls:
    a = 1

m = Mycls()
m.a = 2

print(Mycls().a)  # 2
