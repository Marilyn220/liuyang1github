# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/18 14:07
# @Author  : Chengzy
# @File    : Home_page.py
# @Software: PyCharm
from Public.decorator import *
from base_page import base_page
class Home_page(base_page):
    my_button_ele = u'我的'
    head_button_ele = 'com.qianbao.guanjia.easyloan:id/tv_personal_login'
    et_phone_ele = 'com.qianbao.guanjia.easyloan:id/et_phone'



    @step(my_button_ele)
    def my_button(self):
        return self.click(self.my_button_ele)

    @step(head_button_ele)
    def head_button(self):
        return self.click(self.head_button_ele)

    @step(et_phone_ele)
    def et_phone(self,msg):
        return self.send_key(self.et_phone_ele,msg)

if __name__=='__main__':

    h = Home_page()
    print (h.my_button())
    print (h.head_button())
    print (h.et_phone())