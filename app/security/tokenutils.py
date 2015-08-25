from datetime import datetime
import hashlib

from app import app
from app import redis_conn
from app.models.user import User


def create_auth_token(user):
    pre_token = user.pk + app.config['SALT'] + str(datetime.now().timestamp())
    token = hashlib.sha512(pre_token.encode()).hexdigest()
    redis_conn.setex(token, user.to_json(), 900)
    return token

def update_user(token, user):
    redis_conn.setex(token, user.to_json(), 900)

def get_user_from_auth_token(token):
    redis_user = redis_conn.get(token)
    if not redis_user:
        return None

    redis_conn.expire(token, 900)

    user = User()
    user = user.from_json(redis_user.decode())

    return user
