"""
sqlalchemy.Column():
    -----args-----
    :param: name
    -----kwargs-----
    :param: autoincrement
    :param: default
    :param: doc
    :param: key
    :param: index
    :param: info
    :param: nullable
    :param: onupdate
    :param: primary_key
    :param: server_default
    :param: server_onupdate
    :param: quote
    :param: unique
    :param: system
    :param: comment
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.scoping import scoped_session

db = SQLAlchemy()
session: scoped_session = db.session
