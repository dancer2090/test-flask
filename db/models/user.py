from db import db
from sqlalchemy.orm import deferred
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = deferred(db.Column(db.String(), nullable=False))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<User "{self.id}">'

