from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField
from wtforms.validators import InputRequired,Length,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username_label')
    password = PasswordField('password_label')
    confirm_password = PasswordField('confirm_pswd_label')