# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/6 14:11
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

createUser = Blueprint('createUser',__name__,url_prefix='/createUser',template_folder='templates',static_folder='static')

from . import views