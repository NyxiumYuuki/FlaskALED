import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    FLASK_APP = os.environ.get('FLASK_APP', None)
    FLASK_ENV = os.environ.get('FLASK_ENV', None)

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI_1 = os.environ.get('DATABASE_URL_USERS', None)
    SQLALCHEMY_DATABASE_URI_2 = os.environ.get('DATABASE_URL_LOGS', None)
    SQLALCHEMY_BINDS = {
        'db-users': SQLALCHEMY_DATABASE_URI_1,
        'db-logs': SQLALCHEMY_DATABASE_URI_2
    }

    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    ALLOW_ORIGIN = os.environ.get('ALLOW_ORIGIN', '*')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(Config):
    STAGING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
