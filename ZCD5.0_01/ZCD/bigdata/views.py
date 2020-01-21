# -*- coding: utf-8 -*-
# python 2.7b
# @Time    : 2019/3/22 15:55
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm
from flask.views import MethodView
from flask import render_template,flash,redirect,url_for
from .forms import *
from ZCD.models import *
# def index():
#     return render_template('index.html')


class Login(MethodView):
    def get(self):
        form = LoginFrom()
        form.username(style='width: 200px;', class_='bar')
        return render_template('bigdata/login.html',form=form)

    def post(self):
        form = LoginFrom()
        if form.validate():
            form.username(style='width: 200px;', class_='bar')
            username = form.username.data
            u = User(username=username)
            db.session.add(u)
            db.session.commit()
            flash('Welcome home, %s!' % username)
            print (url_for('index'))
            return redirect(url_for('index'))
        else:
            return render_template('bigdata/login.html',form=form)