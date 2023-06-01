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
  
  def get_all_investments_by_user_id(self, user_id):
    investments =  self.repository.find_all_by_user_id(user_id)
    investments_parsed = [investment.json() for investment in investments]
    return investments_parsed
  
  def update_investment(self, investment : Investment):
      updated = self.repository.update(investment)
      if updated is not None:
        return updated.json()
      return None
  
  def delete_investment(self, id :int):
      return self.repository.delete(id)