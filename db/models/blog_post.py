from db import db
from sqlalchemy_serializer import SerializerMixin


class BlogPost(db.Model, SerializerMixin):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.Text())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<BlogPost "{self.id}">'

