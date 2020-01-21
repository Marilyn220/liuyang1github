# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/8 14:56
# @Author  : Chengzy
# @File    : sql_update.py
# @Software: PyCharm

import time,random
from tools.connect_db import con

class find_mysql:
    def __init__(self,ipnumber,test,serviceid):
        self.ipnumber = ipnumber
        self.test = test
        self.serviceid = serviceid
        self.time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()).replace('-', '')
        sql = """SELECT uif_userno,uif_personno from usr_userinf where  uif_mobile = '{}' """.format(self.ipnumber)
        self.userno, self.personno = con.select_db(sql,self.serviceid)[0]

    def find_auth(self):
        sql2 = '''SELECT ARE_AUTHTYPE from TRD_AUTHRECORD where are_personno = '{}' '''.format(self.personno)
        temp_list = []
        for x in con.select_db(sql2,self.serviceid):
            temp_list.append(x[0])
        return temp_list


    def face_idcard(self):
        l = self.find_auth()
        if self.test in l:
            sql3 = '''UPDATE trd_authrecord SET ARE_AUTHTIME='{}',ARE_STATUS ='20' WHERE (are_personno='{}' and ARE_AUTHTYPE={})'''.format(self.time,self.personno,self.test)
            result = con.updata_db(sql3,self.serviceid)
            return result
        else:
            sql4 = '''INSERT INTO `loan-sit3`.`trd_authrecord` (`ARE_PERSONNO`, `ARE_AUTHTYPE`, `ARE_AUTHTIME`, 
                        `ARE_USERNO`, `ARE_AUTHUSERCODE`, `ARE_DELETEREASON`, 
                        `ARE_DELETETIME`, `ARE_STATUS`, `ARE_AUTHRESULT`, `ARE_SOURCEORGANIZATIONNO`, 
                        `ARE_SUBORGANIZATIONNO`, `ARE_SOURCEPRODUCT`, `ARE_CHANNEL`) 
                        VALUES ('{}', '{}', '{}', '{}', 
                        '{}', NULL, NULL, '20', NULL, 'O20180507113389', NULL, '03', '01')
                        '''.format(self.personno,self.test, self.time, self.userno,self.userno)
            result = con.inster_db(sql4,self.serviceid)
            return result


    def image(self):
        sql7 = '''SELECT upi_imagetype from usr_personimage where upi_personno = '{}'
                '''.format(self.personno)
        P_temp_list = []
        for y in con.select_db(sql7,self.serviceid):
            print (y[0])
            P_temp_list.append(y[0])
        if self.test not in P_temp_list:
            GP = self.userno[:-4] + str(random.randint(1, 9999))
            sql8= '''INSERT INTO
                       `loan-sit3`.`usr_personimage` (`UPI_IMAGENO`, `UPI_IMAGETYPE`, `UPI_PERSONNO`,
                       `UPI_IMAGEURL`, `UPI_USERNO`, `UPI_CREATETIME`)
                       VALUES ('{}','{}','{}' ,
                       '6,19025cb22555', '{}', '{}');
                       '''.format(GP,self.test ,self.personno, self.userno,self.time)
            result = con.updata_db(sql8,self.serviceid)
        return result


    def therinf(self):
        sql1 = '''
                UPDATE `loan-sit3`.usr_personotherinf SET uof_personno = '{}',
                UOF_NATION='汉',UOF_BIRTHDAY='19920919',UOF_CERTADDRESS='北京市朝阳区酒仙桥路52号院东方科技园1号楼A座5层',
                UOF_CERTPROVINCECODE='100016',UOF_CERTCITYCODE='100016',
                `UOF_CERTDISTRICTCODE`='100016', `UOF_CERTISSUINGUNIT`='洒仙桥公安局',
                `UOF_CERTSTARTDATE`='20140709', `UOF_CERTENDDATE`='99990909',
                `UOF_MARRIAGE`=NULL, `UOF_HAVECHILDREN`=NULL, `UOF_COMPANYNAME`='钱包', `UOF_COMPANYPROVINCECODE`=NULL,
                `UOF_COMPANYCITYCODE`=NULL, `UOF_COMPANYDISTRICTCODE`=NULL, `UOF_COMPANYADDRESS`=NULL,
                `UOF_POSITIONTYPE`=NULL, `UOF_SALARYYEAR`=NULL, `UOF_HOMEPROVINCECODE`='110000', `UOF_HOMECITYCODE`='110100',
                `UOF_HOMEDISTRICTCODE`='110101', `UOF_HOMEADDRESS`='北京市北京市朝阳区 东方科技园', `UOF_HAVEHOUSE`=NULL,
                `UOF_EMAIL`=NULL, `UOF_QQNO`=NULL, `UOF_WEIXINNO`=NULL
                WHERE (UOF_PERSONNO='{}')
                '''.format(self.personno,self.personno)
        result = con.updata_db(sql1,self.serviceid)
        return result










# if __name__=='__main__':
#     face_idcard('18511752327','36')