import hashlib
from typing import Dict

AUTHORIZED_USERS: Dict[str, str] = {
    "admin": "5f4dcc3b5aa765d61d8327deb882cf99"  # This is 'password' in MD5
}

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    hashed_password: str = hash_password(password)
    return username in AUTHORIZED_USERS and AUTHORIZED_USERS[username] == hashed_password
