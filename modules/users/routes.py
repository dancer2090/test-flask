from flask import Blueprint, abort, jsonify, request
from werkzeug.exceptions import HTTPException
from decorators.auth import auth_required
from flask_validate_json import validate_json
from modules.users.validators import register_user_schema, user_authentication_schema
import services.user as user_service
from utils.ctypto import generate_token

users_blueprint = Blueprint('users', __name__, url_prefix='/users')


@users_blueprint.route('/', methods=["POST"])
@validate_json(register_user_schema)
def create_user():
    try:
        return user_service.create_user(
            request.json["email"],
            request.json["password"],
            request.json["username"],
        )
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)


@users_blueprint.route('/login', methods=["POST"])
@validate_json(user_authentication_schema)
def login_user():
    try:
        email = request.json['email']
        password = request.json['password']
        user = user_service.get_user_by_email_password(email, password)
        token = generate_token({'id': user['id'], 'email': user['email'], 'username': user['username']})
        return jsonify({'token': token})

    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)


@users_blueprint.route('/<string:username>', methods=["GET"])
@auth_required
def get_user(username):
    current_user = request.user
    try:
        if username == 'current':
            username = current_user['username']
        return user_service.get_user_by_username(username)
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, description=e.description)
        else:
            abort(500)

