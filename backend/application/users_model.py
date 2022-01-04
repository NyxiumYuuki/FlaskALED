from . import db


class Users(db.Model):
    __bind_key__ = 'flaskaled-srv1'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    login = db.Column(db.String(), nullable=False)
    hash_pass = db.Column(db.LargeBinary(), nullable=False)
    salt = db.Column(db.LargeBinary(), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, email, login, hash_pass, salt, is_admin):
        self.email = email
        self.login = login
        self.hash_pass = hash_pass
        self.salt = salt
        self.is_admin = is_admin

    def __repr__(self):
        return {
            'id': self.id,
            'email': self.email,
            'login': self.login,
            'hash_pass': self.hash_pass,
            'salt': self.salt,
            'is_admin': self.is_admin
        }

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'login': self.login,
            'is_admin': self.is_admin
        }

    def get_id(self):
        return self.id

    def get_salt(self):
        return self.salt
