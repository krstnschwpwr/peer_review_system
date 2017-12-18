from app import db, User


db.create_all()

user = User(name="admin", email="admin@admin.com", password="admin")
db.session.add(user)
db.session.commit()