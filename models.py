from app import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    login = db.Column(db.String())
    hashPass = db.Column(db.String())
    role = db.Column(db.String())

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
