# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/25 17:15
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm
from flask import render_template,flash,redirect,url_for
from flask.views import  MethodView
from .forms import HelloForm
from ZCD.models import Message
from ZCD import db

class Hello(MethodView):
    def get(self):
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        form = HelloForm()
        return render_template('sayhello/index.html',form=form,messages=messages)

    def post(self):
        messages = Message.query.all()
        form = HelloForm()
        if form.validate():
            name = form.name.data
            body = form.body.data
            messages = Message(name=name,body=body)
            db.session.add(messages)
            db.session.commit()
            flash('Your message have been sent to the world!')
            return redirect(url_for('sayhello.hello'))
        return render_template('sayhello/index.html', form=form, messages=messages)
