from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from .models import db

migrate = Migrate()
jwt = JWTManager()


def extension_register(app: Flask):
    db.init_app(app)
    # db.app = app
    migrate.init_app(app, db)
    jwt.init_app(app)
