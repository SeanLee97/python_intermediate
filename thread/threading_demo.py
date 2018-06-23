# -*- coding: utf-8 -*-

from time import ctime, sleep
import threading 

def music(info = ''):
     for i in range(2):
         print("I was listening to music.%s %s" % (info, ctime()))
         sleep(1)

def coding(info = ''):
    for i in range(2):
        print("I was coding %s %s" % (info, ctime()))
        sleep(5)

def order_run():
    music()
    coding()

def thread_run():
    t1 = threading.Thread(target=music, args=("sean", ))
    t2 = threading.Thread(target=coding, args=("lee", ))
    threads = [t1, t2]
    for t in threads:
        #setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。  
        t.setDaemon(True)
        t.start()
    """
    join（）的作用是避免僵尸进程，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    注意:  join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程
    """
    t.join()

if __name__ == '__main__':
    #order_run()
    thread_run()

