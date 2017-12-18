
from app import db

from app.models import User


user = User(name="admin", email="admin@admin.com", password="admin")
db.session.add(user)
db.session.commit()