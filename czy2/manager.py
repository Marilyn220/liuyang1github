# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/6 11:41
# @Author  : Chengzy
# @File    : manager.py
# @Software: PyCharm
import os ,json
from flask import Flask, render_template,request
from User import createUser as CU_app
from register import registerUser as RU_app
from smsg import smsg as smsg_app
from pay import pay as pay_app
from xdcore import xdcore as xdcore_app
from payment import payment as payment_app
from loan import loan as loan_app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.register_blueprint(CU_app)#用户信息相关
app.register_blueprint(RU_app)#用户注册相关
app.register_blueprint(smsg_app)#第三方短信验证码相关
app.register_blueprint(pay_app)#二要素验证相关
app.register_blueprint(xdcore_app)#核心相关接口
app.register_blueprint(payment_app)#绑银行卡相关
app.register_blueprint(loan_app)#本地loan服务



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# @app.route('/index',methods=["GET","POST"])
# def index():
#     file_path = os.path.split(os.path.realpath(__file__))[0]
#     print(file_path)
#     if request.method == "POST":
#         file_path = os.path.split(os.path.realpath(__file__))[0]
#         print (file_path)
#         p = os.path.join(file_path,'serviceis.json')
#         serviceid = request.form['id']
#
#         if serviceid == '83':
#             pass
#         if serviceid == '92':
#             pass
#         with open(p,'w+') as f:
#             json.dump()
#         return render_template('index.html',error='环境未配置')
#
#
#     else:
#         return render_template('index.html')

if __name__ == '__main__':
    #print (app.url_map)
    app.run(host='0.0.0.0',port='5004',debug=True)