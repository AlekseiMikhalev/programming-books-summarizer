from enum import Enum
from datetime import datetime


class UserStatus(str, Enum):
    Reader = 'Reader'
    ActiveReader = 'Active Reader'
    RapidReader = 'Rapid Reader'


class User:
    def __init__(self, user_id: int, fname: str, lname: str, status: UserStatus) -> None:
        self.user_id: int = user_id
        self.fname: str = fname
        self.lname: str = lname
        self.status: UserStatus = status

    def __repr__(self) -> str:
        return ' '.join([str(self.user_id), self.fname, self.lname, self.status])

    def __str__(self) -> str:
        return ' '.join([str(self.user_id), self.fname, self.lname, self.status])


class Signup:
    def __init__(self, sign_id: int, user_id: int, username: str, password: str):
        self.sign_id: int = sign_id
        self.user_id: int = user_id
        self.username: str = username
        self.password: str = password

    def __repr__(self) -> str:
        return ' '.join([str(self.sign_id), str(self.user_id), self.username, self.password])

    def __str__(self) -> str:
        return ' '.join([str(self.sign_id), str(self.user_id), self.username, self.password])


class Login:
    def __init__(self, user_id: int, username: str, password: str):
        self.user_id: int = user_id
        self.username: str = username
        self.password: str = password

    def __repr__(self) -> str:
        return ' '.join([str(self.user_id), self.username, self.password])

    def __str__(self) -> str:
        return ' '.join([str(self.user_id), self.username, self.password])

