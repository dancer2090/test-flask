from sqlalchemy import exc
from flask import abort
from db.models import BlogPost
from db import db



def get_all_posts():
    try:
        posts = BlogPost.query.all()
        return [post.to_dict() for post in posts]
    except exc.SQLAlchemyError as e:
        return abort(500, description=e._message())


def get_post_by_id(id):
    try:
        post = BlogPost.query.get(id)

        if not post:
            abort(404, description="Post not found")

        return post.to_dict()
    except exc.SQLAlchemyError as e:
        return abort(500, description=e._message())


def create_post(title, content, author_id):
    try:
        print(title, content, author_id)
        post = BlogPost(title=title, content=content, author_id=author_id)
        db.session.add(post)
        db.session.commit()
        obj = post.to_dict()
        return obj
    except exc.SQLAlchemyError as e:
        return abort(500, description=e._message())