from flask import make_response, request
from helpers.validators import ValidModel
from models.investiments import Investment
from repositories.investment_repository_alchemy import RepositoryInvestmentImpSQLAlchemy
from services.investments_service import InvestimentService

invetment_repository = RepositoryInvestmentImpSQLAlchemy
investment_service =  InvestimentService(invetment_repository)

@ValidModel(Investment)
def create_investment():
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
 
def get_all_investments(user_id):
    try:
        hasUser = investment_service.find_user_by_id(user_id)
        if hasUser:
            investments = investment_service.get_all_investments_by_user_id(user_id)
            return make_response(make_response({"investments": investments}), 200)
        else:
            return make_response(make_response({"error": "user not found"}), 404)
    except Exception as e:
        return make_response(make_response({"error": str(e)}), 400)       

@ValidModel(Investment)
def update_investment():
    data = request.json
    
    try:
        investment = Investment(**data)
        hasUser = investment_service.find_user_by_id(investment.user_id)
        investment_found = investment_service.find_by_id(investment.id)

        if hasUser is None:
            return make_response(make_response({"error": "User not found"}), 404)
        if investment_found is None:
            return make_response(make_response({"error": "Investment not found"}), 404)
            
        if investment_service.update_investment(investment) is not None:
            return make_response(make_response({"message": "investiment update success"}), 201)
        else:
            return make_response(make_response({"error": "investiment update failed"}), 400)
           
    except Exception as e:
        return make_response(make_response({"error": str(e)}), 400)
    
    
def delete_investment(id:int):
    user_id = request.args.get('user_id')
    try:
        hasUser = investment_service.find_user_by_id(user_id)

        if hasUser is None:
            return make_response(make_response({"error": "User not found"}), 404)            
        if investment_service.delete_investment(id):
            return make_response(make_response({"message": "investiment delete success"}), 201)
        return make_response(make_response({"error": "Investment not found"}), 404)

    except Exception as e:
        return make_response(make_response({"error": str(e)}), 400)