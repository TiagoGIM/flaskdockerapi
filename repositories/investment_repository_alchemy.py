from models.investiments import Investment
from repositories.user_repository import Repository
from extensions import db
from models.user import User

class RepositoryInvestmentImpSQLAlchemy(Repository):
  

    @staticmethod
    def create(investment: Investment) -> Investment:
        db.session.add(investment)
        db.session.commit()
        db.session.flush()
        return investment


    @staticmethod
    def find_by_id(id: int) -> Investment:
      return Investment.query.filter_by(id=id).first()
  
  
    @staticmethod
    def find_user_by_id(user_id: int) -> bool:
        return User.query.filter_by(id=user_id).first()