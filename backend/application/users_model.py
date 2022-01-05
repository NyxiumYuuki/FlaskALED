from . import db


class Users(db.Model):
    __bind_key__ = 'db-users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    nickname = db.Column(db.String(), nullable=False)
    hash_pass = db.Column(db.LargeBinary(), nullable=False)
    salt = db.Column(db.LargeBinary(), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, email, nickname, hash_pass, salt, is_admin):
        self.email = email
        self.hash_pass = hash_pass
        self.nickname = nickname
        self.salt = salt
        self.is_admin = is_admin

    def __repr__(self):
        return {
            'id': self.id,
            'email': self.email,
            'nickname': self.nickname,
            'hash_pass': self.hash_pass,
            'salt': self.salt,
            'is_admin': self.is_admin
        }

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'nickname': self.nickname,
            'is_admin': self.is_admin
        }
