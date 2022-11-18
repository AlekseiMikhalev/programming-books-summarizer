from typing import Dict, Any
from users.repository.users import UserRepository
from users.models.data.users import User


class UserService:
    def __init__(self):
        self.repo: UserRepository = UserRepository()

    def add_user(self, user: User):
        result = self.repo.insert_user(user)
        return result

    def update_user(self, user_id: int, details: Dict[str, Any]):
        result = self.repo.update_user(user_id, details)
        return result

    def remove_user(self, user_id: int):
        result = self.repo.delete_user(user_id)
        return result

    def list_users(self):
        return self.repo.get_all_users()
