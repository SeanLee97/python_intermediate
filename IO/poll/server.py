# -*- coding: utf-8 -*-

import socket
import select
import queue
from queue import Queue 

def run(host='localhost', port=8086):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        #设置IP地址复用
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.setblocking(False) #非阻塞
        server.bind((host, port))
        server.listen(5)
        message_queues = {}
        timeout = 1000

        """
        POLLIN    There is data to read
        POLLPRI    There is urgent data to read
        POLLOUT    Ready for output: writing will not block
        POLLERR    Error condition of some sort
        POLLHUP    Hung up
        """
        READ_ONLY = (select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
        READ_WRITE = (READ_ONLY | select.POLLOUT)

        # create poll
        poller = select.poll()
        poller.register(server, READ_ONLY)

        # file description dict
        fd_to_server = {server.fileno(): server, }
        while True:
            print("wait for next event")
            events = poller.poll(timeout)
            print("Debug>>", events)
            # poll轮询
            for fd, flag in events:
                s = fd_to_server[fd]
                if flag & (select.POLLIN | select.POLLPRI):
                    if s is server:
                        conn, addr = s.accept()
                        print("Connection to client address ", addr)
                        conn.setblocking(False) #非阻塞

                        if conn not in fd_to_server:
                            fd_to_server[conn.fileno()] = conn
                        poller.register(conn, READ_ONLY)
                        message_queues[conn] = Queue()
                    else:
                        data = s.recv(1024)
                        if data:
                            print("recvd", data, "from", s.getpeername())
                            message_queues[s].put(data)
                            #修改读取到消息的连接到等待写事件集合
                            poller.modify(s, READ_WRITE)
                        else:
                            print("closing", s.getpeername())
                            poller.unregister(s)
                            del message_queues[s]

                elif flag & select.POLLHUP:
                    # 挂起
                    print("closing", s.getpeername(), "(HUP)")
                    #在epoll中注销客户端的文件句柄
                    poller.unregister(s)

                elif flag & select.POLLOUT:
                    # ready to write
                    try:
                        next_msg = message_queues[s].get_nowait()
                    except queue.Empty:
                        print(s.getpeername(), "queue empty")
                        # 修改文件句柄为读事件
                        poller.modify(s, READ_ONLY)
                    else:
                        print("sending ", next_msg, "to", s.getpeername())
                        s.sendall(next_msg)

                elif flag & select.POLLERR:
                    # error
                    poller.unregister(s)
                    del message_queues[s]

        poller.unregister(server)
        poller.close()

if __name__ == '__main__':
    run()