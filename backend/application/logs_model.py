from . import db


class Logs(db.Model):
    __bind_key__ = 'flaskaled-srv2'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.TIMESTAMP(), nullable=False)
    id_user = db.Column(db.Integer, nullable=True)
    ip = db.Column(db.String(), nullable=False)
    table = db.Column(db.String(), nullable=False)
    action = db.Column(db.String(), nullable=False)
    message = db.Column(db.String(), nullable=False)
    has_succeeded = db.Column(db.Boolean, nullable=False)
    status_code = db.Column(db.Integer, nullable=False)

    def __init__(self, date, id_user, ip, table, action, message, has_succeeded, status_code):
        self.date = date
        self.id_user = id_user
        self.ip = ip
        self.table = table
        self.action = action
        self.message = message
        self.has_succeeded = has_succeeded
        self.status_code = status_code

    def __repr__(self):
        return {
            'id': self.id,
            'date': self.date,
            'id_user': self.id_user,
            'ip': self.ip,
            'table': self.table,
            'action': self.action,
            'message': self.message,
            'has_succeeded': self.has_succeeded,
            'status_code': self.status_code
        }

    def json(self):
        return self.__repr__()
