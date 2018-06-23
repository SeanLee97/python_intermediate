# -*- coding: utf-8 -*-

import ctypes
lib = ctypes.cdll.LoadLibrary('./cbacken.so')

class Wrapper(object):
    def __init__(self):
        self.obj = lib.cbacken_new()

    def sort(self, lst):
        n = len(lst)
        # init arr
        cb_ARR = ctypes.c_int * n
        cb_arr = cb_ARR()
        for i in range(n):
            if not isinstance(lst[i], int):
                raise ValueError("Only support Integer Array")

            cb_arr[i] = lst[i]
        # init int
        cb_N = ctypes.c_int
        cb_n = cb_N()
        cb_n = n
        # sort
        lib.cbacken_sort(self.obj, cb_arr, cb_n)
        nlst = [x for x in cb_arr]
        return nlst

if __name__ == '__main__':
    wp = Wrapper()
    print(wp.sort([2, 1, 4, 3]))
