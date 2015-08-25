from functools import wraps

from flask import request, abort

from app.security.tokenutils import get_user_from_auth_token


def logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('authorization')
        user = get_user_from_auth_token(token)

        if not user:
            abort(401)
        user.token = token
        kwargs['user'] = user

        return f(*args, **kwargs)

    return decorated_function
