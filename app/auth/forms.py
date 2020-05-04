from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,BooleanField,SubmitField,ValidationError
from wtforms.validators import InputRequired,Length,EqualTo,Required,Email


class RegistrationForm(FlaskForm):
    username = StringField('username_label')
    password = PasswordField('password_label')
    confirm_password = PasswordField('confirm_pswd_label')
    submit = SubmitField('sign up')






class LoginForm(FlaskForm):
    useremail = StringField('Your Email Address_label')
    password = PasswordField('Password_label')
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')    