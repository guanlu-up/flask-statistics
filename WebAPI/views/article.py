from flask import Blueprint
from flask import request

from database.users import UsersDB
from database.article import ArticleDB

article_view = Blueprint("article", __name__, url_prefix="/article")


@article_view.route("", methods=["POST"])
def new_article():
    if request.method == "POST":
        """创建文章"""
        user_id = request.json.get("user_id")
        title = request.json.get("title")
        content = request.json.get("content")
        if user_id is None or title is None or content is None:
            return {'message': 'Required param is missing'}, 400

        user_db = UsersDB()
        author = user_db.query_by_id(user_id)
        if author is None:
            return {'message': 'user_id invalid!'}, 400
        article_db = ArticleDB()
        article_db.new_article(title, content, author)

        return {"status": 200, "message": "ok"}


@article_view.route("/<int:article_id>", methods=["GET"])
def browse_article(article_id):
    if request.method == "GET":
        """获取文章"""
        article_db = ArticleDB()
        article = article_db.query_by_id(article_id)
        if article is None:
            return {"message": "not found!"}, 400
        info = {
            "author_id": article.author_id,
            "title": article.title,
            "content": article.content
        }
        return {"status": 200, "message": info}
