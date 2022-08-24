import sqlalchemy as alchemy
from werkzeug.security import check_password_hash

from ..extension import db


class User(db.Model):
    """用户表的模型"""

    __tablename__ = "user"

    id = alchemy.Column(alchemy.Integer, primary_key=True, autoincrement=True)
    username = alchemy.Column(alchemy.String(256), nullable=False, unique=True, doc="username")
    password = alchemy.Column(alchemy.String(256), nullable=False, doc="password")
    is_admin = alchemy.Column(alchemy.Boolean, nullable=False, default=False, doc="is administrator")
    is_delete = alchemy.Column(alchemy.Boolean, nullable=False, default=False, doc="is deleted?")

    def __init__(self, username: str, password: str, is_admin=False, is_delete=False, extension=None):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.is_delete = is_delete
        if extension is None:
            extension = UserExtension()
        self.extension = extension

    def __repr__(self):
        return "<%s %r>" % (self.__class__, self.username)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class UserExtension(db.Model):

    __tablename__ = "user_extension"

    id = alchemy.Column(alchemy.Integer, primary_key=True, autoincrement=True)
    school = alchemy.Column(alchemy.String(128))
    interest = alchemy.Column(alchemy.String(128))
    user_id = alchemy.Column(alchemy.Integer, db.ForeignKey("user.id"))

    # 定义1对1的关系表; db.backref("name") 和直接填 "name"是一样的,但uselist改为False后则变为了1对1
    # 为True时,对方Model访问我时会返回一个列表; 为False时,对方Model访问我时只会返回一个具体实例
    user = db.relationship("User", backref=db.backref("extension", uselist=False))

    def __init__(self, school=None, interest=None):
        self.school = school
        self.interest = interest
