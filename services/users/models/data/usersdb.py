from typing import Dict
from users.models.data.users import Login, User, Signup

users_tbl: Dict[int, User] = dict()
user_login_tbl: Dict[int, Login] = dict()
user_signup_tbl: Dict[int, Signup] = dict()
