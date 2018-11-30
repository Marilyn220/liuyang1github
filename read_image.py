#-*- coding:utf-8 -*-
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
#mage=Image.open("D:/newtest.png")
#ext=pytesseract.image_to_string(image)
#rint(text)

r = ShowapiRequest("http://route.showapi.com/184-4","81842","34a47f67a8b2436783df77a3b4fe6481" )
#r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "30")
r.addBodyPara("convert_to_jpg", "1")
#r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"D:/newtest.png") #文件上传时设置
res = r.post()
text=res.json()['showapi_res_body']['Result']
print(text) # 返回信息
