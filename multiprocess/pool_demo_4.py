# -*- coding: utf-8 -*-

"""
使用多个进程池
"""

import multiprocessing
import os, time, random

def Lee():
    print("Run task Lee-%s" % (os.getpid())) #os.getpid()获取当前的进程的ID
    start = time.time()
    time.sleep(random.random()*10) # 生成0～1的小数
    end = time.time()
    print("Task Lee, runs %0.2f seconds" % (end-start))

def Sean():
    print("Run task Sean-%s" % (os.getpid())) #os.getpid()获取当前的进程的ID
    start = time.time()
    time.sleep(random.random()*40) # 生成0～1的小数
    end = time.time()
    print("Task Sean, runs %0.2f seconds" % (end-start))


if __name__ == "__main__":
    func_list = [Lee, Sean]
    pool = multiprocessing.Pool(2)
    for func in func_list:
        pool.apply_async(func)

    print("Waiting for all subprocesses done...")
    pool.close()
    pool.join()
    print("All Done! ")


