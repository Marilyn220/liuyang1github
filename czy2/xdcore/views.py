# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/8 14:22
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm

from . import xdcore
from .productInfo import productInfo
from flask import request
import requests,json

#公共的post请求
def posturl(url,data):
    r = requests.post(url,json=data,verify=False)
    return r.text



p = productInfo()
#核心绑卡鉴权
@xdcore.route('/v1/payagent/ybpay/v1/bindcard',methods=["GET","POST"])
def bindcard():
    if request.method=="POST":
        print(request.url)
        print('走的是post请求')
        print('请求参数如下：', request.json, type(request.json))
        r = p.bindcard()
        return r
    else:
        return 'bindcard info get '

@xdcore.route('/v1/payagent/ybpay/v1/confirmcard',methods=["GET","POST"])
def confirmcard():
    if request.method=="POST":
        print (request.url)
        print('走的是post请求')
        print('请求参数如下：', request.json, type(request.json))
        r = p.confirmcard()
        return r
    else:
        return 'confirmcard info get '




@xdcore.route('/<path:subpath>',methods=["GET","POST"])
def path(subpath):
    if request.method=="POST":
        url  = 'https://sit4-apis.qianbao.com'+request.full_path
        print ('********************')
        print ('本次请求的地址为',url)
        print ('********************')
        datas = request.json
        Core = posturl(url, datas)
        print ('请求参数',datas)
        print ('响应参数',Core)
        return Core
    else:
        return '%s 该路径请求不支持post以外的方式'%subpath
