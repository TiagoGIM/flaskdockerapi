from typing import Tuple
from models.user import Stock
from repositories.user_repository import Repository
from extensions import db


class RepositoryStockImpSQLAlchemy(Repository):
    @staticmethod
    def create(stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock
