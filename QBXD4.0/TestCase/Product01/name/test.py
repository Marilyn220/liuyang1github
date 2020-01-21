# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/25 15:41
# @Author  : Chengzy
# @File    : base_page.py
# @Software: PyCharm

class test:
    print 'ffffffffff'
    def __init__(self):
        print 'aaaaaaaaaaaaa'
    @classmethod
    def te(cls):
        cls.a = 123
        #da = cls(cls.a)
        return cls.a


    def d(self):
        print self.a

r = test.te()

print r