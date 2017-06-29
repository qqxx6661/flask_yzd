from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log in')


class SignUpForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    user_email = StringField('user email', validators=[Email(), DataRequired(), Length(max=128)])
    submit = SubmitField('Sign up')