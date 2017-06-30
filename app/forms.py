# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('登录'.decode('utf-8'))


class SignUpForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    user_email = StringField('user email', validators=[Email(), DataRequired(), Length(max=128)])
    submit = SubmitField('注册'.decode('utf-8'))


class AboutMeForm(Form):
    describe = TextAreaField('about me', validators=[DataRequired(), Length(max=140)])
    submit = SubmitField('YES!')


class AddMonitorItemForm(Form):
    item_id = TextAreaField('item_id', validators=[DataRequired()])
    user_price = TextAreaField('item_id', validators=[DataRequired()])
    mall_id = TextAreaField('item_id', validators=[DataRequired()])
    submit = SubmitField('添加监控商品'.decode('utf-8'))