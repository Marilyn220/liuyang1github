# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2018/12/28 17:18
# @Author  : Chengzy
# @File    : test_home.py
# @Software: PyCharm
import os,unittest,sys
#单用例测试时打开以下两行
from uiautomator2 import UiObjectNotFoundError

#PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
#sys.path.append(r'D:\chengzhengyang\PycharmProjects\QBXD3.0')

from Public.DrObj import DrObj
#from Public.decorator import *
#from Public.Logs import Log
from PO.Home_page import Home_page


class test_home(unittest.TestCase,DrObj):

    @classmethod
    def setUpClass(cls):

        cls.d.healthcheck()
        cls.d.app_start('com.qianbao.guanjia.easyloan')#com.qianbao.guanjia.easyloanfast
        #com.qianbao.guanjia.easyloan
        cls.h = Home_page()


    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop("com.qianbao.guanjia.easyloan")

    def testh(self):

        self.h.my_button()
        self.h.head_button()
        self.h.et_phone('1581111111')

    def testy(self):
        print ('testy')
if __name__=="__main__":
    unittest.main(verbosity=2)