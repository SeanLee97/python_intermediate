# -*- coding: utf-8 -*-

"""说明：
基本服务端代码
"""

import socket

def run(host='localhost', port=8086):
    # socket.socket([family[, type[, proto]]])
    # family: 套接字家族可以使用AF_UNIX或者AF_INET等
    # type: 套接字类型可以是面向连接的（socket.SOCK_STREAM）TCP 和无连接的(socket.SOCK_DGRAM) UDP等
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
        s.bind((host, port))  # 绑定连接
        s.listen() # 监听状态, netstat -tnl | grep 8086 ,可查看到监听状态
        conn, addr = s.accept() # 建立客户端连接
        with conn:
            while True:
                data = conn.recv(1024)
                print("connect host", addr)
                #conn.send("Welcome to socket test")  # 给客户端发送数据
                if data:
                    conn.sendall(data)
                else:
                    print("not any data")
                    break

if __name__ == '__main__':
    run()
