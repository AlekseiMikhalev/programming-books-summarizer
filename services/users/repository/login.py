from users.models.data.usersdb import user_signup_tbl, user_login_tbl
from users.models.data.usersdb import Login


class UserLoginRepository:
    def insert_login(self, sign_id: int) -> bool:
        try:
            account = user_signup_tbl[sign_id]
            login = Login(user_id=account.sign_id,
                          username=account.username, password=account.password)
            user_login_tbl[account.user_id] = login
        except:
            return False
        return True

    def update_password(self, user_id: int, newpass: str) -> bool:
        try:
            login = user_login_tbl[user_id]
            login.password = newpass
        except:
            return False
        return True

    def delete_login(self, user_id: int) -> bool:
        try:
            del user_login_tbl[user_id]
        except:
            return False
        return True

    def get_login(self, username: str):
        list_login = [account for account in user_login_tbl.values()
                      if account.username == username]
        if not len(list_login) == 0:
            return list_login[0]
        else:
            return None

    def get_all_login(self):
        return user_login_tbl
