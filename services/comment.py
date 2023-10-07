from sqlalchemy import exc
from flask import abort
from db.models import Comment
from db import db


def get_comments_by_post_id(post_id):
    try:
        posts = Comment.query.filter_by(post_id=post_id).all()
        return [post.to_dict() for post in posts]
    except exc.SQLAlchemyError as e:
        return abort(500, description=e._message())


def create_comment(content, author_id, post_id):
    try:
        post = Comment(content=content, author_id=author_id, post_id=post_id)
        db.session.add(post)
        db.session.commit()
        obj = post.to_dict()
        return obj
    except exc.SQLAlchemyError as e:
        return abort(500, description=e._message())