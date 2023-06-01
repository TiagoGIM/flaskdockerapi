from flask import make_response, request
from helpers.validators import ValidModel
from models.investiments import Investment
from repositories.investment_repository_alchemy import RepositoryInvestmentImpSQLAlchemy
from services.investments_service import InvestimentService

invetment_repository = RepositoryInvestmentImpSQLAlchemy
investment_service =  InvestimentService(invetment_repository)

@ValidModel(Investment)
def create_investments():
    data = request.json
    
    try:
        investment = Investment(**data)
        hasUser = investment_service.find_user_by_id(investment.user_id)
        if hasUser is None:
            return make_response(make_response({"error": "User not found"}), 404)
        if investment_service.add_invest(investment) is not None:
            return make_response(make_response({"message": "investiment add success"}), 201)
        else:
            return make_response(make_response({"error": "investiment add failed"}), 400)
           
    except Exception as e:
        return make_response(make_response({"error": str(e)}), 400)
        
