from ..database.base import BaseDB
from ..models.article import Article

from ..models import session


class ArticleDB(BaseDB):
    """数据库; article表"""

    def __init__(self):
        super(ArticleDB, self).__init__(Article)

    def new_article(self, title: str, content: str, user: Article):
        """创建新文章"""
        model = self._model(title, content)
        model.author = user
        session.add(model)
        session.commit()
