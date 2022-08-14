import sqlalchemy as alchemy

from ..models import db


class Article(db.Model):
    """文章表的模型"""

    __tablename__ = "article"

    id = alchemy.Column(alchemy.Integer, primary_key=True, autoincrement=True)
    title = alchemy.Column(alchemy.String(256), nullable=False)
    content = alchemy.Column(alchemy.Text, nullable=False)

    # 外键: alchemy.ForeignKey("表名.字段名"); 字段类型要和外键的字段类型保持一致
    author_id = alchemy.Column(alchemy.Integer, alchemy.ForeignKey("user.id"))

    # 多表关系映射; 必须先定义好与对方表进行绑定的外键, 可以实现: article.author = model
    # param-1: Model的类名, 必须是已经自定义好的Model。
    # param-2: 反向引用,对方访问我的时候的字段名称
    author = db.relationship("User", backref="articles")

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
