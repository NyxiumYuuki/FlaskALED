import os
import sys
from flask import Flask
from config import Config, DevelopmentConfig, StagingConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy

if __name__ == '__main__':
    app = Flask(__name__)

    PORT = int(os.environ.get('PORT', 33507))
    db1 = SQLAlchemy(app)
    db2 = SQLAlchemy(app)

    FLASK_ENV = os.environ.get('FLASK_ENV', None)
    if FLASK_ENV == 'production':
        DEBUG = ProductionConfig.DEBUG
    elif FLASK_ENV == 'stage':
        DEBUG = StagingConfig.DEBUG
    elif FLASK_ENV == 'development':
        DEBUG = DevelopmentConfig.DEBUG
    else:
        sys.exit("Error FLASK_ENV")

    if Config.SQLALCHEMY_DATABASE_URI_1 is None or Config.SQLALCHEMY_DATABASE_URI_2 is None:
        sys.exit("Error SQLALCHEMY_DATABASE_URI_1 or/and SQLALCHEMY_DATABASE_URI_2")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)