from functools import wraps
from flask import abort, request
from utils.ctypto import is_valid_token

error_description = "Authorization: failed"


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get("Authorization"):
            return abort(401, description=error_description)

        auth = request.headers.get("Authorization").split(" ")

        if len(auth) != 2 and auth[0] != "Bearer":
            return abort(401, description=error_description)

        token = auth[1]

        is_valid, user_data = is_valid_token(token)

        if not is_valid:
            return abort(401, description=error_description)

        request.user = user_data
        return f(*args, **kwargs)

    return decorated_function
