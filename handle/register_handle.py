#-*- coding:utf-8 -*-
from page.register_page import RegisterPage
class RegisterHandle():
    def __init__(self):
        self.register_p=RegisterPage(driver)
    #input username
    def send_user_name(self):
        self.register_p.get_name_element().send_keys()
    # input password
    def send_user_password(self):
        pass
    # input code
    def send_user_code(self):
        pass