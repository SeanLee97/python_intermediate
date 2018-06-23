# -*- coding: utf-8 -*-

"""
上下文管理器的一个常见用例，是资源的加锁和解锁，以及关闭已打开的文件（就像我已经展示给你看的）

实现上下文管理器，能在with中使用
"""

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    # __exit__ 三个参数是必须的
    # 如果发生异常，Python会将异常的type,value和traceback传递给__exit__方法。
    # 它让__exit__方法来决定如何关闭文件以及是否需要其他步骤。在我们的案例中，我们并没有注意它们。

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with File('demo.txt', 'w') as f:
    f.write('Hola')
