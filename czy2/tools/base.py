# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/7 16:24
# @Author  : Chengzy
# @File    : base.py
# @Software: PyCharm
import requests
from tools.public_request_api import TestRequest

from tools.creat_username_phone import createPhone
from tools.connect_db import con

def phone_isexist(iphone_number,serviceid):
    number = iphone_number
    if not number:
        number = createPhone()
        print ('number is ',number)
    sql = ''' select count(*) from usr_userinf where uif_mobile = '{}' '''.format(number)
    connect = con.select_db(sql,serviceid)[0]
    if connect[0] >= 1:
        return False,number#返回false说明手机号存在
    else:
        return True,number#返回true说明手机号不存在





class base():
    def __init__(self,serviceid):
        #print ('**************************serviceid',serviceid)
        serviceid = '105'
        if serviceid == '83':
            self.host = 'http://172.28.38.83'
        elif serviceid == '92':

            self.host = 'http://172.28.38.92'
        else:

            self.host = 'http://172.28.38.92'
        self.session = requests.session()
        self.request = TestRequest(self.session)

        self.headers = {'Content-Type': 'application/x-www-form-urlencoded',}
        self.base_data = {
            'productType': '31',
            'sourceProduct': '03',
            'sourceOrganizationNo': 'O20180507113389',
            'channel': '01',}
        self.data = {}

    def login(self,ip_number,pwd):
        '''先进行登录，登录成功拿到token
        '''
        temp_dict = {}
        temp_dict = dict(self.base_data,**temp_dict)
        self.data['mobile']=ip_number
        login = '/loan/login.do'
        url  = self.host+login
        temp_dict['mobile']=ip_number
        temp_dict['password']=pwd
        temp_dict['normal']='01'
        response = self.request.from_post(url,data=temp_dict,headers=self.headers)
        if response[0]['resultCode']=='00000000':
            self.base_data['token']=response[0]['user']['token']
            print('登录成功')
            #self.PBinfo()
            return True
        else:
            print ('登录失败')
            return False

    def control(self):
        con = '/loan/easyLoan/process/control.do'
        url  = self.host+con
        response = self.request.from_post(url,data=self.base_data,headers=self.headers)[0]
        # if response[0]["processModel"]['personNo']=='':
        #     self.auth()
        #     self.fill()
        # if response[0]["processModel"]['status']==-1:
        #     self.userCreditApplyInit()
        #     self.userCreditApply()
        return response