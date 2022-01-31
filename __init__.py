from flask import Flask
from flask_cors import CORS


def create_app(flask_env='development'):
    app = Flask(__name__, instance_relative_config=False, static_url_path='')
    origin = app.config.get('ALLOW_ORIGIN')
    if origin is None:
        origin = ['http://127.0.0.1:5000', 'http://localhost:5000']
    CORS(app, supports_credentials=True, origins=origin)
    if flask_env == 'production':
        app.config.from_object("config.ProductionConfig")
    elif flask_env == 'testing':
        app.config.from_object("config.TestingConfig")
    elif flask_env == 'development':
        app.config.from_object("config.DevelopmentConfig")
    else:
        app.config.from_object("config.Config")

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
    return app
