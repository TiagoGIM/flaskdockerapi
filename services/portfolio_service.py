from repositories.user_repository import Repository
from models.user import Portfolio


class PortfolioService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def create_portfolio(self, portfolio) -> Portfolio:
        return self.repository.create(portfolio)

    def get_portfolio(self, id: int):
        investments = self.repository.find_all_investments_related(id)
        portfolio = self.repository.find_by_id(id)
        response = {}

        if portfolio is not None:
            response = {**portfolio.json(), "investments": []}
            if investments:
                response["investments"] = [investment.json()
                                           for investment in investments]
        return response

    def update_portfolio(self, id: int,):
        port = self.repository.find_by_id(id)
        if port is not None:
            self.repository.update(port)
            return True
        return False

    def delete_portfolio(self, id: int):
        return self.repository.delete(id)
