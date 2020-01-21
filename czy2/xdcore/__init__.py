# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/8 14:22
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint
xdcore = Blueprint('xdcore',__name__,url_prefix='/xdcore',template_folder='templates',static_folder='static')
from . import views