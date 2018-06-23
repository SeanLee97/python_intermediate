# -*- coding: utf-8 -*-

"""描述
 用非递归方式解决递归问题, 一般用辅助栈来实现
"""

# 1.
def recursive1(n):
    if n == 0:
        return n+1
    return n*recursive1(n//2)

def iter1(n):
    stack = []
    while n > 0:
        stack.append(n)
        n //= 2
    f = 1
    while len(stack) > 0:
        f = f*stack.pop()
    return f

print(recursive1(4))
print(iter1(4))
