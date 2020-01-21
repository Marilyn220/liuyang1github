# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2018/12/21 11:31
# @Author  : Chengzy
# @File    : test_home_o.py
# @Software: PyCharm
import yaml

f = open(r'D:\chengzhengyang\PycharmProjects\testa\TESTYAML\product01\Chengzy\HOME1.yaml')

y = yaml.load(f)

f.close()
#print y
#d = u2.connect_usb()
#d.debug = True
#d.info
#d.screen_on()

#d.screen_off()

#d.press("power")
#d.app_start("com.qianbao.guanjia.easyloanfast")
#d.app_info("com.qianbao.guanjia.easyloanfast")
#d.implicitly_wait(10)
#d(resourceId=y['TestInfo'][0]['element_info']).click()
#print("wait timeout", d.implicitly_wait())


#u = u2.connect_usb()
#u.healthcheck()
#d = u.session("com.qianbao.guanjia.easyloanfast")
#d.set_fastinput_ime(True)
#d(resourceId=y['TestInfo'][0]['element_info']).click()
#d(resourceId="com.qianbao.guanjia.easyloanfast:id/et_phone").send_keys("15811142327")

'''
import unittest

class test_home02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(test_home02, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(test_home02, cls).tearDownClass()

    def test003(self):
        print 'test001'

    def test004(self):
        print 'test002'


'''

