from app.models import User, Paper
from app import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User



user_schema = UserSchema()
users_schema = UserSchema(many=True)