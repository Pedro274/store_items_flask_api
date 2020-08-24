from Models.user_model import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_user_by_username(username)
    if user and safe_str_cmp(user.json().password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_user_by_id(user_id)