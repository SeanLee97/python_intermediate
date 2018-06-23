# -*- coding: utf-8 -*-

"""说明：
select
"""

import select
import socket
from queue import Queue  # message queue
import time

def run(host='localhost', port=8086):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # https://docs.python.org/3/library/socket.html#socket.socket.setblocking 
        # equivalent to => server.settimeout(0.0)
        server.setblocking(False) 
        server.bind((host, port))
        server.listen(5)
        rlist = [server]  # read list wait until ready for reading
        wlist = []        # write list wait until ready for writing
        message_queues = {}

        while rlist:
        	# 轮询
        	
            print("wait for event")
            # select.select(rlist, wlist, xlist[, timeout])
            # here xlist equivalent to rlist
            readable, writeable, exceptional = select.select(rlist, wlist, rlist)

            if not (readable or writeable or exceptional):
                print("Time out !")
                break
            for s in readable:
                if s is server:
                    conn, addr = s.accept()
                    print("connecting from client address ", addr)
                    conn.setblocking(False)
                    rlist.append(conn)
                    message_queues[conn] = Queue()  # message queue
                else:
                    data = s.recv(1024)
                    if data:
                        # s.getpeername() : Return the remote address to which the socket is connected
                        print("received", data, "from", s.getpeername())
                        message_queues[s].put(data)
                        if s not in wlist:
                            wlist.append(s)
                    else:
                        print("closing", addr)
                        if s in wlist:
                            wlist.remove(s)
                        rlist.remove(s)
                        del message_queues[s]

            #print("Debug ", writeable)
            for s in writeable:
                try:
                    # get_nowait()
                    # Remove and return an item from the queue.
                    next_msg = message_queues[s].get_nowait()
                except Exception as e:
                    print("", s.getpeername(), 'queue empty')
                    wlist.remove(s)
                else:
                    print("sending ", next_msg, " to ", s.getpeername())
                    s.sendall(next_msg)
            for s in exceptional:
                print("exception condition on ", s.getpeername())
                rlist.remove(s)
                if s in wlist:
                    wlist.remove(s)
                s.close()
                del message_queues[s]

if __name__ == '__main__':
	run()