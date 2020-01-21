# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/6 15:15
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm

from . import registerUser
from flask import request,render_template
from czy2.tools.base import phone_isexist
from .tools.funcAll import main


@registerUser.route('/',methods=["GET","POST"])
def register():

    if request.method == "POST":
        print ('register  走的是post')
        print (request.form['ip'])
        phone_number =  request.form['ip']
        serviceid = request.form['id']
        print (serviceid,'11111111111111')
        p = phone_isexist(phone_number,serviceid)
        if not p[0]:
            return render_template('register/index.html', error='手机号:%s 已存在，请重新输入手机号' % p[1])
        else:
            m = main(serviceid)
            print (serviceid)
            result = m.regist(p[1])
            print (result)
            if result:
                return render_template('register/index.html', succeed='注册成功,手机号为:%s'%p[1])
            else:
                return render_template('register/index.html', error='注册失败,手机号为:%s'%p[1])

    else:
        print ('register  走的是get')
        return render_template('register/index.html')
