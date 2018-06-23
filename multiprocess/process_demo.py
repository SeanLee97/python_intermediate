# -*- coding: utf-8 -*-

import multiprocessing
import time

"""
Process

创建进程的类：Process([group [, target [, name [, args [, kwargs]]]]])，target表示调用对象，args表示调用对象的位置参数元组。kwargs表示调用对象的字典。name为别名。group实质上不使用。

方法：is_alive()、join([timeout])、run()、start()、terminate()。其中，Process以start()启动某个进程。

属性：authkey、daemon（要通过start()设置）、exitcode(进程在运行时为None、如果为–N，表示被信号N结束）、name、pid。其中daemon是父进程终止后自动终止，且自己不能产生新进程，必须在start()之前设置。

"""

# 创建函数并将其作为单个进程
def worker_1(interval):
    print("worker 1")
    time.sleep(interval)
    print("worker 1 end")

def worker_2(interval):
    print("worker 2")
    time.sleep(interval)
    print("worker 2 end")

def worker_3(interval):
    print("worker 3")
    time.sleep(interval)
    print("worker 3 end")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=worker_1, args=(2, ))
    p2 = multiprocessing.Process(target=worker_2, args=(3, ))
    p3 = multiprocessing.Process(target=worker_3, args=(4, ))

    p1.start()   # 启动进程
    p2.start()
    p3.start()

    print("The number of CPU is ", multiprocessing.cpu_count())
    for p in multiprocessing.active_children():
        print("child pid {}, name {}".format(p.pid, p.name))
    print("END !!!")
    '''
    print("pid:", p1.pid)
    print("name:", p1.name)
    print("is_alive:", p1.is_alive())
    '''
