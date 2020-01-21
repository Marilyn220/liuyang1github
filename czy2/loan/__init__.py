# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/26 17:30
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
loan = Blueprint('loan',__name__,url_prefix='/loan')
from . import views,urls,forms