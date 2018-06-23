# -*- coding: utf-8 -*-

"""Semaphore
信号量，Semaphore用来控制对共享资源的访问数量，例如池的最大连接数
"""

import multiprocessing
import time

def worker(sp, i):
    with sp:   # with 自动PV操作
        print(multiprocessing.current_process().name, ' acquired')
        time.sleep(i)
        print(multiprocessing.current_process().name, ' release')
    # try:
    #    sp.acquire()
    #    dosomething()
    # except:
    #    sp.release
if __name__ == '__main__':
    s = multiprocessing.Semaphore(2)   # 2为最大信号量
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(s, i*2))
        p.start()
