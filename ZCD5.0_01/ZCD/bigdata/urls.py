# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/22 15:56
# @Author  : Chengzy
# @File    : urls.py
# @Software: PyCharm

from .views import *
from ZCD.bigdata import bigdata

#bigdata.add_url_rule('/index',view_func=index)
bigdata.add_url_rule('/login',view_func=Login.as_view('login'))