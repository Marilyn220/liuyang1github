from selenium import webdriver
import sys
sys.path.append('C:/Users/liuyang1/liuyang1github')
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement
class RegisterFunction():
    def __init__(self,url,i):
        self.driver=self.get_driver(url,i)
    #get driver and open url
    def get_driver(self,url,i):
        if i==1:
            driver=webdriver.Chrome()
        elif i==2:
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Edge()

        driver.get(url)
        driver.maximize_window()
        return driver

    #input user's infomation
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    #locate user's information,get element
    def get_user_element(self,key):
        find_element=FindElement(self.driver)
        user_element=find_element.get_element(key)
        return user_element

     # get random
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefg', 20))
        return user_info

    # get picture
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
            # return file_name2

    # get code
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "81842", "34a47f67a8b2436783df77a3b4fe6481")
        # r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "30")
        r.addBodyPara("convert_to_jpg", "1")
         # r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text

    def main(self):
        # user_name=get_range_user()
        file_name = "D:/code/test.png"
        code_text=self.code_online(file_name)
        self.send_user_info('user_name',"U2201501011000000002")
        self.send_user_info('password', "12345678")
        self.send_user_info('code_text', code_text)
        self.get_user_element('register_button').click()
        time.sleep(10)
        self.driver.close()

if __name__ == '__main__':
    for i in range(3):
        register_fuction=RegisterFunction('http://test.qianbaocard.com:23480/manager/index.html',1)
        register_fuction.main()