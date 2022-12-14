from flask import Flask

from .views import init_views
from .config import EnvironConfig
from .extension import extension_register


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(EnvironConfig)
    init_views(_app)
    extension_register(_app)

    return _app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=8001)
