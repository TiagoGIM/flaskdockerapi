from flask import Blueprint, jsonify, make_response, request
from models.user import User
from services.user_service import UserService
from repositories.user_repository_alchemy import RepositoryUserImpSQLAlchemy
from extensions import db

user_controller = Blueprint('user_controller', __name__, url_prefix='/users')
user_repository = RepositoryUserImpSQLAlchemy()
user_service = UserService(user_repository)


@user_controller.route('/createuserstable', methods=['GET'])
def create_table():
    db.create_all()
    return jsonify({'message': 'table created'})


@user_controller.route('/', methods=['POST'])
def create_user():
    # Parse request data and create a new user object
    data = request.json
    try:
        user = {'username': data['username'], 'email': data['email']}
        if (not user_service.is_unique_user(user['username'])):
            user_service.create_user(user)
        else:
            # 400 means bad request.  A client
            return make_response(jsonify({'message': 'username or email already exists'}), 400)

        return make_response(jsonify({'message': 'user created', 'user': user.json()}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user', 'error': str(e)}), 500)


@user_controller.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    # Call the get_user method in the UserService
    user = user_service.get_user_by_id(user_id)

    if user:
        print(user)
        return jsonify({'id': user['id'], 'username': user['username'], 'email': user['email']})
    else:
        return jsonify({'message': 'User not found'}), 404


@user_controller.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    # Parse request data and create a new user object
    data = request.json
    user = User(data['username'], data['email'])
    user.id = user_id

    try:
        # Call the update_user method in the UserService
        user_service.update_user(user)
        return jsonify({'message': 'User updated successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 404


@user_controller.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Call the delete_user method in the UserService
        user_service.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 404


"""
@user_controller.route('/', methods=['POST'])
def create():
    try:
        data = request.get_json()
        user = UserService.create(data['username'], data['email'])
        return make_response(jsonify({'message': 'user created', 'user': user.json()}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user', 'error': str(e)}), 500)


@user_controller.route('/', methods=['GET'])
def get_all():
    try:
        users = UserService.get_all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users', 'error': str(e)}), 500)

"""
