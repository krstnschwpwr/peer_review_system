from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired


class UserForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
