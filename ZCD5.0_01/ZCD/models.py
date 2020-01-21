# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/25 11:15
# @Author  : Chengzy
# @File    : models.py
# @Software: PyCharm
import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=False,nullable=False)
    #password = db.Column(db.String(30), unique=False, nullable=False)

    def __repr__(self):
        return "<User %r>"%self.username


class Test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)