import sqlalchemy as alchemy

from models import db


class User(db.Model):
    """用户表的模型"""

    __tablename__ = "user"

    id = alchemy.Column(alchemy.Integer, primary_key=True, autoincrement=True)
    username = alchemy.Column(alchemy.String(256), nullable=False, unique=True, doc="username")
    password = alchemy.Column(alchemy.String(256), nullable=False, doc="password")
    is_admin = alchemy.Column(alchemy.Boolean, nullable=False, default=False, doc="is administrator")

    def __init__(self, username: str, password: str, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return "<%s %r>" % (self.__class__, self.username)
