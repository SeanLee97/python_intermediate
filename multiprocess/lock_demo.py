# -*- coding: utf-8 -*-

"""Lock
当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突
"""

import multiprocessing
import sys

def worker_with(lock, f):
    with lock:
        # 加锁,通过with可自动关锁
        with open(f, 'a+') as fs:
            n = 10
            while n>1:
                fs.writelines("Lockd acquired via with\n")
                n -= 1

def worker_no_with(lock, f):
    lock.acquire()   # 加锁
    try:
        with open(f, 'a+') as fs:
            n = 10 
            while n > 1:
                fs.writelines("Lockd acquired directly\n")
                n -= 1
    finally:
        lock.release()   # 释放锁

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    f = 'lock_test.txt'
    p1 = multiprocessing.Process(target=worker_with, args=(lock, f, ))
    p2 = multiprocessing.Process(target=worker_no_with, args=(lock, f))
    p1.start()
    p2.start()
    print("end")
