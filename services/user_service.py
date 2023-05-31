from typing import List
from models.user import User


class UserService:

    def __init__(self, repository):
        """
        UserService  Sets a repository object for interacting with user data in the database.
        Injection of the repository allows for decoupling of the UserService logic from the specifics of the repository implementation.
        Args:
            repository: An object that implements the necessary methods for interacting with user data in a database.
        """
        self.repository = repository

    def create_user(self, user: User) -> User:
        """
        Creates a new user using the given user object and returns the created user.

        Args:
        user: User object containing information of the user to be created.

        Returns:
        The created User object.
        """

        return self.repository.create(user)

    def get_all_users(self) -> List[User]:
        """
        Retrieves all the User objects from a repository using the find_all() method,
        then attempts to create a list containing a dictionary representation of each User object
        using the json() method of each User object, and returns that list.

        Returns:
            A list of User objects.
        """
        users = self.repository.find_all()
        try:
            return [user.json() for user in users]
        except:
            return []

    def get_user_by_id(self, user_id: int) -> User:
        """
        Retrieves a user from the database using their ID.

        Args:
            user_id: Integer value representing the ID of the user.

        Returns:
            The User object associated with the given ID, if it exists in the database.
            None if the user is not found.
        """
        print('user id', user_id)
        user = self.repository.find_by_id(user_id)
        # user object is None if the user is not found in the database.
        print('user', user.username)
        return user if user else None

    def update_user(self, data: User) -> bool:
        """
        Update a existing user in the repository.

        Args:
            data (User): The updated User object to be stored in the repository.

        Returns:
            bool: True if the user is successfully updated.
        """
        print('broking here', data.id, data.username)
        user = self.get_user_by_id(data.id)
        if user:
            self.repository.update(user)
            return True
        print('return false')
        return False

    def delete_user(self, id) -> bool:
        """
        Deletes a user from the database table.

        Args:
        - id: The ID of the user to be deleted

        Returns:
        - A boolean value indicating whether the user was successfully deleted (True) or not (False).
        """

        return self.repository.delete(id)

    def is_email_or_name_in_use(self, user) -> bool:
        """
        Checks if a given user object has a username or email that already exists in the repository.

        Args:
            user: A user object to check for duplicates.

        Returns:
            bool: True if a matching user object is found.
        """
        props = ['username', 'email']
        found_user = self.repository.find_user_by_prop_list(
            user, props)

        return found_user is not None
