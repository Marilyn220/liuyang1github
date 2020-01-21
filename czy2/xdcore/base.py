# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/26 14:12
# @Author  : Chengzy
# @File    : base.py
# @Software: PyCharm
import time
class base:
    def __init__(self):

        self.pub_xcored = {"status":"20000108","message":None,"result":{},"timestamp":1551266161858,"retCode":"200","info":None}

        self.current_milli_time = lambda: int(round(time.time() * 1000))#13位


