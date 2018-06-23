# socket

## 创建socket
s = socket.socket([family[, type[, proto]]])

- family 地址簇
    - socket.AF_INET   IPv4(默认)
    - socket.AF_INET6  IPv6
    - socket.AF_UNIX   只能够用于单一的UNIX系统进程间通信
- type 类型
    - socket.SOCK_STREAM    面向连接，TCP
    - socket.SOCK_DGRAM     面向数据报（无连接），UDP
    - socket.SOCK_RAW       原始套接字，普通套接字无法处理ICMP，IGMP等网络报文，而sock.SOCK_RAW可以，其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头
    - socket.SOCK_RDM       是一种可靠UDP形式，保证交付数据报但不保证顺序
    - socket.SOCK_RAM       用来对原始协议的低级访问
    - socket.SOCK_SEQPACKET 可靠的连续数据包服务
- protol 协议
    - 0 默认为0，自动选择协议

## 常用函数

### 绑定地址
```python
s.bind((host, port))
```
### 监听
```python
s.listen(backlog)
# backlog 指定在拒绝连接之前可以挂起的最大连接数 
```
可通过
```bash
netstat -tnl | grep xxxx
```
查看tcp连接状态

### 设置阻塞/非阻塞
```python
s.setblocking(bool)
# True 阻塞， False 非阻塞
# 区别：如果设置非阻塞，当accept()和recv()时一旦无数据则报错
```

### 接收连接
```python
conn, addr = s.accept()

# 接收连接并返回连接和客户端地址,conn是新的套接子对象，可用来接收和发送数据
```
### 连接到指定地址

```python
# 方式1
s.connect((host, port))

# 方式2，与1的区别是有返回值，0表示返回成功，其他表示错误代码
status = s.connect_ex((host, port))
if status == 0:
    print("ok")
```

### 关闭套接字
```python
s.close()
```

### 接收套接字数据
```python
# 1. 常用于TCP
s.recv(bufsize[, flag])
# bufsize 设置最多可接收的数量，数据以字符串形式返回

# 2. 常用于UDP
data, address = s.recvfrom(bufsize[, flag])
# 返回值是data，address
```

### 发送数据
```python
# 1.
s.send(string[, flag])
# 将string中的数据发送到连接的套接字。返回值是要发送的字节数量, 该数量可能小于string的字节大小。即：可能未将指定内容全部发送。

# 2.
s.sendall(string[, flag])
# 将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。内部通过递归调用send，将所有内容发送出去。

# 3. 主要用于UDP
s.sendto(string[, flag], (host, port))
# 将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。
```

### 设置套接字操作的超时期
```python
s.settimeout(timeout)
# 设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。
# s.settimeout(0) 和 s.setblocking(False) 功能相同
# s.settimeout(None) 和 s.setblocking(True) 功能相同
```

### 返回套接字地址
```python
# 1.返回远程地址
s.getpeername()

# 2.返回本身地址
s.getsockname()
```

### 获取套接字文件描述符
```python
s.fileno()
```

# socketserver
是一个高级封装库，封装了IO多路复用，以及多线程多进程，从而实现并发处理多个客户端请求的socket服务端
更多请参照目录源码实例


