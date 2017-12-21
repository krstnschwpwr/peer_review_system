from app import db, lm
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Enum

from app import bcrypt





class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)

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

    def __repr__(self):
        return 'Users {}>'.format(self.id)


class Paper(db.Model):
    __tablename__ = "papers"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    abstract = db.Column(db.String, nullable=False)
    status = db.Column(db.String(255), nullable=True, default="under review")
    author_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=True)

    def __init__(self, title, abstract, author_id):
        self.title = title
        self.abstract = abstract
        self.author_id = author_id

    def __repr__(self):
        return '<Paper:{}>'.format(self.title)


class Reviewer(db.Model):

    __tablename__ = "reviewers"
    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.Integer, nullable=False)
    reviewer_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=True)

    def __init__(self, paper_id, reviewer_id):
        self.paper_id = paper_id
        self.reviewer_id = reviewer_id
        self.rating = None

    def __repr__(self):
        return '<Reviewer:{}>'.format(self.id)
