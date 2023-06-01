from ast import List
from sqlalchemy import or_
from repositories.user_repository import Repository
from models.user import User
from extensions import db


class RepositoryUserImpSQLAlchemy(Repository):
    @staticmethod
    def create(user) -> User:
        db.session.add(user)
        db.session.commit()
        db.session.flush()
        return user

    @staticmethod
    def find_all():
        return User.query.all()

    @staticmethod
    def find_by_id(user_id: int) -> User:
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def update(user: User) -> bool:
        if user:
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete(user_id: int):
        user = User.query.find_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            db.session.flush()
            return True

        return False

    @staticmethod
    def find_user_by_prop_list(user: User, props: List):
        query = User.query.filter(
            or_(*[getattr(User, prop) == getattr(user, prop) for prop in props]))

        return query.first()
