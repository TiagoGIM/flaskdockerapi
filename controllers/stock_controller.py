
from functools import wraps
from flask import abort, request, jsonify, make_response
from helpers.validators import ValidModel
from models.user import Stock
from repositories.stock_repository_alchemy import RepositoryStockImpSQLAlchemy
from services.stock_service import StockService

stock_repository = RepositoryStockImpSQLAlchemy

stock_service = StockService(stock_repository)


@ValidModel(Stock)
def create_stock():
    data = request.json
    stock = Stock(**data)

    try:
        stock_service.create_stock(stock)
        return make_response("stock created", 201)
    except Exception as e:
        return make_response(str(e), 500)
