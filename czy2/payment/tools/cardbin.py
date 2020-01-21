# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/27 16:53
# @Author  : Chengzy
# @File    : cardbin.py
# @Software: PyCharm

import json
from payment.tools.bank import get_bank

def dbin(data):
    print ('data is :',data)
    # r = get_bank(data)
    # print (r)
    # d = {"bankCode": r['bank'], "bankName": "招商银行", "cardBin": r['key'][:7], "cardName": "一卡通(银联卡)", "cardNo": r['key'],
    #  "responseCode": "00000000", "responseDesc": "成功", "typeCode": r['cardType'], "typeName": "借记卡"}

    d = {"bankCode": 'CMB', "bankName": "招商银行", "cardBin": data['cardNo'][:7], "cardName": "一卡通(银联卡)", "cardNo": data['cardNo'],
         "responseCode": "00000000", "responseDesc": "成功", "typeCode": "DC", "typeName": "借记卡"}
    return json.dumps(d)
