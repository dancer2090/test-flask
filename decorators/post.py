from functools import wraps
from flask import abort
import services.post as post_service


def post_exist(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(kwargs)
        is_post_exist = post_service.check_is_post_exist(1)
        if not is_post_exist:
            return abort(404, description='Post not found')
        return f(*args, **kwargs)

    return decorated_function
