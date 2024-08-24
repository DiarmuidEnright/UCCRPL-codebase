import hashlib
import os
from typing import Dict

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    hashed_password = hash_password(password)
    return username in AUTHORIZED_USERS and AUTHORIZED_USERS[username] == hashed_password

AUTHORIZED_USERS: Dict[str, str] = {
    "admin": os.getenv("ADMIN_PASSWORD_HASH")
}
