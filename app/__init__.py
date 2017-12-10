from flask import Flask, g
from flask.ext.bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
db = SQLAlchemy(app)
ma = Marshmallow(app)


lm = LoginManager()
lm.init_app(app)

app.config.from_object(__name__)
from app import views
from app.models import User

#lm.login_view = "users.login"



