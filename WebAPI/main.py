from flask import Flask

from models import db
from views import init_views
from config import EnvironConfig


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(EnvironConfig)
    db.init_app(_app)
    db.app = _app
    init_views(_app)

    return _app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=8001)
