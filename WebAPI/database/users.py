from sqlalchemy import Column

from models import session
from database.base import BaseDB
from models.users import User, UserExtension


class UsersDB(BaseDB):
    """数据库; user表"""

    def __init__(self):
        super(UsersDB, self).__init__(User)

    def query_by_username(self, username: str, _raise=False):
        """ 根据用户名进行查询
        :param username: 要查找的数据条目用户名
        :param _raise: 如果未查到是否报错
        :return: Model; self._model
        """
        query = self._query.filter(self._model.username == username)
        return query.one() if _raise else query.first()


class UserExtensionDB(BaseDB):
    """数据库; user_extension表"""

    def __init__(self):
        super(UserExtensionDB, self).__init__(UserExtension)

    def query_by_userid(self, user_id: int, _raise=False):
        """ 根据id进行查询
        :param user_id: 要查找的数据条目的user_id
        :param _raise: 如果未查到是否报错
        :return: Model; self._model
        """
        query = self._query.filter_by(user_id=user_id)
        return query.one() if _raise else query.first()

    def update(self, user_id, mapper: dict, **kwargs):
        """根据user_id查询,更新目标条目的字段值"""
        kwargs.update(mapper)
        if not kwargs:
            return None, False
        query = self._query.filter_by(user_id=user_id)
        query.update(kwargs, synchronize_session="fetch")
        session.commit()
        return query.first(), True
