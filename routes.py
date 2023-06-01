from flask import Blueprint
from controllers.user_controller import delete_user, get_all, get_user, create_user, update_user
from controllers.stock_controller import create_stock, delete_stock, get_all_stocks, get_stock, update_stock
from controllers.portfolio_controller import create_portfolio, delete_portfolio, get_portfolio, update_portfolio
from controllers.investment_controller import create_investment, get_all_investments, update_investment, delete_investment

user = Blueprint('user_controller', __name__, url_prefix='/users')
stock = Blueprint('stock_controller', __name__, url_prefix='/stocks')
basket = Blueprint('wallet_controller', __name__, url_prefix='/basket')
investment = Blueprint('investments_controller', __name__, url_prefix='/investments')

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


# routes to crud basket
basket.route('/', methods=['POST'])(create_portfolio)
basket.route('/<int:id>', methods=['GET'])(get_portfolio)
basket.route('/<int:id>', methods=['DELETE'])(delete_portfolio)
basket.route('/<int:id>', methods=['PUT'])(update_portfolio)

# routes to crud investments
investment.route('/', methods=['POST'])(create_investment)
investment.route('/list/<int:user_id>', methods=['GET'])(get_all_investments)
investment.route('/', methods=['PUT'])(update_investment)
investment.route('/<int:id>', methods=['DELETE'])(delete_investment)


all_routes = [user, stock, basket, investment]
