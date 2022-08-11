from typing import Union

from sqlalchemy.orm.query import Query
from flask_sqlalchemy.model import DefaultMeta

from models import session


class BaseDB(object):
    """base class; 数据库查询"""
    _model: Union[DefaultMeta] = None

    def __init__(self, model):
        """
        :param model: 自定义的Model类(继承自db.Model)
        """
        self._model = model
        self._query: Query = self._model.query

    def query_by_id(self, _id: int, _raise=False):
        """ 根据id进行查询
        :param _id: 要查找的数据条目id
        :param _raise: 如果未查到是否报错
        :return: Model; self._model
        """
        query: Query = self._query.filter_by(id=_id)
        return query.one() if _raise else query.first()

    def update(self, _id: int, key, value):
        """ 根据id查询,更新目标条目的字段值
        :param _id: 要查找的数据条目id
        :param key: 字段名称
        :param value: 字段值
        :return: Model; self._model
        """
        query: Query = self._query.filter_by(id=_id)
        query.update({key: value}, synchronize_session="fetch")
        session.commit()
        return query.first()
