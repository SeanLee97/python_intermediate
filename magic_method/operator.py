# -*- coding: utf-8 -*-

class Box(object):
    def __init__(self, w, h):
        self.w  = w 
        self.h  = h

    def getW(self):
        return self.w 

    def getH(self):
        return self.h

    def __eq__(self, obj):
        return self.w == obj.getW() and self.h == obj.getH()

    def __lt__(self, obj):
        return self.w < obj.getW() and self.w < obj.getH()

    def __gt__(self, obj):
        return self.w > obj.getW() and self.h > obj.getH() 

    def __egt__(self, obj):
        return self.w >= obj.getW() and self.h >= obj.getH() 

    def __lgt__(self, obj):
        return self.w <= obj.getW() and self.h <= obj.getH() 

if __name__ == '__main__':
    b1 = Box(1, 2)
    b2 = Box(1, 3)
    print(b1 == b2)
    print(b1 > b1)
    print(b1 < b2)
    print(b1 >= b2)
    print(b1 <= b2)