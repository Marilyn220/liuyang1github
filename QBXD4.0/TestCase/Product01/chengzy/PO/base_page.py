# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/22 18:07
# @Author  : Chengzy
# @File    : base_page.py
# @Software: PyCharm

from Public.DrObj import DrObj
class base_page(DrObj):
    def __init__(self):
        self.time_out = 10
        print ('base_page.py中初始化后的dr信息如下：')
        print (self.d)

    def find_ele(self,ele):
        if ele.startswith('com.'):#id
            if self.d(resourceId = ele).exists(timeout=self.time_out):
                return 'resourceId'
            else:
                return False
        elif ele.startswith('//'):#xpath
            if self.d(xpath = ele).exists(timeout=self.time_out):
                return 'xpath'
            else:
                return False
        else:
            if self.d(text = ele).exists(timeout=self.time_out):
                return 'text'
            else:
                return False


    def click(self,ele):
        find_type = self.find_ele(ele)
        if find_type and find_type== 'resourceId':
            self.d(resourceId = ele).click()
        elif find_type and find_type == 'xpath':
            self.d(xpath = ele).click()
        elif find_type and find_type == 'text':
            self.d(text = ele).click()
        else:
            return False

    def send_key(self,ele,msg):
        find_type = self.find_ele(ele)
        self.d.set_fastinput_ime(True)
        if find_type and find_type == 'resourceId':
            self.d(resourceId=ele).clear_text(timeout=self.time_out)
            self.d(resourceId=ele).send_keys(str(msg))
            self.d.set_fastinput_ime(False)
        elif find_type and find_type == 'xpath':
            self.d(xpath=ele).clear_text(timeout=self.time_out)
            self.d(xpath=ele).send_keys(str(msg))
            self.d.set_fastinput_ime(False)
        elif find_type and find_type == 'text':
            self.d(text=ele).clear_text(timeout=self.time_out)
            self.d(text=ele).send_keys(str(msg))
            self.d.set_fastinput_ime(False)
        else:
            self.d.set_fastinput_ime(False)
            return False
