
from flask import jsonify, make_response, request
from helpers.validators import ValidModel
from models.user import User
from services.user_service import UserService
from repositories.user_repository_alchemy import RepositoryUserImpSQLAlchemy
from extensions import db

user_repository = RepositoryUserImpSQLAlchemy()
user_service = UserService(user_repository)


@ValidModel(User)
def create_user():
    data = request.json
    user = User(**data)
    try:
        if (not user_service.is_email_or_name_in_use(user)):
            created = user_service.create_user(user)

        else:
            return make_response(jsonify({'message': 'username or email already exists'}), 400)
        return make_response(jsonify({'message': 'user created', 'user': created.json()}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user', 'error': str(e)}), 500)


def get_user(user_id):
    user = user_service.get_user_by_id(user_id)

    if user:
        return jsonify({'id': user['id'], 'username': user['username'], 'email': user['email']})
    else:
        return jsonify({'message': 'User not found'}), 404


@ValidModel(User)
def update_user(user_id):
    # Parse request data and create a new user object
    data = request.json
    user = User(data['username'], data['email'])
    user.id = user_id

    try:
        user_service.update_user(user)
        return jsonify({'message': 'User updated successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 404


def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 404


def get_all():
    try:
        users = user_service.get_all_users()
        return jsonify({'users': [user for user in users]})
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users', 'error': str(e)}), 500)
