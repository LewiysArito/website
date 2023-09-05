import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "12451355123"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = "[Flask]"
    FLASK_MAIL_SENDER = f"Flask ADMIN {os.environ.get('MAIL_USERNAME')}"
    FLASK_ADMIN = os.environ.get("FLASK_ADMIN")
    '''тут хранятся общие настройки'''

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/demos1"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/demos1"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/demos2"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
