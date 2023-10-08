from functools import wraps
from flask import abort
import services.post as post_service


def post_exist(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(kwargs)
        if not kwargs['post_id']:
            return abort(404, description='Post not found')

        is_post_exist = post_service.check_is_post_exist(kwargs['post_id'])

        if not is_post_exist:
            return abort(404, description='Post not found')
        return f(*args, **kwargs)

    return decorated_function
