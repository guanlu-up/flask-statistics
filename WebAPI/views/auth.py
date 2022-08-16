from flask import Blueprint, request
from flask_jwt_extended import create_access_token, create_refresh_token

from ..database.users import UsersDB, UserExtensionDB

auth_view = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_view.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = UsersDB().query_by_username(username)
    if user is None or not user.verify_password(password):
        return {"status": 401, "message": "Wrong username or password"}

    access_token = create_access_token(user.username, additional_claims={"is_admin": user.is_admin})
    refresh_token = create_refresh_token(user.username)
    data = {
        "username": username,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    return {"status": 200, "message": data}
