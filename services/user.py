from sqlalchemy import exc, or_
from flask import abort
from db import db
from db.models import User
import hashlib


def check_is_user_exist(email, username):
    try:
        user = db.session.execute(
            db.select(User).where(
                or_(
                    User.email == email,
                    User.username == username
                )
            )
        ).one_or_none()

        if user:
            return True
        return False
    except exc.SQLAlchemyError as e:
        return abort(500, description=e._message())


def create_user(email, password, username):
    try:
        is_user_exist = check_is_user_exist(email, username)
        if is_user_exist:
            abort(400, description="User already exists")
        else:
            password_hash = hashlib.md5(password.encode()).hexdigest()
            user = User(username=username, email=email, password_hash=password_hash)
            db.session.add(user)
            db.session.commit()
            obj = user.to_dict()
            del obj["password_hash"]
            return obj
    except exc.SQLAlchemyError as e:
        return abort(500, description=e._message())


def get_user_by_email_password(email, password):
    try:
        password_hash = hashlib.md5(password.encode()).hexdigest()
        user = User.query.filter_by(
            email=email,
            password_hash=password_hash
        ).one_or_none()

        if not user:
            abort(404, description="User not found")

        obj = user.to_dict()
        del obj["password_hash"]
        return obj

    except exc.SQLAlchemyError as e:
        print(e)
        return abort(500, description=e._message())


def get_user_by_username(username):
    try:
        user = User.query.filter_by(
            username=username,
        ).one_or_none()

        if not user:
            abort(404, description="User not found")
        return user.to_dict()
    except exc.SQLAlchemyError as e:
        print(e)
        return abort(500, description=e._message())

