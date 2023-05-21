from typing import List
from models.user import User


class UserService:

    def __init__(self, repository):
        self.repository = repository

    def create_user(self, user):
        # new_user = User(username=user['username'], email=user['email'])
        self.repository.create(username=user['username'], email=user['email'])

    def get_all_users(self) -> List[User] | List[None]:
        users = self.repository.getAll()
        return [user.json() for user in users]

    def get_user_by_id(self, user_id) -> User | None:
        user = self.repository.find_by_id(user_id)
        return user.json() if user else None

    def update_user(self, id, data) -> bool:
        user = self.repository.getById(id)
        if user:
            user.username = data['username']
            user.email = data['email']
            self.repository.update(user)
            return True
        return False

    def delete_user(self, id) -> bool:
        user = self.repository.get_by_id(id)
        if user:
            self.repository.delete(user)
            return True
        return False

    def is_unique_user(self, username) -> bool:
        return self.repository.find_by_username(username)
