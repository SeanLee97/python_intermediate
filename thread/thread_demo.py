# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
_thread.start_new_thread ( function, args[, kwargs] )

    function - 线程函数。
    args - 传递给线程函数的参数,他必须是个tuple类型。
    kwargs - 可选参数。

"""

import _thread
import time

# 为线程定义一个函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
         time.sleep(delay)
         count += 1
         print("%s: %s" % (thread_name, time.ctime(time.time())))

# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("thread1", 2))
    _thread.start_new_thread(print_time, ("thread2", 4))
except:
    print("Unable to start thread")

# 使得主进程一直运行，要不随着主进程运行结束，它的线程也会结束
while 1:
    pass
