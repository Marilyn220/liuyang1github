# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/25 15:58
# @Author  : Chengzy
# @File    : conf.py.py
# @Software: PyCharm

import os,sys
from ZCD import app



WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

class dev:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'test.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG = True




