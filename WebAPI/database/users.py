from database.base import BaseDB
from models.users import User


class UsersDB(BaseDB):
    """数据库; Users表"""

    def __init__(self):
        super(UsersDB, self).__init__(User)

    def update(self, _id: int, key: str, value):
        if not isinstance(key, str) or not hasattr(self._model, key):
            raise AttributeError("key is not a valid attribute!")
        super(UsersDB, self).update(_id, key, value)
