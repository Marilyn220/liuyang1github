# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/22 15:41
# @Author  : Chengzy
# @File    : urls.py
# @Software: PyCharm

from ZCD import app
#from .main_views import Index
from ZCD.manager import Index

app.add_url_rule('/index',view_func=Index.as_view('index'))