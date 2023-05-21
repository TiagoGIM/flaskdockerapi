from flask import Blueprint
from controllers.user_controller import delete_user, get_all, get_user, create_user, update_user

user = Blueprint('user_controller', __name__, url_prefix='/users')

user.route('/', methods=['POST'])(create_user)
user.route('/<user_id>', methods=['GET'])(get_user)
user.route('/list', methods=['GET'])(get_all)
user.route('/<user_id>', methods=['PUT'])(update_user)
user.route('/<user_id>', methods=['DELETE'])(delete_user)
