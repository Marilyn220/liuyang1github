# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/18 11:22
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm
#http://172.17.6.210:5004
#http://sit-apis.csdnpay.com
from . import payment
from .tools.cardbin import dbin
from flask import request

@payment.route('/v1/basedata/cardbin',methods=['GET','POST'])
def cardbin():
    if request.method=="POST":
        print ('*****************绑卡请求**************')
        print('走的是post请求')

        print('请求参数如下：', request.get_data(),type(request.get_data()))
        print('url:',request.url)
        carno = str(request.get_data(), encoding='utf-8')
        carnolist = carno.split('=')
        d = {}
        d[carnolist[0]]=carnolist[1]
        print (d)
        r = dbin(d)
        print ('返回信息如下：',r)
        return r
    else:
        return 'bindcard info get '



