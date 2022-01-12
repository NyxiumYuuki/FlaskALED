from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
import os

db = SQLAlchemy()


def create_app(flask_env='development'):
    app = Flask(__name__, instance_relative_config=False)
    if flask_env == 'production':
        app.config.from_object("config.ProductionConfig")
    elif flask_env == 'testing':
        app.config.from_object("config.TestingConfig")
    elif flask_env == 'development':
        app.config.from_object("config.DevelopmentConfig")
    else:
        app.config.from_object("config.Config")

    if app.config['SQLALCHEMY_DATABASE_URI_1'] is None or app.config['SQLALCHEMY_DATABASE_URI_2'] is None:
        print('No ENV Variable for DATABASE_URL_USERS or DATABASE_URL_LOGS')
        sys.exit(1)
    else:
        print('ENV Variables passed : ', app.config['SQLALCHEMY_BINDS'])

    print('init_app')
    db.init_app(app)
    with app.app_context():
        print('import routes')
        from . import routes
        app.register_blueprint(routes.bp)
        print('db.create_all')
        db.create_all()
        print('db created')
    return app
