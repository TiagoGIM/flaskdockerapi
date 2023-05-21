from sqlalchemy import or_
from repositories.user_repository import Repository
from models.user import User
from extensions import db


class RepositoryUserImpSQLAlchemy(Repository):
    @staticmethod
    def create(user) -> User:
        created = db.session.add(user)
        print("what is returned")
        print(created)
        db.session.commit()
        return created

    @staticmethod
    def find_all():
        return User.query.all()

    @staticmethod
    def find_by_id(user_id: int) -> User:
        return User.query.filter_by(id=user_id).first()

    def update(self, user_id: int, username: str, email: str):
        user = self.find_by_id(user_id)

        if user:
            user.username = username
            user.email = email
            db.session.commit()

    def delete(self, user_id: int):
        user = self.find_by_id(user_id)

        if user:
            db.session.delete(user)
            db.session.commit()

    def find_by_username(self, username: str) -> User:
        return User.query.filter_by(username=username).first()

    def find_user_by_name_or_email(self, username, email):
        user = User.query.filter(
            or_(User.username == username, User.email == email)).first()

        return user is not None