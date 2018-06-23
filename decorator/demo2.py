# -*- coding: utf-8 -*-

def a_new_deco(a_func):
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
print(func.__name__)  # wrap_func, 理应是hello_world，但装饰器重写了函数的名字和注释文档, 如何解决呢？看demo3
