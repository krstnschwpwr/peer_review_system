from app import db, lm
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer
from app import bcrypt





class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    papers = db.relationship("Paper", backref="reviewer", lazy="dynamic")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    @lm.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    def __repr__(self):
        return 'Users {}>'.format(self.id)


class Paper(db.Model):

    __tablename__ = "papers"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    abstract = db.Column(db.String, nullable=False)
    reviewer_id =db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, abstract, reviewer_id):
        self.title = title
        self.abstract = abstract
        self.reviewer_id = reviewer_id

    def __repr__(self):
        return '<Paper:{}>'.format(self.title)


db.create_all()