from app.models import User, Paper, Reviewer
from app import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class PaperSchema(ma.ModelSchema):
    class Meta:
        model = Paper

class ReviewerSchema(ma.ModelSchema):
    class Meta:
        model = Reviewer


user_schema = UserSchema()
users_schema = UserSchema(many=True)

paper_schema = PaperSchema()
papers_schema = PaperSchema(many=True)

reviewer_schema = ReviewerSchema()
reviewers_schema = ReviewerSchema(many=True)