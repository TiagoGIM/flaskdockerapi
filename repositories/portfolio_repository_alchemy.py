from ast import List
from typing import Tuple
from models.investiments import Investment
from models.user import Portfolio, User
from repositories.user_repository import Repository
from extensions import db


class RepositoryPortfolioImpSQLAlchemy(Repository):
    @staticmethod
    def create(portfolio: Portfolio) -> Portfolio:
        found_user = User.query.filter_by(id=portfolio.user_id).first()
        if found_user:
            db.session.add(portfolio)
            db.session.commit()
            db.session.flush()
            return portfolio
        return None

    @staticmethod
    def find_by_id(id) -> Portfolio:
        return Portfolio.query.filter_by(id=id).first()

    @staticmethod
    def find_all() -> List:
        return Portfolio.query.all()

    @staticmethod
    def update(portfolio: Portfolio):
        found_user = User.query.filter_by(id=portfolio.user_id).first()
        found_port = Portfolio.query.filter_by(id=portfolio.id).first()  # type: Portfolio  # noqa:
        if found_user and found_port:
            db.session.add(portfolio)
            db.session.commit()
            db.session.flush()
            return portfolio
        return None

    @staticmethod
    def delete(id):
        portfolio = Portfolio.query.filter_by(id=id).first()
        if portfolio:
            db.session.delete(portfolio)
            db.session.commit()
            db.session.flush()
            return True

        return False

    @staticmethod
    def find_all_investments_related(portfolio_id: int):
        return Investment.query.filter_by(portfolio_id=portfolio_id).all()  # type: List[Tuple[Portfolio, List[str]]]  # noqa: F841  #
