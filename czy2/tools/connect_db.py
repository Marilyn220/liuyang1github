# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/6 19:49
# @Author  : Chengzy
# @File    : connect_db.py
# @Software: PyCharm

import pymysql


class con:
    @classmethod
    def select_db(cls,sql,serviceid):
        #host = '172.28.38.%s'%serviceid
        host = '172.28.38.83'
        try:
            cls.conn = pymysql.connect(host=host, port=3306, user='mysqladmin', passwd='123465',
                                        db='loan-sit3')
            cls.cursor = cls.conn.cursor()
            cls.cursor.execute(sql)
            cls.conn.commit()
            row = cls.cursor.fetchall()
            cls.cursor.close()
            cls.conn.close()
            return row
        except Exception as e:
            print ('提交数据报错',e)
            cls.cursor.close()
            cls.conn.close()
            return False


    @classmethod
    def inster_db(self,sql,serviceid):
        #host = '172.28.38.%s' % serviceid
        host = '172.28.38.83'
        try:
            self.conn = pymysql.connect(host=host, port=3306, user='mysqladmin', passwd='123465',
                                        db='loan-sit3')
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            return '插入数据成功'
        except Exception as e:
            print ('插入数据报错')
            self.cursor.close()
            self.conn.close()
            return False


    @classmethod
    def updata_db(self,sql,serviceid):
        #host = '172.28.38.%s' % serviceid
        host = '172.28.38.83'
        try:
            self.conn = pymysql.connect(host=host, port=3306, user='mysqladmin', passwd='123465',
                                        db='loan-sit3')
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            self.conn.commit()
            print('成功插入', self.cursor.rowcount, '条数据')
            self.cursor.close()
            self.conn.close()
            return self.cursor.rowcount
        except Exception as e:
            print ('提交数据报错',e)
            self.cursor.close()
            self.conn.close()
            return False

if __name__=="__main__":

    c = con()
    sql = "SELECT t3.*,t4.* from t3 ,t4 where t3.orderNumber=t4.orderNumber and t3.orderNumber='DS201902288940'"
    print (c.select_db(sql))