# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/26 17:44
# @Author  : Chengzy
# @File    : urls.py
# @Software: PyCharm

from .views import Loan_views_one
from loan import loan

loan.add_url_rule('/index',view_func=Loan_views_one.as_view('loan'))