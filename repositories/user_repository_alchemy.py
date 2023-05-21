from repositories.user_repository import Repository
from models.user import User
from extensions import db


class RepositoryUserImpSQLAlchemy(Repository):
    @staticmethod
    def create(username: str, email: str) -> User:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

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
