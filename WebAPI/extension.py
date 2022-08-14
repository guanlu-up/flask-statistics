from flask import Flask
from flask_migrate import Migrate

from .models import db

migrate = Migrate()


def extension_register(app: Flask):
    db.init_app(app)
    # db.app = app
    migrate.init_app(app, db)
