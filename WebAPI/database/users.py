from database.base import BaseDB
from models.users import User


class UsersDB(BaseDB):
    """数据库; Users表"""

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
