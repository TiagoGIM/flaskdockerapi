from typing import List
from models.stock import Stock
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
    def find_by_id(id) -> Stock:
        return Stock.query.filter_by(id=id).first()

    @staticmethod
    def find_all() -> List[Stock]:
        return Stock.query.all()

    @staticmethod
    def update(stock):
        db.session.merge(stock)
        db.session.commit()
        db.session.flush()
        return stock

    @staticmethod
    def delete(stock):
        db.session.delete(stock)
        db.session.commit()
