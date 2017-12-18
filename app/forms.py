from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import User

review_status = [('0', 'Under Review'), ('1', 'Accepted'),('2', 'Rejected')]

class RegisterForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class PaperForm(Form):
    title = StringField('title', validators=[InputRequired()])
    abstract = TextAreaField('abstract', validators=[InputRequired()])
    status = SelectField('Status', choices=review_status)


class UserForm(Form):
    all_users = SelectField('User', choices=[])
