#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest
from PIL import Image
import time
import random

driver = webdriver.Chrome()
driver.get('http://test.qianbaocard.com:23480/manager/index.html')
time.sleep(5)
EC.title_contains("运营中心") #Use the title to determine if the page is open
print(EC.title_contains("运营中心"))   
name_element=driver.find_element_by_id("name")
driver.save_screenshot("D:/test.png")
code_element=driver.find_element_by_id("validationCodeImg")
print(code_element.location)#("x":123,"y":345)
left=code_element.location['x']
top=code_element.location['y']
right=code_element.size['width']+left
height=code_element.size['height']+top
im=Image.open("D:/test.png")
img=im.crop((left,top,right,height))
img.save("D:/newtest.png")


r = ShowapiRequest("http://route.showapi.com/184-4","81842","34a47f67a8b2436783df77a3b4fe6481" )
#r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "1")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"D:/newtest.png") #文件上传时设置
res = r.post()
text=res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
#driver.find_element_by_id("code").send_keys(text)

#for i in range(5):
#    user_name=''.join(random.sample('123456789abcdefg',20))
#    print(user_name)

#element=driver.find_element_by_class_name("login-label")
#EC.visibility_of_element_located(element)#judge if the element is visible
locator=(By.CLASS_NAME,"login-label")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))

print(name_element.get_attribute("placeholder"))
name_element.send_keys("U2201501011000000002")
print(name_element.get_attribute("value"))

time.sleep(5)
driver.close()
#driver.find_element_by_xpath("//*[@id='name']").send_keys("U2201501011000000002")
#driver.find_element_by_id("password").send_keys("12345678")
#driver.find_element_by_id("code").send_keys("1111")
