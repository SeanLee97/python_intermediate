# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_DGRAM

with socket(AF_INET, SOCK_DGRAM) as s:
    s.sendto(b'hello world', ('localhost', 8086))
    msg = s.recvfrom(1024)
    print(msg)