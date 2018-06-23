# -*- coding: utf-8 -*-

def a_new_deco(a_func):
    def wrap_func():
        print("start to wrap...")
        a_func()
        print("finish!")
    return wrap_func

def hello_world():
    print("hello world")


func = a_new_deco(hello_world)

func()
