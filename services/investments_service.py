from repositories.user_repository import Repository
from models.investiments import Investment

class InvestimentService:
  def __init__(self, repository: Repository):
      self.repository = repository
    
  def add_invest(self, Investment):
      return self.repository.create(Investment)
    
  def find_by_id(self, id):
    return self.repository.find_by_id(id)
  
  def find_user_by_id(self, user_id):
    return self.repository.find_user_by_id(user_id)