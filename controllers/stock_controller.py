
from functools import wraps
from flask import request, jsonify, make_response
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
        created = stock_service.create_stock(stock)
        return make_response(jsonify({'message': 'Stock created', 'stock ': created.json()}), 201)
    except Exception as e:
        return make_response(str(e), 500)


def get_all_stocks():
    stocks = stock_service.get_all_stocks()
    response_stocks = [stock.json() for stock in stocks]
    print(response_stocks)
    try:
        return make_response(jsonify(response_stocks), 200)
    except Exception as e:
        return make_response(str(e), 500)


def get_stock(id):
    try:
        stock = stock_service.get_by_id(id)
        if stock:
            return make_response(jsonify({'stock    ': stock.json()}), 200)
        return make_response(jsonify({'message': 'stock not found'}), 404)
    except:
        return make_response(jsonify({'message': 'error getting user'}), 500)


def update_stock(id):
    try:
        stock = stock_service.get_by_id(id)

        if stock:
            data = request.json
            stock_to_update = Stock(**data)
            updated_stock = stock_service.update(stock_to_update)
            return make_response(jsonify({'message': 'Stock updated', 'updated ': updated_stock.json()}), 200)

        return make_response(jsonify({'message': 'stock not found'}), 404)
    except Exception as e:
        return make_response(str(e), 500)


def delete_stock(id):
    try:
        if (stock_service.delete(id)):
            return make_response(str(id), 200)
        return make_response("Not found", 404)
    except Exception as e:
        return make_response(str(e), 500)
