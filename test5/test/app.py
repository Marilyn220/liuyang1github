# -*- coding: utf-8 -*-
# python 3.7
# @Time    : 2019/9/20 11:41
# @Author  : Chengzy
# @File    : app.py.py
# @Software: PyCharm


import os ,json
from flask import Flask, render_template,request

#from .smsg import smsg as smsg_app
#from .pay import pay as pay_app
from test5.test.pay import pay as pay_app
#from payment import payment as payment_app
from test5.test.payment import payment as payment_app

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

#app.register_blueprint(smsg_app)#第三方短信验证码相关
app.register_blueprint(pay_app)#二要素验证相关

app.register_blueprint(payment_app)#绑银行卡相关




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    #print (app.url_map)
    app.run(host='0.0.0.0',port='5004',debug=True)