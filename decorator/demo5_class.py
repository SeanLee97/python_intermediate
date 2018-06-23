# -*- coding: utf-8 -*-

"""装饰器类
"""

from functools import wraps

class log(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(self.logfile, 'a') as f:
                f.writelines(log_string + '\n')
            self.notify()  # 发送一个通知
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass

class email_log(log):
    def __init__(self, email, *args, **kwargs):
        self.email = email
        super(email_log, self).__init__(*args, **kwargs)

    def notify(self):
        print('send mail to %s' % self.email)
        pass

@log()
def myfunc1():
    pass

@email_log("xmlee97@gmail.com", logfile='email.log')
def myfunc2():
    pass

myfunc1()
myfunc2()
