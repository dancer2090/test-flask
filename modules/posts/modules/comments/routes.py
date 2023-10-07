from flask import Blueprint, abort, request
from werkzeug.exceptions import HTTPException
from decorators.auth import auth_required
from flask_validate_json import validate_json
from modules.posts.modules.comments.validators import create_comment_schema
import services.comment as comment_service

comments_blueprint = Blueprint('comments', __name__, url_prefix='/<int:post_id>/comments')


@comments_blueprint.route('/', methods=["POST"])
@validate_json(create_comment_schema)
@auth_required
def create_comment(post_id):
    try:
        current_user = request.user
        content = request.json["content"]

        return comment_service.create_comment(content, current_user["id"], post_id)
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)


@comments_blueprint.route('/', methods=["GET"])
@auth_required
def get_comments(post_id):
    try:
        return comment_service.get_comments_by_post_id(post_id)
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)