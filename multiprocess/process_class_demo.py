# -*- coding: utf-8 -*-

"""
将进程定义为类
"""

import multiprocessing
import time

class ClockProcessing(multiprocessing.Process):
    def __init__(self, interval):
        super(ClockProcessing, self).__init__()
        self.interval = interval
    # 进程p调用start()时自动调用run()
    def run(self):
        n = 5
        while n > 0:
            print("The time is ", time.ctime())
            time.sleep(self.interval)
            n -= 1

    @property
    def pid(self):
        return multiprocessing.current_process().pid

    @property
    def name(self):
        return multiprocessing.current_process().name

if __name__ == "__main__":
    p = ClockProcessing(3)
    print("pid {} \t name {}".format(p.pid, p.name))
    p.start()
