from database import (create_admin,
                      view_admin_by_username)
import bcrypt
import exceptions
from validators import is_int,is_valid_data,checkpass
def hash_password(password):
    hashed_pw=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    return hashed_pw.decode()

def check_password(password,hashed):
    return bcrypt.checkpw(password.encode(),hashed.encode())

def exist_admin(username):
    admin=view_admin_by_username(username)
    return admin if admin else None

def register_admin(username,password):
    if not is_valid_data(username):
        raise exceptions.ValidationError("username is required.")
    if not is_valid_data(password):
        raise exceptions.ValidationError("password cannot be empty.")
    username=username.strip()
    password=password.strip()
    if not len(username)<=30:
        raise exceptions.ValidationError("Maximum length of username is 30")
    if not checkpass(password):
        raise exceptions.ValidationError("Password must be at least 8 characters long,"
        " contain a number, an uppercase letter,"
        " a lowercase letter, and a special character")
    if exist_admin(username):
        raise exceptions.ValidationError("Username already exists.")
    hashedpw=hash_password(password)
    return create_admin(username,hashedpw)

def login_admin(username,password):
    if not is_valid_data(username):
        raise exceptions.ValidationError("username is required.")
    if not is_valid_data(password):
        raise exceptions.ValidationError("password cannot be empty.")
    
    admin=view_admin_by_username(username)
    if not admin:
        raise exceptions.AuthenticationError("Invalid Credentials.")
    if not check_password(password,admin.password_hash):
        raise exceptions.AuthenticationError("Invalid Credentials.")
    return True