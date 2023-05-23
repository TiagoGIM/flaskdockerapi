from typing import List, Tuple
from models.user import Stock, User
from repositories.user_repository import Repository
from extensions import db


class RepositoryStockImpSQLAlchemy(Repository):

    @staticmethod
    def create(stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        db.session.flush()
        return stock

    @staticmethod
    def find_by_id(id) -> User:
        return Stock.query.filter_by(id=id).first()

    @staticmethod
    def find_all() -> List[User]:
        return Stock.query.all()

    @staticmethod
    def update(stock):
        db.session.add(stock)
        db.session.commit()
        db.session.flush()
        return stock

    @staticmethod
    def delete(stock):
        db.session.delete(stock)
        db.session.commit()
