# -*- coding: utf-8 -*-

import ctypes

lib = ctypes.cdll.LoadLibrary('./calculate.so')

class Calculate(object):
    def __init__(self):
        lib.Calculate_add.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        lib.Calculate_add.restype = ctypes.c_int;

        self.obj = lib.Calculate_new()

    def add(self, x, y):
        return lib.Calculate_add(self.obj, x, y)

if __name__ == '__main__':
    cal = Calculate()
    print(cal.add(3, 2))

