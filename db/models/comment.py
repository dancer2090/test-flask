from db import db
from sqlalchemy_serializer import SerializerMixin


class Comment(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Comment "{self.id}">'

