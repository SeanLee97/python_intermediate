# -*- coding: utf-8 -*-

"""Pool 进程池
（可以限制最大进程数目）
在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，并行操作可以节约大量的时间。当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥进程池的功效。
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。

apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，异步的
apply(func[, args[, kwds]])是阻塞的（理解区别，看例1例2结果区别）
close()    关闭pool，使其不在接受新的任务。
terminate()    结束工作进程，不在处理未完成的任务。
join()    主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。

非阻塞，不等待子进程的执行完毕就执行主函数其他部分
"""

import multiprocessing
import time

# 非阻塞
def func(msg):
    print("msg: ", msg)
    time.sleep(2)
    print("end")

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in range(4):
        msg = "hello %d " % (i)
        pool.apply_async(func, (msg, ))   # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去, 非阻塞

    print("这是非组塞的，主函数会自己执行自个的，不等待子进程执行完，这句话就输出了")
    pool.close() 
    pool.join()    # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("end")



