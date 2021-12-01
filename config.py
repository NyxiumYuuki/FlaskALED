import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', None)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
