from flask import Blueprint
from controllers.user_controller import delete_user, get_all, get_user, create_user, update_user
from controllers.stock_controller import create_stock, delete_stock, get_all_stocks, get_stock, update_stock
user = Blueprint('user_controller', __name__, url_prefix='/users')
stock = Blueprint('stock_controller', __name__, url_prefix='/stocks')


user.route('/', methods=['POST'])(create_user)
user.route('/<int:id>', methods=['GET'])(get_user)
user.route('/list', methods=['GET'])(get_all)
user.route('/<int:id>', methods=['PUT'])(update_user)
user.route('/<int:id>', methods=['DELETE'])(delete_user)


stock.route('/', methods=['POST'])(create_stock)
stock.route('/<int:id>', methods=['GET'])(get_stock)
stock.route('/list', methods=['GET'])(get_all_stocks)
stock.route('/<int:id>', methods=['DELETE'])(delete_stock)
stock.route('/<int:id>', methods=['PUT'])(update_stock)
