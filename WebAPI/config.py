import datetime


class DATABASE(object):
    HOST = "192.168.0.114"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = "root"
    DB = "flask"
    URI = (USERNAME, PASSWORD, HOST, PORT, DB)


class EnvironConfig(object):
    DEBUG = True
    ENV = "development" if DEBUG else "production"
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(*DATABASE.URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "10#*secret#*%$key!@01"

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=1)
