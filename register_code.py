#-*- coding:utf-8 -*-
from selenium import webdriver
from ShowapiRequest import ShowapiRequest
from PIL import Image
import random
import time
class ff ():
    driver = webdriver.Chrome()
    file_name1 = "D:/code/test.png"
    #browser init

    def driver_init(self):
        self.driver.get('http://test.qianbaocard.com:23480/manager/index.html')
        self.driver.maximize_window()
        time.sleep(5)

    # get element information
    def get_element(self,id):
        element=self.driver.find_element_by_id(id)
        return element

    #get random
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefg',20))
        return user_info

    #get picture
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("validationCodeImg")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        #return file_name2

    # get code
    def code_online(self,file_name):
        r = ShowapiRequest("http://route.showapi.com/184-4", "81842", "34a47f67a8b2436783df77a3b4fe6481")
        # r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "30")
        r.addBodyPara("convert_to_jpg", "1")
        # r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text

    # run main programe
    def run_main(self):
        #user_name=get_range_user()
        file_name="D:/code/test.png"
        self.driver_init()
        self.get_element("name").send_keys("U2201501011000000002")
        self.get_element("password").send_keys("12345678")
        self.get_code_image(file_name)
        text=self.code_online(file_name)
        self.get_element("code").send_keys(text)
        self.get_element("login").click()
        self.driver.close()
ff().run_main()
