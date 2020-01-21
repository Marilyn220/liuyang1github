# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/22 16:48
# @Author  : Chengzy
# @File    : forms.py
# @Software: PyCharm
#from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length
from wtforms import validators
from wtforms import widgets

class LoginFrom(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()], render_kw={'placeholder': '默认信息'})
    #password = PasswordField('密码', validators=[DataRequired(), Length(8, 128)])
    password = PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="密码不能为空"),
            validators.Length(min=8, max=16, message="密码长度必须大于%(min)d且小于%(max)d"),
            validators.Regexp(regex="\d+", message="密码必须是数字"),
        ],
        widget=widgets.PasswordInput(),
        render_kw={"class": "form-control"}
    )
    submit = SubmitField('提交')