from typing import List
from models.user import User


class UserService:

    def __init__(self, repository):
        self.repository = repository

    def create_user(self, user):
        return self.repository.create(user)

    def get_all_users(self) -> List[User]:
        users = self.repository.find_all()
        try:
            return [user.json() for user in users]
        except:
            return []

    def get_user_by_id(self, user_id) -> User:
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

    def is_email_or_name_in_use(self, user) -> bool:
        return self.repository.find_user_by_name_or_email(user)
