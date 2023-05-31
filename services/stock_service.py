from typing import List, Optional
from models.stock import Stock
from repositories.user_repository import Repository


class StockService:

    def __init__(self, repository: Repository):
        self.repository = repository

    def create_stock(self, stock) -> Stock:
        return self.repository.create(stock)

    def get_all_stocks(self) -> List[Stock]:
        return self.repository.find_all()

    def get_by_id(self, id: int) -> Optional[Stock]:
        print(self.repository.find_by_id(id)
              )
        return self.repository.find_by_id(id)

    def update(self, stock) -> Optional[Stock]:
        return self.repository.update(stock)

    def delete(self, id: int):
        stock = self.repository.find_by_id(id)
        if (stock):
            self.repository.delete(stock)
            return True
        else:
            return False
