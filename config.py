import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI_1 = os.environ.get('DATABASE_URL_1', None)
    SQLALCHEMY_DATABASE_URI_2 = os.environ.get('DATABASE_URL_2', None)


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    STAGING = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
