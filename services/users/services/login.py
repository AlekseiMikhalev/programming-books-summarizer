from users.repository.login import UserLoginRepository
from users.models.data.users import Login


class UserLoginService:
    def __init__(self):
        self.repo: UserLoginRepository = UserLoginRepository()

    def add_user_login(self, login: Login):
        result = self.repo.insert_login(login)
        return result

    def update_login_password(self, user_id: int, newpass: str):
        result = self.repo.update_password(user_id, newpass)
        return result

    def remove_user_login(self, user_id: int):
        result = self.repo.delete_login(user_id)
        return result

    def get_user_login(self, username):
        return self.repo.get_login(username)

    def list_login(self):
        return self.repo.get_all_login()
