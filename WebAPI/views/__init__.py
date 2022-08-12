from flask import Flask

from .welcome import welcome_view
from .users import users_view
from .article import article_view


def init_views(app: Flask):
    app.register_blueprint(welcome_view)
    app.register_blueprint(users_view)
    app.register_blueprint(article_view)
