from datetime import datetime, timedelta
from flask import current_app as app
import jwt

from . import db


class Users(db.Model):
    __bind_key__ = 'flaskaled-srv1'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    hash_pass = db.Column(db.LargeBinary(), nullable=False)
    salt = db.Column(db.LargeBinary(), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, email, hash_pass, salt, is_admin):
        self.email = email
        self.hash_pass = hash_pass
        self.salt = salt
        self.is_admin = is_admin

    def __repr__(self):
        return {
            'id': self.id,
            'email': self.email,
            'hash_pass': self.hash_pass,
            'salt': self.salt,
            'is_admin': self.is_admin
        }

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'is_admin': self.is_admin
        }

    def auth_token(self):
        try:
            time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            payload = {
                'exp': time + timedelta(days=0, seconds=5),
                'iat': time,
                'user': self.json()
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(
                auth_token,
                app.config.get('SECRET_KEY')
            )
            return payload['user']
        except jwt.ExpiredSignatureError:
            return 'Signature expired . Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
