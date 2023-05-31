from flask import Blueprint
from controllers.user_controller import delete_user, get_all, get_user, create_user, update_user
from controllers.stock_controller import create_stock, delete_stock, get_all_stocks, get_stock, update_stock
from controllers.portfolio_controller import create_portfolio, delete_portfolio, get_portfolio, update_portfolio

user = Blueprint('user_controller', __name__, url_prefix='/users')
stock = Blueprint('stock_controller', __name__, url_prefix='/stocks')
wallet = Blueprint('wallet_controller', __name__, url_prefix='/wallet')

user.route('/', methods=['POST'])(create_user)

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


# routes to crud wallet
wallet.route('/', methods=['POST'])(create_portfolio)
wallet.route('/<int:id>', methods=['GET'])(get_portfolio)
wallet.route('/<int:id>', methods=['DELETE'])(delete_portfolio)
wallet.route('/<int:id>', methods=['PUT'])(update_portfolio)

all_routes = [user, stock, wallet]
