# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/7 10:37
# @Author  : Chengzy
# @File    : funcAll.py
# @Software: PyCharm

from tools.base import base
import os , json


class main(base):

    def regist(self,ip_number):
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)

        getImageCode = '/loan/sms/getImageCode.do?mobile={}'.format(ip_number)#获取图片验证码
        url = self.host + getImageCode
        print ('获取图片验证码')
        response = self.request.get_imgcode_get(url)
        #print(response)
        print(response['imageCode'])
        temp_dict['imageCode'] = response['imageCode']

        getMobileMessage = '/loan/sms/getMobileMessage.do'#获取短信验证码
        url = self.host + getMobileMessage

        temp_dict['mobile'] = ip_number
        response = self.request.from_post(url, data=temp_dict, headers=self.headers)

        print (response)

        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        smsg = PATH('../../smsg/')
        #smsgpath = smsg+'/smsCode.json'
        #print (smsgpath)
        smsgpath1 = os.path.join(smsg,'smsCode.json')
        print (smsgpath1)
        with open(smsgpath1,'r') as f:
            code = json.load(f)['smsCode']
        print (code)

        registerUser = '/loan/register/registerUser.do'
        url = self.host + registerUser
        #messageCode = input('短信验证码:')
        temp_dict.pop('imageCode')
        temp_dict['messageCode'] = code
        temp_dict['password'] = '123456a'
        response = self.request.from_post(url, data=temp_dict, headers=self.headers)
        print(response)
        if response[0]['resultCode'] == '00000000':
            print('注册成功')
            return True
        else:
            print('注册失败')
            return False





if __name__ == '__main__':

    m = main('83')
    print (m.regist(13111113333))







