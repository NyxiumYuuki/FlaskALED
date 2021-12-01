import os
from flask import Flask
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy

if __name__ == '__main__':
    app = Flask(__name__)

    PORT = int(os.environ.get('PORT', 33507))
    db = SQLAlchemy(app)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret_key')
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(host='0.0.0.0', port=PORT, debug=False)