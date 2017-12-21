from flask import Flask, g
from flask.ext.bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os
from db_create import create_db
#from flask_restful import Api, Resource
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bcrypt = Bcrypt(app)
#api = Api(app)



app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
db = SQLAlchemy(app)



ma = Marshmallow(app)
#auth = HTTPBasicAuth()

lm = LoginManager()
lm.init_app(app)


@lm.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

lm.login_view="home"

db.create_all()

app.config.from_object(__name__)

from app import views
from app.models import User

create_db()






