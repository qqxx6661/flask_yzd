# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class LoginForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    remember_me = BooleanField('remember me', default=False)
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('登录'.decode('utf-8'))


class SignUpForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    user_email = StringField('user email', validators=[Email(), DataRequired(), Length(max=128)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('注册'.decode('utf-8'))


class AboutMeForm(Form):
    describe = TextAreaField('about me', validators=[DataRequired(), Length(max=140)])
    submit = SubmitField('YES!')


class AddMonitorItemForm(Form):
    item_id = IntegerField('item_id', validators=[NumberRange(min=1, max=99999999999, message='请输入正确的数字')])
    user_price = IntegerField('user_price', validators=[NumberRange(min=1, max=9999999, message='请输入正确的数字')])
    mall_id = RadioField('mall_id', choices=[('1', '京东')], validators=[DataRequired()])
    submit = SubmitField('添加监控商品'.decode('utf-8'))