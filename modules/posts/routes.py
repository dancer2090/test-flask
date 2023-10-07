from flask import Blueprint, abort, request
from werkzeug.exceptions import HTTPException
from decorators.auth import auth_required
from flask_validate_json import validate_json
from modules.posts.validators import create_post_schema
from modules.posts.modules import comments
import services.post as post_service

posts_blueprint = Blueprint('posts', __name__, url_prefix='/posts')
posts_blueprint.register_blueprint(comments)


@posts_blueprint.route('/', methods=["POST"])
@validate_json(create_post_schema)
@auth_required
def create_post():
    try:
        current_user = request.user
        title = request.json["title"]
        content = request.json["content"]
        return post_service.create_post(title, content, current_user["id"])
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)


@posts_blueprint.route('/', methods=["GET"])
@auth_required
def get_posts():
    try:
        return post_service.get_all_posts()
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)


@posts_blueprint.route('/<int:id>', methods=["GET"])
@auth_required
def get_post(id):
    try:
        return post_service.get_post_by_id(id)
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)
