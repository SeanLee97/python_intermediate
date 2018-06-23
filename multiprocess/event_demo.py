# -*- coding: utf-8 -*-

"""Event
Event用来实现进程间通信(IPC)
"""

import multiprocessing
import time

def wait_for_event(e):
    print("wait for event: starting...")
    e.wait()
    print("wait for event: e.is_set() -> ", e.is_set())

def wait_for_event_timeout(e, t):
    print("wait for event timeout: starting...")
    e.wait(t)
    print("wait for event timeout: e.is_set() -> ", e.is_set())

if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name="Block", 
                                 target=wait_for_event, args=(e, ))
    w2 = multiprocessing.Process(name="Non-Block", 
                                 target=wait_for_event_timeout, args=(e, 2))
    w1.start()
    w2.start()
    time.sleep(3)
    e.set() # 发送事件,3s后timeout过期了，故只有wait_for_event有效

