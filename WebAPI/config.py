
class DATABASE(object):
    HOST = "100.100.21.90"
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
