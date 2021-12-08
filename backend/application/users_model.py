from . import db


class Users(db.Model):
    __bind_key__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    login = db.Column(db.String(), nullable=False)
    hashPass = db.Column(db.String(), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, email, login, hash_pass, role):
        self.email = email
        self.login = login
        self.hashPass = hash_pass
        self.role = role

    def __repr__(self):
        return {
            'id': self.id,
            'email': self.email,
            'login': self.login,
            'hashPass': self.hashPass,
            'role': self.role
        }
