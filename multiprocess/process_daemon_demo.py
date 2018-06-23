# -*- coding: utf-8 -*-

"""
因子进程设置了daemon属性，主进程结束，它们就随着结束了
除非主进程调用join()方法阻塞，等待子进程执行完毕
"""

import multiprocessing
import time

def worker(interval):
    print("work start: {}".format(time.ctime()))
    time.sleep(interval)
    print("work end: {}".format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3, ))
    p.daemon = True   # 守护进程，不打印
    p.start()
    p.join()   # 阻塞父进程结束，等待子进程结束再结束
    print("end")
