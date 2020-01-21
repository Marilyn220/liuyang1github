# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/26 17:30
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm
from flask import render_template,flash,redirect,url_for
from flask.views import  MethodView
from .forms import loan_forms_one
from .loan_tools import submit_core

class Loan_views_one(MethodView):
    def get(self):
        form = loan_forms_one()
        return render_template('loan/index.html',form=form)


    def post(self):
        form = loan_forms_one()
        if form.validate():
            ip_number = form.iphone_number.data
            pwd = form.password.data
            timelimit = form.timelimit.data
            money = form.money.data
            sub = submit_core('83')
            if sub.checkCardUsable(ip_number,pwd,timelimit,money):
                return render_template('loan/index.html',succeed='提交成功',form=form)
            else:
                return render_template('loan/index.html',error='提交进件失败',form=form)
        return render_template('loan/index.html',form=form)


