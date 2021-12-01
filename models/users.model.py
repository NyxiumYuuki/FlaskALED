from app import db1


class Users(db1.Model):
    __tablename__ = 'users'

    id = db1.Column(db1.Integer, primary_key=True)
    email = db1.Column(db1.String())
    login = db1.Column(db1.String())
    hashPass = db1.Column(db1.String())
    role = db1.Column(db1.String())

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
