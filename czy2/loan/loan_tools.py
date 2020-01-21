# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/26 18:06
# @Author  : Chengzy
# @File    : loan_tools.py
# @Software: PyCharm

from tools.base import base


class submit_core(base):


    '''
    1.调base里的登录拿到token
    2.调base里的control拿到用户银行卡
    3.再执行checkcarusable方法
    '''


    def getAccountList(self):#获取银行卡
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)
        temp_dict['sceneCode'] = 'S03'
        url = self.host+'/loan/bindCard/getAccountList.do'
        response = self.request.from_post(url=url,data=temp_dict,headers=self.headers)[0]
        if response['resultCode'] == '00000000' and response['accountList']!=[]:
            return response['accountList'][0]['accountNo']
        else:
            return False




    #http://172.28.38.92/loan/bindCard/checkCardUsable.do
    def checkCardUsable(self,i,p,timelimit,money):#获取短信验证码
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)
        temp_dict['sceneCode'] = 'S03'
        if self.login(i,p):
            account = self.getAccountList()
            if account:
                temp_dict['accountNo'] = account
            else:
                return (False,'未找到银行卡信息或接口不通')
            url = self.host+'/loan/bindCard/checkCardUsable.do'
            response = self.request.from_post(url=url,data=temp_dict,headers=self.headers)[0]
            if response['resultCode']== '00000000':
                if self.toBind():
                    temp_dict.pop('sceneCode')
                    temp_dict['purpose'] = '2'
                    temp_dict['applyAmount'] = money
                    temp_dict['periodType'] = 'M'
                    temp_dict['periodValue'] = timelimit
                    temp_dict['buyInsurance'] = '1'
                    temp_dict['signScene'] = '02'
                    url = self.host+'/loan/easyLoan/loanApply/addLoanApply.do'#提交进件接口
                    response = self.request.from_post(url=url,data=temp_dict,headers=self.headers)[0]
                    return True
                else:
                    return False
            else:
                return False
        else:
            return (False,'登录失败')

    #http://172.28.38.92/loan/bindCard/toBind.do
    def toBind(self):
        temp_dict = {}
        temp_dict = dict(self.base_data, **temp_dict)
        tobin = '/loan/bindCard/toBind.do'
        url = self.host + tobin
        #temp_dict.pop('sceneCode')
        temp_dict['mobileCode'] = '666666'
        respone = self.request.from_post(url=url, data=temp_dict, headers=self.headers)[0]
        if respone['resultCode']=='00000000':
            return '绑卡成功'
        else:
            return False

    #http://172.28.38.92/loan/easyLoan/loanApply/addLoanApply.do
    # def addloanapply(self,timelimit,money):
    #     temp_dict = {}
    #     temp_dict = dict(self.base_data, **temp_dict)
    #     temp_dict['purpose'] = '2'
    #     temp_dict['applyAmount'] = money
    #     temp_dict['periodType'] = 'M'
    #     temp_dict['periodValue'] = timelimit
    #     temp_dict['buyInsurance'] = '1'
    #     temp_dict['accountNo'] = ''
    #     temp_dict['signScene'] = '02'



    #发短信写完了，该写提交的接口了
if __name__=="__main__":
    s = submit_core('83')
    s.t('18797010372','123456a')