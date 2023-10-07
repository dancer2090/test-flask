from flask import Flask
from modules import posts, users
from utils.errors import register_app_errors
from db import register_db

def create_app():
    # Init the app here
    app = Flask(__name__)

    # Setup error handlers
    register_app_errors(app)

    # Init the DB here
    db, migrate = register_db(app)

    # Init the routes here
    app.register_blueprint(users)
    app.register_blueprint(posts)

    return app, db, migrate

# Join models to force migrations
import db.models
