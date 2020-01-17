# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/5/31 16:36
# @Author  : Chengzy
# @File    : tt.py
# @Software: PyCharm


import time
import  requests
import hashlib
from urllib import parse
r = requests.session()

print (round(time.time()*1000))
timep = int(round(time.time()*1000))


def getsign(url):
    appSecret = '93397ABA-6DC1-4000-922F-57515FEDD19F'
    urldata = parse.unquote(url)

    result = parse.urlparse(urldata)

    query_dict = parse.parse_qs(result.query)

    #print(query_dict,type(query_dict))

    sign = '%sapiCode%sappKey%sbizCode%stimestamp%s%s'%(appSecret,query_dict['apiCode'][0],query_dict['appKey'][0],query_dict['bizCode'][0],query_dict['timestamp'][0],appSecret)

    m = hashlib.md5()
    m.update(sign.encode('utf-8'))

    return m.hexdigest()



def posturl(sign,url,data):
    print('请求参数', data)
    print ('请求url',url+sign)
    r = requests.post(url+sign,json=data,verify=False)
    return r.text

#url1 = 'https://sit1-apis.qianbao.com/xdcore/v1/loan/queryProductInfo?appKey=000008&apiCode=LB0001&bizCode=LBN001&timestamp=%s&'%(timep)
#data1 = {"productCode":"210517,210522,210515","secondChannelCode":"O20160901100001","channelCode":"CH0001"}
url2 = 'https://sit1-apis.qianbao.com/xdcore/v1/loan/submitApplyInfo?appKey=000008&apiCode=LB0005&bizCode=LBN005&timestamp=%s&'%(timep)

data2 ={"application":{"secondChannelName":"招财贷","channelCode":"CH0001","productCode":"210515","loanPurpose":"10","attachNumber":7,"period":12,"additionalInfo":"","applyDate":"20190603162307593","channelDutyCell":"13165793298","channelDutyPerson":"安江华","applyAmount":30000.00,"periodUnit":"M","secondChannelCode":"O20160901100001"},"contactList":[{"certificateCode":"110101198611021016","contactRelation":"5","contactName":"郭泽民","certificateType":"1","mobileNo":"13464646464"},{"contactRelation":"8","contactName":"555","certificateType":"1","mobileNo":"18600032182"}],"repayAccount":{"repayAccountBankName":"CMB","repayCardType":"DC","repayCheckDate":"20190413","repayAccountNo":"6225880151110997","repayAccountType":"2","repayIsCheck":"2","repayAccountName":"程正阳","repayAccountMobileNo":"15811142327"},"lendAccount":{"lendAccountBankName":"CMB","lendAccountType":"2","lendAccountName":"程正阳","lendIsCheck":"2","lendAccountMobileNo":"15811142327","lendAccountNo":"6225880151110997","lendCardType":"DC"},"transactionNumber":"LON2019060310000000087816","customer":{"idCardAddress":"河北省张家口市怀来县西八里镇闫家房村2号","sex":"1","idCardLimitStartDate":"20160415","marrageState":"1","birthdate":"19891029","idcardRegionCode":"130730","customerName":"程正阳","certificateCode":"130730198910290812","regionCode":"150304","customerType":"1","idCardOffice":"怀来县公安局","certificateType":"1","nation":"1","address":"四川省乐山市雁塔区 558","idCardLimit":"20360415","mobileNo":"15811142327"},"businessList":[{"restaurantType":"JY126","endDate":"","beginDate":"","corporateRepresentative":"程正阳","staffNumber":"00","corporationPhone":"15811142327","establishDate":"","hygieneLevel":"00","businessLicenseRegionCode":"","shMerchantName":"藕相逢（光华路店）","managerType":"01","companyName":"西安市雁塔区达人牛肉面馆","societyCode":"610113600203090","corporationCertificateCode":"130730198910290812","businessEntityRegionCode":"511100","businessEntityAddress":"兴善寺东街育才中学西侧","onlineMerchantNumber":"M20170329270730","businessLicenseAddress":"","posMerchantNumber":"890000000002639"}]}

url3 = 'https://sit4-apis.qianbao.com/xdcore/v1/loan/paymentplan/search?appKey=000008&apiCode=LA0003&bizCode=LAN003&timestamp=%s&'%(timep)

data3 = {"channelCode":"CH0001","iouCode":"20190523000013-01"}

url4 = 'https://sit4-apis.qianbao.com/xdcore/v1/loan/submitApplyInfo?appKey=000008&apiCode=LB0005&bizCode=LBN005&timestamp=%s&'%(timep)

data4 = {"application":{"secondChannelName":"招财贷","channelCode":"CH0001","productCode":"212204","loanPurpose":"10","attachNumber":11,"period":6,"additionalInfo":"","applyDate":"20190709150102634","channelDutyCell":"18739188630","channelDutyPerson":"程胜","applyAmount":20000.00,"periodUnit":"M","secondChannelCode":"O20160901100001"},"contactList":[{"contactRelation":"2","contactName":"测试","certificateType":"1","mobileNo":"13066613666"},{"contactRelation":"3","contactName":"查韦斯","certificateType":"1","mobileNo":"13782718789"},{"certificateCode":"41142119880924522X","contactRelation":"5","contactName":"李娟","certificateType":"1","mobileNo":"15396526885"},{"contactRelation":"7","contactName":"更好","certificateType":"1","mobileNo":"13681157434"},{"contactRelation":"8","contactName":"李静","certificateType":"1","mobileNo":"15211425365"},{"contactRelation":"9","contactName":"搞活经济","certificateType":"1","mobileNo":"13681157433"}],"repayAccount":{"repayAccountBankName":"ICBC","repayCardType":"DC","repayCheckDate":"20190612","repayAccountNo":"6222000200121658611","repayAccountType":"2","repayIsCheck":"2","repayAccountName":"张伟","repayAccountMobileNo":"13511063604"},"lendAccount":{"lendAccountBankName":"ICBC","lendAccountType":"2","lendAccountName":"张伟","lendIsCheck":"2","lendAccountMobileNo":"13511063604","lendAccountNo":"6222000200121658611","lendCardType":"DC"},"transactionNumber":"LON2019070510000000189761","customer":{"idCardAddress":"河南省温县鲁田镇西城外村三摊","sex":"0","idCardLimitStartDate":"20140612","marrageState":"1","birthdate":"19830915","idcardRegionCode":"410825","customerName":"张伟","certificateCode":"410825198309152525","regionCode":"410802","customerType":"1","idCardOffice":"松原市公安局宁江分局","certificateType":"1","nation":"1","address":"河南省焦作市解放区 李静来咯哦","idCardLimit":"99990909","mobileNo":"13511063604"},"businessList":[{"restaurantType":"JY126","endDate":"","beginDate":"20041102","corporateRepresentative":"张伟","staffNumber":"04","corporationPhone":"18639171555","establishDate":"","hygieneLevel":"02","businessLicenseRegionCode":"","shMerchantName":"森林大酒店","companyName":"焦作市森林大酒店（普通合伙）","societyCode":"410802000006970","corporationCertificateCode":"410825198309152525","businessEntityRegionCode":"410802","businessEntityAddress":"解放路田涧村口斜对面","onlineMerchantNumber":"M20160819108440","businessLicenseAddress":"","posMerchantNumber":"890000000001760"}]}



url5 = 'https://sit3-apis.qianbao.com/xdcore/v1/loan/queryContractInfo?appKey=000001&apiCode=LB0028&bizCode=LBN028&timestamp=%s&'%(timep)

data5 = {}

url6 = 'https://sit5-apis.qianbao.com/xdcore/v1/loan/queryLoanStatus?appKey=000001&apiCode=LB0033&bizCode=LBN033&timestamp=%s&'%(timep)

data6 = [{"iouCode":"20190528000005-01","loanStatus":"05","loanDate":"2022-12-03","rbMaxRepayPenalty":"100.03","rbMaxRepayAmount":"8123.678"}]


url7 = 'https://sit5-apis.qianbao.com/xdcore/v1/loanapi/ba/pay/doCollectionDj?appKey=000003&apiCode=BA0095&bizCode=LON065&timestamp=%s&'%(timep)

data7 = [{"iouCode":"20190528000005-01","loanStatus":"05","loanDate":"2022-12-03","rbMaxRepayPenalty":"100.03","rbMaxRepayAmount":"8123.678"}]


url8 = 'https://sit5-apis.qianbao.com/xdcore/v1/loan/biz/queryCoaChargeTmpl?appKey=000001&apiCode=LB0048&bizCode=TDN048&timestamp=%s&'%(timep)

data8 = {}

url9 = 'https://sit6-apis.qianbao.com/xdcore/v1/loan/queryContractInfo?appKey=000001&apiCode=LB0028&bizCode=LBN028&timestamp=%s&'%(timep)

data9 = {"iouCode":"20190926000007-01"}

url10='http://sit6-apis.qianbao.com/xdcore/v1/loan/queryAuditResult?appKey=000007&apiCode=LB0030&bizCode=LBN030&timestamp=%s&'%(timep)
data10=[
        {
            "iouCode":"20191230000002-01",
            "loanStatus":"02",
            "opinion":"【6003:businessEntityAddress经营地址不能为空参数不能为空】"
        }
    ]

if __name__=='__main__':
    print (getsign(url10))
    print (posturl('sign=%s'%getsign(url10),url10,data10))



