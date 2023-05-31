from abc import ABC, abstractmethod
from typing import List
from models.user import User


class Repository(ABC):

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def delete(self, stock):
        pass

    @abstractmethod
    def update(self, user) -> User:
        pass
