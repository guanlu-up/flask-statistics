from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.scoping import scoped_session

db = SQLAlchemy()
session: scoped_session = db.session
