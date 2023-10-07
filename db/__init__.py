from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from constants import POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER, POSTGRES_HOST, POSTGRES_PORT, MIGRATION_DIR

db = SQLAlchemy()


def register_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    db.init_app(app)
    migrate = Migrate(app, db, directory=MIGRATION_DIR)

    return db, migrate

