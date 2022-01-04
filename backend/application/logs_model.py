from . import db

class Logs(db.Model):
    __bind_key__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    id_user = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.String(), nullable=False)
    table = db.Column(db.String(), nullable=False)
    action = db.Column(db.String(), nullable=False)
    has_succeeded = db.Column(db.Boolean, nullable=False)
    status_code = db.Column(db.Integer, nullable=False)

    def __init__(self, date, user, ip, table, action, status):
        self.date = date
        self.user = user
        self.ip = ip
        self.table = table
        self.action = action
        self.status = status

    def __repr__(self):
        return {
            'id': self.id,
            'date': self.date,
            'user': self.user,
            'ip': self.ip,
            'table': self.table,
            'action': self.action,
            'status': self.status
        }
