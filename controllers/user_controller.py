
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
        return make_response({'message': 'error creating user', 'error': str(e)}, 500)


def get_user(id):
    user = user_service.get_user_by_id(id)

    if user:
        # OK (201) created (200)
        return make_response({'message': 'user found', 'user': user.json()}, 200)

    else:
        return jsonify({'message': 'User not found'}), 404


@ValidModel(User)
def update_user(id):
    data = request.json
    user = User(**data)
    user.id = id

    try:
        if (not user_service.update_user(user)):
            return make_response({'message': 'user not found'}, 404)
        return make_response({'message': 'User updated successfully'}, 200)
    except Exception as e:
        return jsonify({'message': str(e)}), 500


def delete_user(id):
    try:
        if (user_service.delete_user(id)):
            return jsonify({'message': 'User deleted successfully'})
        return make_response({'message': 'user not found'}, 404)
    except Exception as e:
        return jsonify({'message': str(e)}), 500


def get_all():
    try:
        users = user_service.get_all_users()
        return jsonify({'users': [user for user in users]})
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users', 'error': str(e)}), 500)
