from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, DataRequired


class RegisterForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class PaperForm(Form):
    title = StringField('title', validators=[InputRequired()])
    abstract = StringField('abstract', validators=[InputRequired()])