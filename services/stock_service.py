from typing import List
from models.user import Stock


class StockService:

    def __init__(self, repository):
        self.repository = repository

    def create_stock(self, stock):
        return self.repository.create(stock)
