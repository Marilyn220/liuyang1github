# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/14 16:38
# @Author  : Chengzy
# @File    : RunCase.py
# @Software: PyCharm

import os

from HTMLTestRunner import HTMLTestRunner



class RunCases:
    def __init__(self, device,test_report_path):
        self.test_report_root = test_report_path
        self.device = device

        if self.device.get('serial') and self.device.get('ip'):
            self.test_report_path = os.path.join(self.test_report_root, self.device['model'].replace(':', '_').replace(' ', '')+'_'+self.device['ip'].replace(':','_'))
        else:
            self.test_report_path = os.path.join(self.test_report_root,
                                                 self.device['model'].replace(':', '_').replace(' ', '') + '_' +
                                                 self.device['serial'])
        if not os.path.exists(self.test_report_path):
            os.mkdir(self.test_report_path)
        self.file_name = os.path.join(self.test_report_path, 'TestReport.html')

    def get_path(self):
        return self.test_report_path

    def get_device(self):
        return self.device

    def run_testcase(self, cases):
        with open(self.file_name, 'wb') as file:
            runner = HTMLTestRunner(stream=file, title=self.device['model']+u'自动化测试报告', description=u'用例执行情况：')
            runner.run(cases)
            file.close()


if __name__=='__main__':
    d = [{u'product': None, u'udid': u'c7ea4c93-44:9e:f9:c1:a3:c7-vivo_Y66i_A', u'serial': u'c7ea4c93', u'brand': u'vivo', u'memory': {u'total': 2914744, u'around': u'3 GB'}, u'cpu': {u'hardware': u'Qualcomm Technologies, Inc MSM8917', u'cores': 4}, u'port': 7912, u'owner': None, u'version': u'7.1.2', u'presenceChangedAt': u'0001-01-01T00:00:00Z', u'agentVersion': u'0.5.2', u'provider': None, u'usingBeganAt': u'0001-01-01T00:00:00Z', u'model': u'vivo Y66i A', u'hwaddr': u'44:9e:f9:c1:a3:c7', u'display': {u'width': 720, u'height': 1280}, u'battery': {u'status': 5, u'scale': 100, u'temperature': 285, u'level': 100, u'acPowered': False, u'usbPowered': True, u'health': 2, u'voltage': 4383, u'wirelessPowered': False, u'technology': u'Li-ion', u'present': True}, u'sdk': 25},
{u'product': None, u'udid': u'3HX0217930010763-b0:55:08:9f:48:0d-MHA-AL00', 'ip': u'172.28.66.234:7557', u'brand': u'HUAWEI', u'memory': {u'total': 3809304, u'around': u'4 GB'}, u'cpu': {u'hardware': u'', u'cores': 7}, u'port': 7912, u'owner': None, u'version': u'8.0.0', u'presenceChangedAt': u'0001-01-01T00:00:00Z', u'agentVersion': u'0.5.2', u'serial': u'3HX0217930010763', u'provider': None, u'usingBeganAt': u'0001-01-01T00:00:00Z', u'model': u'MHA-AL00', u'hwaddr': u'b0:55:08:9f:48:0d', u'display': {u'width': 1080, u'height': 1920}, u'battery': {u'status': 5, u'scale': 100, u'temperature': 270, u'level': 100, u'acPowered': False, u'usbPowered': True, u'health': 2, u'voltage': 4347, u'wirelessPowered': False, u'technology': u'Li-poly', u'present': True}, u'sdk': 26}]

    l = len(d)
    for x in range(len(d)):
        r = RunCases(d[x])
