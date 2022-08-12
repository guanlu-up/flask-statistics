from flask import Blueprint
from flask import request

article_view = Blueprint("article", __name__, url_prefix="/article")


@article_view.route("", methods=["GET", "POST"])
def new_article():
    if request.method == "GET":
        user_id = request.args.get("user_id")
        title = request.json.get("title")
        content = request.json.get("content")

        if user_id is None:
            return {'message': 'Required param is missing'}, 400

        from models.users import Article
        from models import session
        from database.users import UsersDB

        article = Article("Flask-Used", "this is a test flask")
        db = UsersDB()
        admin = db.query_by_username("admin")
        article.author = admin
        session.add(article)
        session.commit()

        return {"status": 200, "message": "ok"}

    if request.method == "PUT":
        return {"status": 200, "message": "ok"}
