# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/6 15:12
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
registerUser = Blueprint('registerUser',__name__,url_prefix='/registerUser',template_folder='templates',static_folder='static')
from . import views