from enum import Enum
from datetime import datetime

class UserStatus(str, Enum):
    Reader='Reader'
    ActiveReader='Active Reader'
    RapidReader='Rapid Reader'
    
class User:
    