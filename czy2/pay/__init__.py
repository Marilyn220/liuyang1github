# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/18 11:11
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
pay = Blueprint('pay',__name__,url_prefix='/pay',template_folder='templates',static_folder='static')
from . import views