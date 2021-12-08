from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
import sys
import os

db = SQLAlchemy()
patch_all()


def create_app():
    app = Flask(__name__)
    FLASK_ENV = os.environ.get('FLASK_ENV', None)
    if FLASK_ENV == 'production':
        app.config.from_object("config.ProductionConfig")
    elif FLASK_ENV == 'staging':
        app.config.from_object("config.StagingConfig")
    elif FLASK_ENV == 'development':
        app.config.from_object("config.DevelopmentConfig")
    else:
        app.config.from_object("config.Config")

    if app.config['SQLALCHEMY_DATABASE_URI_1'] is None or app.config['SQLALCHEMY_DATABASE_URI_2'] is None:
        print('No ENV Variable for DATABASE_URL_1 or DATABASE_URL_2')
        sys.exit(1)
    else:
        print('ENV Variables passed : ', app.config['SQLALCHEMY_BINDS'])

    # import routes
    return app

    # db.init_app(app)
    # db.create_all()

    # return app
