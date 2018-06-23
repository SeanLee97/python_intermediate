# -*- coding: utf-8 -*-

"""带参数的装饰器
"""

from functools import wraps

def log(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(logfile, 'a') as f:
                f.writelines(log_string + '\n')

            return func(*args, **kwargs)
        return wrapped_func
    return logging_decorator

@log()
def myfunc1():
    pass
@log(logfile='out1.log')
def myfunc2():
    pass

myfunc1()
myfunc2()
