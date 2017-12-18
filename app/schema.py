from app.models import User, Paper
from app import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class PaperSchema(ma.ModelSchema):
    class Meta:
        model = Paper

user_schema = UserSchema()
users_schema = UserSchema(many=True)

paper_schema = PaperSchema()
papers_schema = PaperSchema(many=True)