# -*- coding: utf-8 -*-

"""日志
"""

from functools import wraps

def log(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + ' was called')
        return func(*args, **kwargs)
    return with_logging

@log
def addition_func(x):
    return x+x


print(addition_func(2))
