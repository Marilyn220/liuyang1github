# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/22 15:40
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm
import os,sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("ZCD")
#app.config.from_object('conf.dev')

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'test.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
db = SQLAlchemy(app)

from ZCD import urls
