from flask import Blueprint
from flask import request

from models import users as users_model
from models import session
from database import UsersDB

users_view = Blueprint("users", __name__, url_prefix="/users")


@users_view.route("", methods=["GET", "POST", "PUT"])
def add_user():
    if request.method == "GET":
        _id = request.args.get("id")
        if _id is None or not str(_id).isdigit():
            return {"status": 400, "message": "required params is missing"}

        db = UsersDB()
        user: users_model.User = db.query_by_id(int(_id))
        if user is None:
            return {"status": 400, "message": "user not exist!"}
        userinfo = {
            "username": user.username,
            "password": user.password,
            "is_admin": user.is_admin,
        }

        return {"status": 200, "message": userinfo}

    if request.method == "POST":
        username = request.json.get("username")
        password = request.json.get("password")
        is_admin = request.json.get("is_admin")

        if username is None or password is None or is_admin is None:
            return {'message': 'Required param is missing'}, 400

        user = users_model.User(username=username, password=password, is_admin=is_admin)
        session.add(user)
        session.commit()

        return {"status": 200, "message": "success"}

    if request.method == "PUT":
        db = UsersDB()
        db.update(1, "is_admin", True)

        return {"status": 200, "message": "success"}
