# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/26 17:38
# @Author  : Chengzy
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,PasswordField
from wtforms.validators import DataRequired,Length


class  loan_forms_one(FlaskForm):
    iphone_number = StringField('手机号', validators=[DataRequired()])
    password = PasswordField(
        label="密码",
        validators=[DataRequired(message="密码不能为空"),],render_kw={"class": "form-control"})
    timelimit = SelectField(label='期限3、6、9、12',validators=[DataRequired('请选择标签')],render_kw={'class': 'form-control'},choices=[(3,'3期'),(6,'6期'),(9,'9期'),(12,'12期')],default=3,
                            coerce=int)
    money = StringField(label='金额',validators=[DataRequired()])
    submit = SubmitField()
