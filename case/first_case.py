#-*- coding:utf-8 -*-
class  FirstCase(object):
     def test_login_username_error(self):
        login('1234','111')
        #use 'assert' to judge if it is error
     def test_login_password_error(self):
        login('1234', '111')
     def test_login_code_error(self):
        login('1234', '111')
     def test_login_success(self):
        login('1234', '111')
