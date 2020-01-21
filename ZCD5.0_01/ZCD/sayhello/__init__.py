# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/25 17:10
# @Author  : Chengzy
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
sayhello = Blueprint('sayhello',__name__,url_prefix='/sayhello')
from . import urls,errors