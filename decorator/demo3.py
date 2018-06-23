# -*- coding: utf-8 -*-

from functools import wraps

def a_new_deco(a_func):
    @wraps(a_func)   # 使用a_func的名字和文档，不重写
    def wrap_func():
        print("start to wrap...")
        a_func()
        print("finish!")
    return wrap_func

@a_new_deco
def hello_world():
    print("hello world")


func = hello_world
func()
print(func.__name__)  # hello_world
