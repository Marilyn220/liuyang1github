# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/27 17:23
# @Author  : Chengzy
# @File    : bank.py
# @Software: PyCharm

import requests

def get_bank(cardNo):
    url = "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json"
    params = {
        "_input_charset": "utf-8",
        "cardNo": cardNo['cardNo'],
        "cardBinCheck": "true",
    }
    bank = requests.get(url=url, params=params,verify=False).json()
    #print (bank,type(bank))
    #print (bank['cardType'])
    temp_dict={}
    if bank['messages']==[]:
        temp_dict['cardType'] = bank['cardType']
        temp_dict['bank'] = bank['bank']
        temp_dict['key'] = bank['key']
        return temp_dict
    else:
        return temp_dict

if __name__=='__main__':

    print (get_bank({'cardNo':"6225880111111111"}))
    print (get_bank({'cardNo':"6225880111111111"}))
