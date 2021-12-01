from app import db2


class Logs(db2.Model):
    __tablename__ = 'logs'

    id = db2.Column(db2.Integer, primary_key=True)
    date = db2.Column(db2.Date())
    user = db2.Column(db2.String())
    ip = db2.Column(db2.String())
    table = db2.Column(db2.String())
    action = db2.Column(db2.String())
    status = db2.Column(db2.String())

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
