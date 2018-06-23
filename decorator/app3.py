# -*- coding: utf-8 -*-

from functools import wraps

def memory(func):
    mem = {}
    @wraps(func)
    def wrap_func(*args):
        if args not in mem:
            v = func(*args)
            mem[args] = v
        else:
            v = mem[args]
        return v
    return wrap_func


