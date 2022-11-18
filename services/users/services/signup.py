from users.repository.signup import UserSignupRepository
from users.models.data.users import Signup


class UserSignupService:
    def __init__(self):
        self.repo: UserSignupRepository = UserSignupRepository()

    def add_signup(self, signup: Signup):
        result = self.repo.insert_item(signup)
        return result

    def get_signup(self, sign_id: int):
        result = self.repo.get_item(sign_id)

    def delete_signup(self, sign_id: int):
        result = self.repo.delete_item(sign_id)
        return result
