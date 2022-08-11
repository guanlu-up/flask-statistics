from flask import Blueprint, redirect, url_for

welcome_view = Blueprint("welcome", __name__)


@welcome_view.route("/", methods=["GET"])
def helloworld():
    return {"satus": 200, "message": "helloworld 中国"}


@welcome_view.route("/welcome", methods=["GET"])
def welcome_api():
    return redirect(url_for("welcome.helloworld"))


@welcome_view.route("/database", methods=["GET"])
def mysql_testing():
    from models import db
    from sqlalchemy.engine.base import Connection, Engine
    engine: Engine = db.get_engine()
    connect: Connection = engine.connect()
    result = connect.execute("select 1")
    print(result.fetchone())
    connect.close()
    return {"status": 200, "message": "database connect success!"}
