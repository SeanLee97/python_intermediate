# -*- coding: utf-8 -*-

"""
客户端，连接
"""

import socket

host='localhost'
port=8086
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((host, port))
	s.sendall(b'hello world') # send binary data
	data = s.recv(1024)
print("recvd", repr(data)) # repr() 将任意值转为字符串, 用str也可
