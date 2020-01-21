# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/6 14:14
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm

from . import createUser
from flask import request,render_template
from tools.base import phone_isexist

from .user_tools.funcAll import main
from User.sql_update import find_mysql

@createUser.route('/',methods=["GET","POST"])
def auth():#实名认证
    if request.method == "POST":
        number = request.form['ip']
        pwd = request.form['pwd']
        serviceid = request.form['id']
        if number=='' or pwd=='' or serviceid=='':
            return render_template('user/index.html',error='手机号或密码或环境不可为空')
        p = phone_isexist(number,serviceid)#检查手机号是否存在
        if p[0]==False:#手机号存在
            m = main(serviceid)
            if m.login(number,pwd):
                auth = m.auth()
                if auth[0] :
                    return render_template('user/index.html',succeed=auth[1])
                else:
                    return render_template('user/index.html',error='认证失败信息如下：%s'%auth[1])
            else:
                return render_template('user/index.html',error='登录失败，请确认手机号与验证码')
        else:
            return render_template('user/index.html',error='手机号不存在')

    else:
        return render_template('user/index.html')


@createUser.route('/fill',methods=["GET","POST"])
def fill():#联系人认证
    if request.method == "POST":
        number = request.form['ip']
        pwd = request.form['pwd']
        serviceid = request.form['id']
        if number == '' or pwd == '' or serviceid=='':
            return render_template('user/fill.html', error='手机号或密码不可为空')
        p = phone_isexist(number,serviceid)  # 检查手机号是否存在
        if p[0] == False:  # 手机号存在
            m = main(serviceid)
            if m.login(number, pwd):
                fill = m.fill()
                if fill:
                    return render_template('user/fill.html', succeed='联系人认证成功')
                else:
                    return render_template('user/fill.html', error='联系人认证失败')
            else:
                return render_template('user/fill.html', error='登录失败，请确认手机号与验证码')
        else:
            return render_template('user/fill.html', error='手机号不存在')
    else:
        return render_template('user/fill.html')




@createUser.route('/face_idcard',methods=["GET","POST"])
def face_idcard():
    if request.method == "POST":
        temp_dict = {'0':None,'30':'人脸认证','36':'身份证识别(H5)','P11':'身份证正面','P12':'身份证反面','1':'个人基本信息补充'}
        ip = request.form['ip']
        test = request.form['test']
        serviceid = request.form['id']
        print (ip,test)
        if ip==''or request.form['test']=='0'or phone_isexist(ip,serviceid)[0]==True:
            return render_template('user/face_idcard.html',error = '手机号必填或选项未选择或手机号在库中未查到')

        f = find_mysql(ip,test,serviceid)
        if test == '30' or test=='36':
            f.face_idcard()
            return render_template('user/face_idcard.html',succeed ='认证项%s成功'%temp_dict[test])
        if test == 'P11' or test == 'P12':
            f.image()
            return render_template('user/face_idcard.html', succeed='认证项%s成功' % temp_dict[test])
        if test == '1':
            f.therinf()
            return render_template('user/face_idcard.html', succeed='认证项%s成功' % temp_dict[test])
    else:
        return render_template('user/face_idcard.html')



@createUser.route('/cardbin',methods=["GET","POST"])
def cardbin():
    if request.method == "POST":
        iphone_number = request.form['ip']
        pwd = request.form['pwd']
        dbin = request.form['dbin']
        serviceid = request.form['id']
        if iphone_number == '' or dbin == '' or pwd =='' or phone_isexist(iphone_number,serviceid)[0] == True:
            return render_template('user/cardbin.html',error = '手机号未必填或银行卡号未必填或手机号在库中未查到')
        m = main(serviceid)
        if m.login(iphone_number, pwd):
            if m.cardbin(iphone_number,dbin):
                #验证通过输入密码进行绑卡操作
                if m.toBind():
                    return render_template('user/cardbin.html',succeed = '绑卡成功')
                else:
                    return render_template('user/cardbin.html', error='绑卡失败')

            return render_template('user/cardbin.html',succeed = '绑卡失败')
        else:
            return render_template('user/cardbin.html',error = '登录失败，请确认手机号与验证码')

    else:
        return render_template('user/cardbin.html')



