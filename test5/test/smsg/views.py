# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/18 11:22
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm

from . import smsg
from flask import request
import re,os
import json
@smsg.route('/p/send',methods=['GET','POST'])
def hello():
    te_dict = {}
    if request.method == 'POST':
        messages = request.form
        messages_dict = messages.to_dict()
        r = '(\d+)'
        smsCode = re.findall(r,messages_dict['content'])
        te_dict['smsCode'] = ''.join(smsCode)
        te_dict['mobiles'] = messages_dict['mobiles']

    file_path = os.path.split(os.path.realpath(__file__))[0]
    p = os.path.join(file_path,'smsCode.json')
    #with open(file_path + '/smsCode.json', 'w+') as f:
    with open(p, 'w+') as f:
        l = json.dump(te_dict,f)
        print ('短信验证码的数据为：',te_dict)
    return 'hello,smsg'
