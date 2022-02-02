print("Import os")
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    FLASK_APP = os.environ.get('FLASK_APP', None)
    FLASK_ENV = os.environ.get('FLASK_ENV', None)
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT', 5000)

    API_URL = os.environ.get('API_URL', 'http://127.0.0.1:5000/api/')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    ALLOW_ORIGIN = os.environ.get('ALLOW_ORIGIN', None)


class ProductionConfig(Config):
    DEBUG = False
    API_URL = os.environ.get('API_URL', 'http://10.1.2.10:5000/api/')


class TestingConfig(Config):
    TESTING = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
