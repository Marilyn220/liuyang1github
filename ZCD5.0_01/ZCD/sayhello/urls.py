# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/25 17:11
# @Author  : Chengzy
# @File    : urls.py
# @Software: PyCharm
from .views import Hello
from ZCD.sayhello import sayhello

sayhello.add_url_rule('/',view_func=Hello.as_view('hello'))