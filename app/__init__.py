from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_openid import OpenID

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
db = SQLAlchemy(app)



lm = LoginManager()
lm.init_app(app)
#oid = OpenID(app, os.path.join(basedir, 'tmp'))

app.config.from_object(__name__)
from app import views
from app.models import User

lm.login_view = "users.login"


@lm.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
