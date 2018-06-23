# -*- coding: utf-8 -*-

from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer
from threading import Thread

"""
socketserver封装了TCPServer意味着不用使用socket写长篇代码实现相同的功能了
"""
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("Got connection from ", self.client_address)
        while True:
            msg = self.request.recv(1024)
            if not msg:
                break
            self.request.send(msg)
if __name__ == '__main__':
    """
    1. simple way
    """
    #serv = TCPServer(('localhost', 8086), EchoHandler)
    
    """
	2. socketserver 可以让我们很容易的创建简单的TCP服务器。 
	需要注意的是，默认情况下这种服务器是单线程的，一次只能为一个客户端连接服务。
	如果你想处理多个客户端，可以初始化一个 ForkingTCPServer 或者是 ThreadingTCPServer 对象
	"""
    #serv = ThreadingTCPServer(('localhost', 8086), EchoHandler)

    """
    3. 使用fork或线程服务器有个潜在问题就是它们会为每个客户端连接创建一个新的进程或线程。 
    由于客户端连接数是没有限制的，因此一个恶意的黑客可以同时发送大量的连接让你的服务器奔溃。
    如果你担心这个问题，你可以创建一个预先分配大小的工作线程池或进程池。 
    你先创建一个普通的非线程服务器，然后在一个线程池中使用 serve_forever() 方法来启动它们。
    """
    workers = 6
    serv = TCPServer(('localhost', 8086), EchoHandler)
    for w in range(workers):
    	t = Thread(target=serv.serve_forever())
    	t.daemon = True  # 守护进程
    	t.start()
    

    serv.serve_forever()