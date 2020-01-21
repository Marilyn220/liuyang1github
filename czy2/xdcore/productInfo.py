# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/26 14:13
# @Author  : Chengzy
# @File    : productInfo.py
# @Software: PyCharm

import time,random
import os
from xdcore.base import base


import json

class productInfo(base):

    def bindcard(self):#VALIDATE  BIND_SUCCESS
        temp_dict = {}
        temp_dict = dict(self.pub_xcored, **temp_dict)
        temp_dict['result'] = {"errorcode": None, "errormsg": None, "issms": True, "remark": None, "smscode": "666666",
             "status": "TO_VALIDATE", "yborderid": "AP273485238611480576"}
        temp_dict['timestamp'] = self.current_milli_time()
        print ('temp_dict: is ',temp_dict)
        return json.dumps(temp_dict)

    def confirmcard(self):
        temp_dict = {}
        temp_dict = dict(self.pub_xcored, **temp_dict)
        temp_dict['result'] = {"errorcode": None, "errormsg": None, "issms": False, "remark": None, "smscode": None,
                "status": "BIND_SUCCESS", "yborderid": "AP273485238611480576"}
        temp_dict['timestamp'] = self.current_milli_time()
        print('temp_dict: is ', temp_dict)
        return json.dumps(temp_dict)


if __name__=='__main__':
    p = productInfo()
    print (p.orders('20190304142144289931'))