import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KEY = os.environ.get('SECRET_KEY', None)
    FLASK_APP = os.environ.get('FLASK_APP', None)
    FLASK_ENV = os.environ.get('FLASK_ENV', None)

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI_1 = os.environ.get('DATABASE_URL_1', None)
    SQLALCHEMY_DATABASE_URI_2 = os.environ.get('DATABASE_URL_2', None)
    SQLALCHEMY_BINDS = {
        'users': SQLALCHEMY_DATABASE_URI_1,
        'logs': SQLALCHEMY_DATABASE_URI_2
    }


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    STAGING = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
