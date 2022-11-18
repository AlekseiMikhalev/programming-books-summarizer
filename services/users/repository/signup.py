from users.models.data.usersdb import user_signup_tbl
from users.models.data.usersdb import Signup


class UserSignupRepository:
    def insert_item(self, item: Signup):
        try:
            user_signup_tbl[item.sign_id] = item
        except:
            return False
        return True

    def delete_item(self, sign_id: int):
        try:
            del user_signup_tbl[sign_id]
        except:
            return False
        return True

    def get_item(self, sign_id: int):
        try:
            account = user_signup_tbl[sign_id]
        except:
            return None
        return account
