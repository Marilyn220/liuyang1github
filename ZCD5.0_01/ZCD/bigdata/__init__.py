# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/22 15:52
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
bigdata = Blueprint('bigdata',__name__,url_prefix='/qbaquila_web',static_folder='static')
from . import urls