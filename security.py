
from werkzeug.security import safe_str_cmp
from application.models import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.check_password(password):
        return user
    else:
        return None

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)

