from database import (create_admin,
                      get_admin_by_username)
import bcrypt
import exceptions

def hash_password(password):
    hashed_pw=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    return hashed_pw.decode()

def check_password(password,hashed):
    return bcrypt.checkpw(password.encode(),hashed.encode())

def exist_admin(username):
    admin=get_admin_by_username(username)
    return admin if admin else None

def register_admin(username,password):
    if exist_admin(username):
        raise exceptions.ValidationError("Username already exists.")
    hashedpw=hash_password(password)
    user=create_admin(username,hashedpw)
    if not user:
        raise exceptions.AuthenticationError("Admin registration failed.")
    return user

def login_admin(username,password):
    admin=get_admin_by_username(username)
    if not admin:
        raise exceptions.AuthenticationError("Invalid Credentials.")
    if check_password(password,admin.password_hash):
        return True 
    else:
        raise exceptions.AuthenticationError("Invalid Credentials.")