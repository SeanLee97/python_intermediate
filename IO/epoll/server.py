# -*- coding: utf-8 -*-

import socket
import select
import queue
from queue import Queue

def run(host='localhost', port=8086):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    	#设置IP地址复用
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.setblocking(False)
        server.bind((host, port))
        server.listen(5)
        timeout = 1000

        epoll = select.epoll()
        """
        EPOLLIN    Available for read
        EPOLLOUT    Available for write
        EPOLLPRI    Urgent data for read
        EPOLLERR    Error condition happened on the assoc. fd
        EPOLLHUP    Hang up happened on the assoc. fd
        EPOLLET    Set Edge Trigger behavior, the default is Level Trigger behavior
        """
        READ_ONLY = (select.EPOLLIN | select.EPOLLPRI | select.EPOLLHUP | select.EPOLLERR)
        READ_WRITE = (READ_ONLY | select.EPOLLOUT)
        epoll.register(server.fileno(), READ_ONLY)
        message_queues = {}
        fd_to_server = {server.fileno(): server, }

        while True:
            print("wait for event")
            events = epoll.poll(timeout)
            print("Debug>>", events)

            if not events:
                print("timeout, repolling...")
                continue

            for fd, flag in events:
                s = fd_to_server[fd]
                if s is server:
                    conn, addr = s.accept()
                    print("Connected to client address", addr)
                    conn.setblocking(False)  # set non-block
                    epoll.register(conn.fileno(), select.EPOLLIN)
                    fd_to_server[conn.fileno()] = conn
                    message_queues[conn] = Queue()
                elif flag & select.EPOLLHUP:
                    print("client close")
                    #在epoll中注销客户端的文件句柄
                    epoll.unregister(fd)
                    #关闭客户端的文件句柄
                    fd_to_server[fd].close()
                    #在字典中删除与已关闭客户端相关的信息
                    del fd_to_server[fd]
                elif flag & select.EPOLLIN:
                    # recv data
                    data = s.recv(1024)
                    if data:
                        print("recvd ", data, "from", s.getpeername())
                        message_queues[s].put(data)
                        #修改读取到消息的连接到等待写事件集合(即对应客户端收到消息后，再将其fd修改并加入写事件集合)
                        epoll.modify(fd, READ_WRITE)
                elif flag & select.EPOLLOUT:
                    try:
                        next_msg = message_queues[s].get_nowait()
                    except queue.Empty:
                        print(s.getpeername, "queue empty")
                        # 修改文件句柄为读事件
                        epoll.modify(fd, READ_ONLY)
                    else:
                        print("send", data, "to", s.getpeername())
                        s.sendall(next_msg)
                elif flag & select.POLLERR:
                    # error
                    epoll.unregister(fd)
                    del message_queues[s]

        epoll.unregister(server.fileno())
        epoll.close()

if __name__ == '__main__':
	run()