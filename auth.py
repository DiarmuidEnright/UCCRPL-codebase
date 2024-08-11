import hashlib

AUTHORIZED_USERS = {
    "admin": "5f4dcc3b5aa765d61d8327deb882cf99"  
}

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username, password):
    hashed_password = hash_password(password)
    if username in AUTHORIZED_USERS and AUTHORIZED_USERS[username] == hashed_password:
        return True
    return False
