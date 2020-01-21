# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/7 16:18
# @Author  : Chengzy
# @File    : funcAll.py
# @Software: PyCharm
import json
import os
from tools.creat_username_phone import createusername,gennerator,createPhone
from tools.base import base
from tools.connect_db import con


def iscertauth(iphone_number):
    sql = '''SELECT COUNT(*) from usr_personbaseinf where ubf_userno in (SELECT UIF_USERNO FROM usr_userinf where UIF_MOBILE='{}')'''.format(iphone_number)
    connect = con.select_db(sql)[0]
    if connect[0] >= 1:
        return False
    else:
        return True





class main(base):

    def auth(self):
        #调用实名认证接口
        authCertInfo = '/loan/authenticate/authCertInfo.do'
        url = self.host+authCertInfo
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)
        temp_dict['personName']=createusername()#生成随机姓名
        temp_dict['certType'] = '10'
        print (gennerator())
        temp_dict['certNo'] = gennerator()#随机生成身份证号码
        response = self.request.from_post(url,data=temp_dict,headers=self.headers)[0]
        print ('auth:',response)
        if response['resultCode'] == '00000000':
            usrinfo = {}
            usrinfo['personName'] = temp_dict['personName']
            usrinfo['certNo'] = temp_dict['certNo']
            with open('User/user_tools/userinfo.json','w') as f:
                json.dump(usrinfo,f)
                f.close()
            return True,'姓名为:%s,身份证号:%s'%(usrinfo['personName'],usrinfo['certNo'])
        else:
            return False,response['resultMessage']


    def fill(self):
        #个人详细信息与两个联系人
        #self.login(ip_number,pwd)
        control = self.control()
        if control['resultCode'] == '00000000':
            self.data['applyNo']=control['processModel']['loanCreditApply']['applyNo']

        fillContactInformationAuth = '/loan/fillInformation/fillContactInformationAuth.do'
        url  = self.host+fillContactInformationAuth
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)
        temp_dict['applyNo']=self.data['applyNo']
        temp_dict['homeAddress']='北京市北京市东城区 1111'
        temp_dict['mobileFirst'] = createPhone()
        temp_dict['personNameFirst'] = createusername()
        temp_dict['contactTypeFirst'] = '2'
        temp_dict['mobileSecond'] = createPhone()
        temp_dict['personNameSecond'] = createusername()
        temp_dict['companyName'] = '2222'
        temp_dict['contactTypeSecond'] = '6'
        temp_dict['homeProvinceCode'] = '110000'
        temp_dict['homeCityCode'] = '110100'
        temp_dict['homeDistrictCode'] = '110101'
        temp_dict['authType'] = '37'
        response = self.request.from_post(url,data=temp_dict,headers=self.headers)[0]
        print ('fill返回:',response)
        if response['resultCode'] == '00000000':
            return True
        else:
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


    def cardbin(self,iphone_number,accountNo):
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)
        temp_dict['accountNo'] = accountNo
        temp_dict['accountType'] = 'DC'
        temp_dict['mobile']=iphone_number
        temp_dict['bankNo']='CMB'
        temp_dict['sceneCode'] = 'S01'
        car = '/loan/bindCard/getMobileCodeForBind.do'
        url = self.host+car
        response = self.request.from_post(url,data=temp_dict,headers=self.headers)[0]
        print ('aaaaaaaaaaa',response)
        if response['resultCode'] == '00000000':
            return True
        else:
            return False

    def toBind(self):
        tobind = '/loan/bindCard/toBind.do'
        url = self.host+tobind
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)
        temp_dict['mobileCode'] = '666666'
        response = self.request.from_post(url, data=temp_dict, headers=self.headers)[0]
        if response['resultCode'] == '00000000':
            return True
        else:
            return False


if __name__ == '__main__':
    m = main()
    print (m.login('18511752327','123456a'))
    #print (m.auth())
    a = m.auth()
