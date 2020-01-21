# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/25 19:39
# @Author  : Chengzy
# @File    : errors.py
# @Software: PyCharm
from flask import render_template
from . import sayhello

@sayhello.errorhandler(404)
def page_not_found(e):
    return render_template('sayhello/errors/404.html'),404