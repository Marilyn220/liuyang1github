# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/14 18:50
# @Author  : Chengzy
# @File    : CaseStrategy.py
# @Software: PyCharm

import unittest


class CaseStrategy:
    def __init__(self):
        self.case_pattern = 'test*.py'

    def collect_cases(self, case_path):
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
        suite = unittest.TestSuite()
        suite.addTest(discover)
        return suite
