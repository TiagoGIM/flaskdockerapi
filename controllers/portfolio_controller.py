from flask import make_response, request
from helpers.validators import ValidModel
from models.user import Portfolio
from services.portfolio_service import PortfolioService
from repositories.portfolio_repository_alchemy import RepositoryPortfolioImpSQLAlchemy


portfolio_repository = RepositoryPortfolioImpSQLAlchemy()
portfolio_service = PortfolioService(portfolio_repository)


@ValidModel(Portfolio)
def create_portfolio():
    data = request.json
    portfolio = Portfolio(**data)

    try:
        created_portfolio = portfolio_service.create_portfolio(portfolio)
        if (created_portfolio):
            return make_response({'message': 'user created', 'user': created_portfolio.json()}, 201)
        return make_response({'message': 'could not create wallet'}, 400)
    except Exception as e:
        return make_response({'message': 'Error', 'error': str(e)}, 500)


def get_portfolio(id):  
    try:
        portfolio = portfolio_service.get_portfolio(id)
        if portfolio:
            return make_response({'message': 'portfolio found', 'portfolio':  portfolio}, 200)
        return make_response({'message': 'portfolio not found'}, 404) 
    except Exception as e:
        return make_response({'message': 'Error', 'error': str(e)}, 500)


def delete_portfolio(id):
    try:
        if portfolio_service.delete_portfolio(id):
            return make_response({'message': 'portf. deleted'}, 200)
        return make_response({'message': 'portf. not found'}, 404)
    except Exception as e:
        return make_response({'message': 'Error', 'error': str(e)}, 500)


@ValidModel(Portfolio)
def update_portfolio(id:int):
    data = request.json

    try:
        
        portfolio = Portfolio(**data)
        portfolio.id = id
        
        if (not portfolio_service.update_portfolio(portfolio)):
            
            return make_response({'message': 'user not found'}, 404)
        
        return make_response({'message': 'Portfolio updated successfully'}, 200)
    
    except Exception as e:
        print(e)
        return make_response({'message': 'Error', 'error': str(e)}, 500)
