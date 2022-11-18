from typing import List, Dict, Any

from fastapi.encoders import jsonable_encoder
from users.models.data.users import User
from users.models.data.usersdb import users_tbl
from collections import namedtuple


class UserRepository:
    def insert_user(self, user: User) -> bool:
        try:
            users_tbl[user.user_id] = user
        except:
            return False
        return True

    def update_user(self, user_id: int, details: Dict[str, Any]) -> bool:
        try:
            profile = users_tbl[user_id]
            profile_enc = jsonable_encoder(profile)
            profile_dict = dict(profile_enc)
            profile_dict.update(details)
            users_tbl[user_id] = namedtuple(
                'User', profile_dict.keys())(*profile_dict.values())
        except:
            return False
        return True

    def delete_user(self, user_id: int) -> bool:
        try:
            del users_tbl[user_id]
        except:
            return False
        return True

    def get_all_users(self):
        return users_tbl
