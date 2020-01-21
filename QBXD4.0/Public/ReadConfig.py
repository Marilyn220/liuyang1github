# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/14 17:57
# @Author  : Chengzy
# @File    : ReadConfig.py
# @Software: PyCharm

import configparser
import os,sys


class ReadConfig:

    def __init__(self,proDir):
        self.cf = configparser.ConfigParser()
        self.proDir = proDir

    def get_ips(self):
        ips = self.cf.get("connect_devives_method","ips")
        if ips=='':
            return []
        else:
            return ips.split(',')

    def get_log_path(self,testcase_path):
        TC_path = self.get_testcase_path(testcase_path)
        log_path = self.cf.get("log_path","log_path")
        log_file_path = TC_path+log_path
        if os.path.exists(log_file_path):
            return log_file_path
        else:
            os.mkdir(log_file_path)
            return log_file_path


    def get_testcase_path(self,configPath):
        if os.path.exists(configPath):
            self.cf.read(configPath)
            case_path = self.cf.get("TestCase_path","TC_path")
            testcase_path = self.proDir+case_path
            if os.path.exists(testcase_path):
                return testcase_path
            else:
                return False
        else:
            return False

    def get_testreport(self,testcase_path):
        TC_path = self.get_testcase_path(testcase_path)
        tr = self.cf.get("TestReport_path","TestReport_path")
        testReport = TC_path+tr
        if os.path.exists(testReport):
            return testReport
        else:
            os.mkdir(testReport)
            return testReport


if __name__=="__main__":
    rc = ReadConfig('D:\chengzhengyang\PycharmProjects\QBXD3.1')


    print (rc.get_testcase_path(r'D:\chengzhengyang\PycharmProjects\QBXD3.1\baseconfig.ini'))



