import hashlib
import json
from typing import Dict

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    hashed_password = hash_password(password)
    return username in AUTHORIZED_USERS and AUTHORIZED_USERS[username] == hashed_password

def load_authorized_users(filepath: str) -> Dict[str, str]:
    with open(filepath, 'r') as file:
        return json.load(file)

AUTHORIZED_USERS = load_authorized_users('config.json')
