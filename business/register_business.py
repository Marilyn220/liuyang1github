#-*- coding:utf-8 -*-
from page.register_page import RegisterPage
class RegisterBusiness():
    def __init__(self):
        self.register_h=RegisterPage(driver)
    #Perform operations
    def login(self,name,password,code):
        self.register_h.send_user_name()
        if self.register_h.get_user_text("字符长度必须大于等于4，一个"):
            print("用户名验证成功")
        elif self.register_h.get_user_text("最少需要输入5个字符"):
            print("用户名验证成功")
            return True
