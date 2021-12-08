from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask import current_app as app
from backend import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()